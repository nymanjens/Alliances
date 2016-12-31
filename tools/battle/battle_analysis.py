from __future__ import division
from pylab import *
from army import Army, StochasticArmy
from battle_state import BattleState, SimpleBattleState, StochasticBattleState
from networkx import DiGraph
from pprint import pprint
from cPickle import load
import cProfile, gzip

PROFILE = False

def main():
    print "loading pkl..."
    graph = loadChanceGraph("battle_graph_full")
    printStats(graph, BattleState.fromUnits(3, 2, 6, 1))

def printStats(graph, battle):
    print "{:<20}{:^20}{:^20}".format("","Attacker", "Defender")
    print "{:}"
    
    
    #res = graph.node[battle]["outcome"]
    #print "Attacker win chance: {:3.0f}%".format(res.attackerWon()*100)
    #print "Defender win chance: {:3.0f}%".format(res.defenderWon()*100)
    #print "Net value gain: {:5.1f} +- {:3.1f}".format(res.valueAdvantage()[0]-battle.valueAdvantage(), res.valueAdvantage()[1])
    #print res

def loadChanceGraph(name):
    with gzip.open(name+".pkl") as fil:
        chanceGraph = load(fil)
    return chanceGraph

if __name__=="__main__":
    if PROFILE:
        cProfile.run("main()")
    else:
        main()
