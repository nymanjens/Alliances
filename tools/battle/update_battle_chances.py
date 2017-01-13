from army import Army
from battle_state import BattleState, StochasticBattleState
from collections import defaultdict, Counter
from multiprocessing import Manager
from cPickle import dump
from networkx import DiGraph
import itertools, argparse, gzip
from util import parallelExec
from progressbar import ProgressBar

USE_GZIP = False

def main():
    typ = "full"
    battles = generateBattles()
    
    print "-----------------------------------------------------------"
    print "Calculating battle chances for all battle cases"
    print "Assuming max infantry of {} and max artillery of {}".format(MAX_INFANTRY, MAX_ARTILLERY)
    print "--> Number of battle cases: {}".format(len(battles))
    updateGraph(battles, "_graph/" + typ)

def updateGraph(battles, name):
    print "calculating battle graph..."
    battleGraph, battleStats = calcIntensive(battles)
    
    # convert to a graph object
    print "converting to graph object..."
    graph = convertToGraph(battleGraph)
    del battleGraph
    
    # add expected result
    print "adding battle statistics to the graph..."
    addBattleStats(graph, battleStats)
    del battleStats
    
    # save
    filename = name+".pkl"
    print "dumping battle graph to: {}".format(filename)
    with (gzip.open(filename, "wb") if USE_GZIP else open(filename, "wb")) as fil:
        dump(graph, fil, 2)
    
    print "Number of nodes in battle graph: {}".format(graph.number_of_nodes())
    print "Number of edges in battle graph: {}".format(graph.number_of_edges())

def addBattleStats(graph, battleStats):
    bar = ProgressBar(max_value=graph.number_of_nodes())
    for i, battle in enumerate(graph.nodes()):
        graph.add_node(battle, {typ: stats[battle] for typ,stats in battleStats.iteritems() if stats.has_key(battle)})
        bar.update(i+1)

def convertToGraph(battleGraph):
    nestedList = map(lambda item: [(item[0], k, v) for k,v in item[1].iteritems()] , battleGraph.iteritems())
    edgeList = [ee for e in nestedList for ee in e]
    graph = DiGraph()
    graph.add_weighted_edges_from(edgeList)
    return graph

def simpleAttackerRetreatStrat(battle, roundStat, fullBattleStat):
    if fullBattleStat.attackerWon()>fullBattleStat.defenderWon():
        return False
    if roundStat.valueAdvantage()[0]>0:
        return False
    return True

def simpleDefenderRetreatStrat(battle, roundStat, fullBattleStat):
    if fullBattleStat.defenderWon()>fullBattleStat.attackerWon():
        return False
    if roundStat.valueAdvantage()[0]<0:
        return False
    return True

def calcIntensive(battles):
    with Manager() as manager:
        battleGraph = manager.dict()
        roundStats = manager.dict()
        lock = manager.Lock()
        parallelExec(calcBattleRoundChances, ((battle, battleGraph, roundStats, lock) for battle in battles))
        
        print "calculating full battle chances..."
        fullBattleChances = manager.dict()
        fullBattleStats = manager.dict()
        parallelExec(calcFullBattleChances, ((battle, battleGraph, fullBattleChances, fullBattleStats, lock) for battle in battles))
        
        print "calculating retreat battle chances..."
        retreatBattleChances = manager.dict()
        retreatBattleStats = manager.dict()
        parallelExec(calcRetreatBattleChances, ((battle, battleGraph, retreatBattleChances, retreatBattleStats, lock, 
                roundStats, fullBattleStats, simpleAttackerRetreatStrat, simpleDefenderRetreatStrat) for battle in battles))
        
        print "copying result..."
        battleGraph = dict(battleGraph)
        roundStats = dict(roundStats)
        fullBattleStats = dict(fullBattleStats)
        retreatBattleStats = dict(retreatBattleStats)
    return battleGraph, {"round": roundStats, "full": fullBattleStats, "retreat": retreatBattleStats}

