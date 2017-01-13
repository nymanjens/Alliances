from __future__ import division
from pylab import *
from army import Army, StochasticArmy
from battle_state import BattleState, StochasticBattleState
from networkx import DiGraph
from pprint import pprint
from cPickle import load
import cProfile, gzip, itertools
from matplotlib import ticker
from matplotlib import patheffects

PROFILE = False
USE_GZIP = False

MAX_VALUE = 8
MAX_INFANTRY = 8
MAX_ARTILLERY = 4


ARMY_LABEL = lambda army: "I{} A{}".format(army.infantry, army.artillery)
UNIT_LABEL = lambda army: "U{}".format(army.unitCount())

VALUE_MAPPINGS = [
    ( "win_balance", ["full", "retreat", "round"], "chance diff", lambda b, bs: (bs.attackerWon()-bs.defenderWon()+1)/2 ),
    ( "retreat_attacker", ["retreat"], "chance", lambda b, bs: bs.attackerRetreat() ),
    ( "retreat_defender", ["retreat"], "chance", lambda b, bs: bs.defenderRetreat() ),
    ( "net_unit_advantage", ["full", "retreat", "round"], "number", lambda b, bs: bs.unitAdvantage()[0]-b.unitAdvantage() ),
    ( "net_value_advantage", ["full", "retreat", "round"], "number", lambda b, bs: bs.valueAdvantage()[0]-b.valueAdvantage() ),
    ( "loss_value_attacker", ["full", "retreat", "round"], "number", lambda b, bs: bs.attackingArmy.value()[0]-b.attackingArmy.value() ),
    ( "loss_value_defender", ["full", "retreat", "round"], "number", lambda b, bs: -bs.defendingArmy.value()[0]+b.defendingArmy.value() ),
    ( "loss_unit_attacker", ["full", "retreat", "round"], "number", lambda b, bs: bs.attackingArmy.unitCount()[0]-b.attackingArmy.unitCount() ),
    ( "loss_unit_defender", ["full", "retreat", "round"], "number", lambda b, bs: -bs.defendingArmy.unitCount()[0]+b.defendingArmy.unitCount() ),
]

def main():
    graph = loadChanceGraph("full")
    
    for typ in ['normal', 'trench']:
        for name, keys, plotTyp, mapper in VALUE_MAPPINGS:
            for key in keys:
                plotValue(plotTyp, getMapper(graph, key, mapper), "_tables/{}_{}_{}.png".format(name, typ, key), hasTrench=typ=="trench")

def loadChanceGraph(name):
    print "loading pkl {}...".format(name)
    with (gzip.open("_graph/"+name+".pkl", "rb") if USE_GZIP else open("_graph/"+name+".pkl", "rb")) as fil:
        chanceGraph = load(fil)
    return chanceGraph

def getMapper(graph, key, valueMapping):
    return lambda battle: valueMapping(battle, graph.node[battle][key]) if battle in graph.node and key in graph.node[battle] else nan

def plotValue(plotTyp, mapper, name, hasTrench=False):
    print "plotting", name
    # TODO find in graph instead of this?
    attArmies = generateArmiesAttacker()
    defArmies = generateArmiesDefender()
    valueMatrix = getValueMatrix(attArmies, defArmies, mapper, hasTrench)
    plotMatrix(attArmies, defArmies, valueMatrix, name, plotTyp)

def generateArmiesAttacker():
    armies = [Army(*args) for args in itertools.product(xrange(MAX_INFANTRY+1), xrange(MAX_ARTILLERY+1))]
    armies = [a for a in armies if 0<a.value()<=MAX_VALUE]
    armies.sort(key=lambda x: (x.value(), x.artillery))
    return armies

def generateArmiesDefender():
    armies = [Army(infantry, 0) for infantry in xrange(1, MAX_INFANTRY+1)]
    return [a for a in armies if a.unitCount()<=MAX_VALUE]

def getValueMatrix(attArmies, defArmies, mapper, hasTrench):
    values = zeros((len(defArmies),len(attArmies)))
    for i,defender in enumerate(defArmies):
        for j,attacker in enumerate(attArmies):
            values[i,j] = mapper(BattleState(attacker, defender, hasTrench))
    return values

def plotMatrix(attArmies, defArmies, valueMatrix, name, plotTyp):
    fig, ax = plt.subplots()
    
    if plotTyp=="chance diff":
        cmap = cm.coolwarm
        cmap.set_bad(color="black")
        cax = ax.matshow(valueMatrix, cmap=cmap, vmin=0, vmax=1, interpolation='nearest', aspect='equal')
        valueTxt = [(i,j, 'D' if abs(z)<1e-4 else 'A' if abs(z-1)<1e-4 else "{:.0f}".format(round(z*100))) for (i,j),z in ndenumerate(valueMatrix)]
    elif plotTyp=="chance":
        cmap = cm.Greens
        cmap.set_bad(color="black")
        cax = ax.matshow(valueMatrix, cmap=cmap, vmin=0, vmax=1, interpolation='nearest', aspect='equal')
        valueTxt = [(i,j, "{:.0f}".format(round(z*100))) for (i,j),z in ndenumerate(valueMatrix)]
    elif plotTyp=="number":
        cmap = cm.coolwarm
        cmap.set_bad(color="black")
        cax = ax.matshow(valueMatrix, cmap=cmap, vmin=-5, vmax=5, interpolation='nearest', aspect='equal')
        valueTxt = [(i,j, "{:.1f}".format(z)) for (i,j),z in ndenumerate(valueMatrix)]
    else:
        assert False
    #fig.colorbar(cax)
    
    ax.set_xticklabels(map(ARMY_LABEL, attArmies), family="monospace", rotation="vertical")
    ax.set_yticklabels(map(UNIT_LABEL, defArmies), family="monospace")
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.xaxis.set_label_position('top') 
    ax.tick_params(axis='both', which='both',length=0)
    
    ax.set_xlabel("Attacker")
    ax.set_ylabel("Defender")
    
    for i,j,t in valueTxt:
        txt = ax.text(j, i, t, ha='center', va='center', fontsize=5)
        txt.set_path_effects([patheffects.withStroke(linewidth=1, foreground='w')])
    
    val = 0
    for i,a in enumerate(attArmies):
        if a.value()!=val:
            val = a.value()
            axvline(i-.5,c="k", alpha=.6, linewidth=.6)
    
    val = 0
    for i,a in enumerate(defArmies):
        if a.value()!=val:
            val = a.value()
            axhline(i-.5,c="k", alpha=.6, linewidth=.6)
    
    savefig(name, transparent=True, bbox_inches='tight', dpi=300)


if __name__=="__main__":
    if PROFILE:
        cProfile.run("main()")
    else:
        main()
