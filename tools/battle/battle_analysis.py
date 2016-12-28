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
    graph = loadChanceGraph("battle_graph_small")
    
    startBattles = [n for n, d in graph.in_degree().iteritems() if d==0]
    endBattles = [n for n, d in graph.out_degree().iteritems() if d==0]
    
    assert len(startBattles)==12
    for battle, attr in graph.node.iteritems():
        assert battle in endBattles and not attr.has_key("outcome") or battle not in endBattles and attr.has_key("outcome")
        if battle not in endBattles:
            assert battle.attackingArmy.value()>=attr["outcome"].attackingArmy.value()[0], "{}\n{}".format(battle, attr)
            assert battle.defendingArmy.value()>=attr["outcome"].defendingArmy.value()[0], "{}\n{}".format(battle, attr)
    assert graph.number_of_selfloops()==0
    
    print "nr of nodes:", graph.number_of_nodes()
    print "nr of edges:", graph.number_of_edges()

def loadChanceGraph(name):
    with gzip.open(name+".pkl") as fil:
        chanceGraph = load(fil)
    return chanceGraph

if __name__=="__main__":
    if PROFILE:
        cProfile.run("main()")
    else:
        main()