def calcBattleRoundChances(battle, battleGraph, roundStats, lock):
    # prevent unnecessary calculations
    lock.acquire()
    exists = battle in battleGraph
    if not exists and battle.hasEnded():
        battleGraph[battle] = {}
    lock.release()
    if exists or battle.hasEnded(): return
    
    # determine chances for possible outcomes of this battle round
    roundOutcomes = defaultdict(int)
    for _ in xrange(NR_OF_SAMPLES):
        roundOutcomes[battle.simulate()] += 1
    roundChances = {k: v/float(NR_OF_SAMPLES) for k,v in roundOutcomes.iteritems()}
    roundStat = StochasticBattleState.fromDict(roundChances)
    
    lock.acquire()
    if battle not in battleGraph:
        battleGraph[battle] = roundChances
        roundStats[battle] = roundStat
    lock.release()
    
    # also calculate all subsequent possible battles
    for sampleBattle in roundChances:
        # recurse to build up the chance tree
        # Note: max recursive depth equals max infantry
        calcBattleRoundChances(sampleBattle, battleGraph, roundStats, lock)

def calcFullBattleChances(battle, graph, fullBattleChances, fullBattleStats, lock):
    # prevent unnecessary calculations
    if battle.hasEnded(): return Counter({battle: 1})
    lock.acquire()
    exists = battle in fullBattleChances
    if exists: battleChances = fullBattleChances[battle]
    lock.release()
    if exists: return battleChances
    
    # recursively calculate
    battleChances = Counter()
    for nextRound, chance in graph[battle].iteritems():
        nextRoundBattleChances = calcFullBattleChances(nextRound, graph, fullBattleChances, fullBattleStats, lock)
        for b in nextRoundBattleChances:
            nextRoundBattleChances[b] *= chance
        battleChances += nextRoundBattleChances
    battleStat = StochasticBattleState.fromDict(battleChances)
    
    # update fullBattleChances
    lock.acquire()
    if battle not in fullBattleChances:
        fullBattleChances[battle] = battleChances
        fullBattleStats[battle] = battleStat
    lock.release()
    return battleChances

def calcRetreatBattleChances(battle, graph, retreatBattleChances, retreatBattleStats, lock, 
        roundBattleStats, fullBattleStats, attackerRetreatStrat, defenderRetreatStrat, first=True):
    # prevent unnecessary calculations
    # note: 'first' is meant to disallow retreating even before the first battle round
    if battle.hasEnded(): return Counter({battle: 1})
    lock.acquire()
    exists = battle in retreatBattleChances
    if exists and not first:
        battleChances = retreatBattleChances[battle]
    elif not first:
        if attackerRetreatStrat(battle, roundBattleStats[battle], fullBattleStats[battle]):
            battleChances = Counter({battle.attackerRetreats(): 1})
            retreatBattleChances[battle] = battleChances
            exists = True
        elif defenderRetreatStrat(battle, roundBattleStats[battle], fullBattleStats[battle]):
            battleChances = Counter({battle.defenderRetreats(): 1})
            retreatBattleChances[battle] = battleChances
            exists = True
    lock.release()
    if exists: return battleChances
    
    # recursively calculate
    battleChances = Counter()
    for nextRound, chance in graph[battle].iteritems():
        nextRoundBattleChances = calcRetreatBattleChances(nextRound, graph, retreatBattleChances, retreatBattleStats, lock, 
                roundBattleStats, fullBattleStats, attackerRetreatStrat, defenderRetreatStrat, first=False)
        for b in nextRoundBattleChances:
            nextRoundBattleChances[b] *= chance
        battleChances += nextRoundBattleChances
    battleStat = StochasticBattleState.fromDict(battleChances)
    
    # update retreatBattleChances
    lock.acquire()
    if battle not in retreatBattleChances:
        retreatBattleChances[battle] = battleChances
        retreatBattleStats[battle] = battleStat
    lock.release()
    return battleChances

def generateBattles():
    combinations = itertools.product(
        xrange(MAX_INFANTRY+1), 
        xrange(MAX_ARTILLERY+1), 
        xrange(MAX_INFANTRY+1), 
        xrange(MAX_ARTILLERY+1)
    )
    normalBattles = map(lambda args: BattleState.fromUnits(*args), combinations)
    trenchBattles = [b.withTrench() for b in normalBattles]
    return [b for b in normalBattles+trenchBattles if not b.hasEnded()]

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Update a battle chance graph.')
    parser.add_argument('--samples', type=int, default=5000, help='nr of samples per battle case')
    parser.add_argument('--maxinfantry', type=int, default=8, help='max nr of infantry')
    parser.add_argument('--maxartillery', type=int, default=4, help='max nr of artillery')
    
    args = parser.parse_args()
    NR_OF_SAMPLES = args.samples
    MAX_INFANTRY = args.maxinfantry
    MAX_ARTILLERY = args.maxartillery
    
    main()
