from army import Army
from battle_state import BattleState, SimpleBattleState, StochasticBattleState
from collections import defaultdict, Counter
from multiprocessing import Manager
from cPickle import dump
from networkx import DiGraph
import itertools, argparse, gzip
from util import parallelExec
from progressbar import ProgressBar


def main(typ):
    battles = generateBattles(BattleState if typ!="simple" else SimpleBattleState)
    
    if typ=="full":
        textMod = "all"
    elif typ=="simple":
        textMod = "all *simplified*"
    elif typ=="small":
        textMod = "some of the"
        battles = [
            BattleState.fromUnits(6, 1, 2, 2), 
            BattleState.fromUnits(6, 1, 3, 2), 
            BattleState.fromUnits(6, 1, 4, 2), 
            BattleState.fromUnits(6, 1, 5, 2), 
            BattleState.fromUnits(6, 1, 6, 2), 
            BattleState.fromUnits(6, 1, 7, 2),
            BattleState.fromUnits(2, 2, 6, 1), 
            BattleState.fromUnits(3, 2, 6, 1), 
            BattleState.fromUnits(4, 2, 6, 1), 
            BattleState.fromUnits(5, 2, 6, 1), 
            BattleState.fromUnits(6, 2, 6, 1), 
            BattleState.fromUnits(7, 2, 6, 1),
        ]
    
    print "-----------------------------------------------------------"
    print "Calculating battle chances for {} possible battle cases".format(textMod)
    print "Assuming max infantry of {} and max artillery of {}".format(MAX_INFANTRY, MAX_ARTILLERY)
    print "--> Number of battle cases: {}".format(len(battles))
    updateGraph(battles, "battle_graph_" + typ)

def updateGraph(battles, name):
    print "calculating battle chances..."
    battleGraph, battleOutcomes = calcIntensive(battles)
    
    # convert to a graph object
    print "converting to graph object..."
    graph = convertToGraph(battleGraph)
    del battleGraph
    
    # add expected result
    print "adding death battle statistics to the graph..."
    combineResults(graph, battleOutcomes)
    del battleOutcomes
    
    # save
    filename = name+".pkl"
    print "dumping battle chance graph to: {}".format(filename)
    with gzip.open(filename, "wb") as fil:
        dump(graph, fil, 2)
    
    print "Number of nodes in battle chances graph: {}".format(graph.number_of_nodes())
    print "Number of edges in battle chances graph: {}".format(graph.number_of_edges())

def combineResults(graph, battleOutcomes):
    bar = ProgressBar(max_value=len(battleOutcomes))
    for i,(battle, outcomes) in enumerate(battleOutcomes.iteritems()):
        graph.add_node(battle, outcome=StochasticBattleState(*zip(*outcomes.iteritems())))
        bar.update(i+1)

def convertToGraph(battleGraph):
    nestedList = map(lambda item: [(item[0], k, v) for k,v in item[1].iteritems()] , battleGraph.iteritems())
    edgeList = [ee for e in nestedList for ee in e]
    graph = DiGraph()
    graph.add_weighted_edges_from(edgeList)
    return graph

def calcIntensive(battles):
    with Manager() as manager:
        battleGraph = manager.dict()
        lock = manager.Lock()
        parallelExec(calcBattleChances, ((battle, battleGraph, lock) for battle in battles))
        
        print "calculating expected to the death battle..."
        battleOutcomes = manager.dict()
        parallelExec(battleEndChances, ((battle, battleGraph, battleOutcomes, lock) for battle in battles))
        
        print "copying result..."
        battleGraph = dict(battleGraph)
        battleOutcomes = dict(battleOutcomes)
    return battleGraph, battleOutcomes

def calcBattleChances(battle, battleGraph, lock):
    # prevent unnecessary calculations
    if battle.hasEnded(): return
    lock.acquire()
    alreadyCalculated = battle in battleGraph
    lock.release()
    if alreadyCalculated: return
    
    # determine chances for possible outcomes of this battle
    battleOutcomes = defaultdict(int)
    for _ in xrange(NR_OF_SAMPLES):
        battleOutcomes[battle.simulate()] += 1
    battleChances = {k: v/float(NR_OF_SAMPLES) for k,v in battleOutcomes.iteritems()}
    
    lock.acquire()
    if battle not in battleGraph:
        battleGraph[battle] = battleChances
    lock.release()
    
    # also calculate all subsequent possible battles
    for sampleBattle in battleChances:
        # recurse to build up the chance tree
        # Note: max recursive depth equals max infantry
        calcBattleChances(sampleBattle, battleGraph, lock)

def battleEndChances(battle, graph, battleOutcomes, lock):
    # prevent unnecessary calculations
    if battle.hasEnded(): return None
    lock.acquire()
    exists = battle in battleOutcomes
    if exists: battleOutcome = battleOutcomes[battle]
    lock.release()
    if exists: return battleOutcome
    
    # recursively calculate
    battleChances = Counter()
    for nextBattle, nextChance in graph[battle].iteritems():
        nextBattleOutcome = battleEndChances(nextBattle, graph, battleOutcomes, lock)
        if nextBattleOutcome==None:
            battleChances[nextBattle] += nextChance
        else:
            for b in nextBattleOutcome:
                nextBattleOutcome[b] *= nextChance
            battleChances += nextBattleOutcome
    
    # update battleOutcomes
    lock.acquire()
    if battle not in battleOutcomes:
        battleOutcomes[battle] = battleChances
    lock.release()
    return battleChances

def generateBattles(battleStateType=BattleState):
    combinations = itertools.product(
        xrange(MAX_INFANTRY+1), 
        xrange(MAX_ARTILLERY+1), 
        xrange(MAX_INFANTRY+1), 
        xrange(MAX_ARTILLERY+1)
    )
    battles = map(lambda args: battleStateType.fromUnits(*args), combinations)
    return [b for b in battles if not b.hasEnded()]

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Update a battle chance graph.')
    parser.add_argument('type', type=str, choices=["full", "simple", "small"], help='battle chance graph type')
    parser.add_argument('--samples', type=int, default=5000, help='nr of samples per battle case')
    parser.add_argument('--maxinfantry', type=int, default=9, help='max nr of infantry')
    parser.add_argument('--maxartillery', type=int, default=5, help='max nr of artillery')
    
    args = parser.parse_args()
    NR_OF_SAMPLES = args.samples
    MAX_INFANTRY = args.maxinfantry
    MAX_ARTILLERY = args.maxartillery
    
    main(args.type)
