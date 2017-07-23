import argparse
import gzip
import itertools
import os
from collections import defaultdict, Counter
from multiprocessing import Manager
from pickle import dump

from networkx import DiGraph
from progressbar import ProgressBar

from battle_state import BattleState, StochasticBattleState
from util import parallel_exec

USE_GZIP = False


def main():
    typ = "full"
    battles = generate_battles()

    print("-----------------------------------------------------------")
    print("Calculating battle chances for all battle cases")
    print("Assuming max infantry of {} and max artillery of {}".format(MAX_INFANTRY, MAX_ARTILLERY))
    print("--> Number of battle cases: {}".format(len(battles)))
    update_graph(battles, "_graph/" + typ)


def update_graph(battles, name):
    print("calculating battle graph...")
    battle_graph, battle_stats = calc_intensive(battles)

    # convert to a graph object
    print("converting to graph object...")
    graph = convert_to_graph(battle_graph)
    del battle_graph

    # add expected result
    print("adding battle statistics to the graph...")
    add_battle_stats(graph, battle_stats)
    del battle_stats

    # save
    filename = name + ".pkl"
    print("dumping battle graph to: {}".format(filename))
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with (gzip.open(filename, "wb") if USE_GZIP else open(filename, "wb")) as fil:
        dump(graph, fil, 2)

    print("Number of nodes in battle graph: {}".format(graph.number_of_nodes()))
    print("Number of edges in battle graph: {}".format(graph.number_of_edges()))


def add_battle_stats(graph, battle_stats):
    bar = ProgressBar(max_value=graph.number_of_nodes())
    for i, battle in enumerate(graph.nodes()):
        graph.add_node(battle, {typ: stats[battle] for typ, stats in battle_stats.items() if battle in stats})
        bar.update(i + 1)


def convert_to_graph(battle_graph):
    nested_list = list(map(lambda item: [(item[0], k, v) for k, v in item[1].items()], battle_graph.items()))
    edge_list = [ee for e in nested_list for ee in e]
    graph = DiGraph()
    graph.add_weighted_edges_from(edge_list)
    return graph


def simple_attacker_retreat_strat(battle, round_stat, full_battle_stat):
    if full_battle_stat.attacker_won() > full_battle_stat.defender_won():
        return False
    if round_stat.value_advantage()[0] > 0:
        return False
    return True


def simple_defender_retreat_strat(battle, round_stat, full_battle_stat):
    if full_battle_stat.defender_won() > full_battle_stat.attacker_won():
        return False
    if round_stat.value_advantage()[0] < 0:
        return False
    return True


def calc_intensive(battles):
    with Manager() as manager:
        battle_graph = manager.dict()
        round_stats = manager.dict()
        lock = manager.Lock()
        parallel_exec(calc_battle_round_chances, ((battle, battle_graph, round_stats, lock) for battle in battles))

        print("calculating full battle chances...")
        full_battle_chances = manager.dict()
        full_battle_stats = manager.dict()
        parallel_exec(calc_full_battle_chances,
                      ((battle, battle_graph, full_battle_chances, full_battle_stats, lock) for battle in battles))

        print("calculating retreat battle chances...")
        retreat_battle_chances = manager.dict()
        retreat_battle_stats = manager.dict()
        parallel_exec(calc_retreat_battle_chances,
                      ((battle, battle_graph, retreat_battle_chances, retreat_battle_stats, lock,
                        round_stats, full_battle_stats, simple_attacker_retreat_strat,
                        simple_defender_retreat_strat) for battle in battles))

        print("copying result...")
        battle_graph = dict(battle_graph)
        round_stats = dict(round_stats)
        full_battle_stats = dict(full_battle_stats)
        retreat_battle_stats = dict(retreat_battle_stats)
    return battle_graph, {"round": round_stats, "full": full_battle_stats, "retreat": retreat_battle_stats}


def calc_battle_round_chances(battle, battle_graph, round_stats, lock):
    # prevent unnecessary calculations
    lock.acquire()
    exists = battle in battle_graph
    if not exists and battle.has_ended():
        battle_graph[battle] = {}
    lock.release()
    if exists or battle.has_ended():
        return

    # determine chances for possible outcomes of this battle round
    round_outcomes = defaultdict(int)
    for _ in range(NR_OF_SAMPLES):
        round_outcomes[battle.simulate()] += 1
    round_chances = {k: v / float(NR_OF_SAMPLES) for k, v in round_outcomes.items()}
    round_stat = StochasticBattleState.from_dict(round_chances)

    lock.acquire()
    if battle not in battle_graph:
        battle_graph[battle] = round_chances
        round_stats[battle] = round_stat
    lock.release()

    # also calculate all subsequent possible battles
    for sampleBattle in round_chances:
        # recurse to build up the chance tree
        # Note: max recursive depth equals max infantry
        calc_battle_round_chances(sampleBattle, battle_graph, round_stats, lock)


def calc_full_battle_chances(battle, graph, full_battle_chances, full_battle_stats, lock):
    # prevent unnecessary calculations
    if battle.has_ended():
        return Counter({battle: 1})
    lock.acquire()
    exists = battle in full_battle_chances
    if exists:
        battle_chances = full_battle_chances[battle]
    lock.release()
    if exists:
        return battle_chances

    # recursively calculate
    battle_chances = Counter()
    for nextRound, chance in graph[battle].items():
        next_round_battle_chances = calc_full_battle_chances(nextRound, graph, full_battle_chances, full_battle_stats,
                                                             lock)
        for b in next_round_battle_chances:
            next_round_battle_chances[b] *= chance
        battle_chances += next_round_battle_chances
    battle_stat = StochasticBattleState.from_dict(battle_chances)

    # update full_battle_chances
    lock.acquire()
    if battle not in full_battle_chances:
        full_battle_chances[battle] = battle_chances
        full_battle_stats[battle] = battle_stat
    lock.release()
    return battle_chances


def calc_retreat_battle_chances(battle, graph, retreat_battle_chances, retreat_battle_stats, lock,
                                round_battle_stats, full_battle_stats, attacker_retreat_strat, defender_retreat_strat,
                                first=True):
    # prevent unnecessary calculations
    # note: 'first' is meant to disallow retreating even before the first battle round
    if battle.has_ended():
        return Counter({battle: 1})
    lock.acquire()
    exists = battle in retreat_battle_chances
    if exists and not first:
        battle_chances = retreat_battle_chances[battle]
    elif not first:
        if attacker_retreat_strat(battle, round_battle_stats[battle], full_battle_stats[battle]):
            battle_chances = Counter({battle.attacker_retreats(): 1})
            retreat_battle_chances[battle] = battle_chances
            exists = True
        elif defender_retreat_strat(battle, round_battle_stats[battle], full_battle_stats[battle]):
            battle_chances = Counter({battle.defender_retreats(): 1})
            retreat_battle_chances[battle] = battle_chances
            exists = True
    lock.release()
    if exists:
        return battle_chances

    # recursively calculate
    battle_chances = Counter()
    for nextRound, chance in graph[battle].items():
        next_round_battle_chances = calc_retreat_battle_chances(nextRound, graph, retreat_battle_chances,
                                                                retreat_battle_stats,
                                                                lock,
                                                                round_battle_stats, full_battle_stats,
                                                                attacker_retreat_strat,
                                                                defender_retreat_strat, first=False)
        for b in next_round_battle_chances:
            next_round_battle_chances[b] *= chance
        battle_chances += next_round_battle_chances
    battle_stat = StochasticBattleState.from_dict(battle_chances)

    # update retreat_battle_chances
    lock.acquire()
    if battle not in retreat_battle_chances:
        retreat_battle_chances[battle] = battle_chances
        retreat_battle_stats[battle] = battle_stat
    lock.release()
    return battle_chances


def generate_battles():
    combinations = itertools.product(
        range(MAX_INFANTRY + 1),
        range(MAX_ARTILLERY + 1),
        range(MAX_INFANTRY + 1),
        range(MAX_ARTILLERY + 1)
    )
    normal_battles = list(map(lambda a: BattleState.from_units(*a), combinations))
    trench_battles = [b.with_trench() for b in normal_battles]
    return [b for b in itertools.chain(normal_battles, trench_battles) if not b.has_ended()]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Update a battle chance graph.')
    parser.add_argument('--samples', type=int, default=5000, help='nr of samples per battle case')
    parser.add_argument('--max-infantry', type=int, default=8, help='max nr of infantry')
    parser.add_argument('--max-artillery', type=int, default=4, help='max nr of artillery')

    args = parser.parse_args()
    NR_OF_SAMPLES = args.samples
    MAX_INFANTRY = args.max_infantry
    MAX_ARTILLERY = args.max_artillery

    main()
