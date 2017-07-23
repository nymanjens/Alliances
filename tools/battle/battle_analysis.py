import cProfile
import gzip
import itertools
import os
from pickle import load

import numpy
import pylab
from matplotlib import patheffects
from matplotlib import ticker

from army import Army
from battle_state import BattleState

pylab.ioff()

PROFILE = False
USE_GZIP = False

MAX_VALUE = 8
MAX_INFANTRY = 8
MAX_ARTILLERY = 4


def army_label(army):
    return "I{} A{}".format(army.infantry, army.artillery)


def unit_label(army):
    return "U{}".format(army.unit_count())


VALUE_MAPPINGS = [
    ("battle_rounds", ["full", "retreat"], "number", lambda b, bs: bs.rounds),
    ("win_balance", ["full", "retreat", "round"], "chance diff",
     lambda b, bs: (bs.attacker_won() - bs.defender_won() + 1) / 2),
    ("retreat_attacker", ["retreat"], "chance", lambda b, bs: bs.attacker_retreat()),
    ("retreat_defender", ["retreat"], "chance", lambda b, bs: bs.defender_retreat()),
    ("net_unit_advantage", ["full", "retreat", "round"], "number",
     lambda b, bs: bs.unit_advantage()[0] - b.unit_advantage()),
    ("net_value_advantage", ["full", "retreat", "round"], "number",
     lambda b, bs: bs.value_advantage()[0] - b.value_advantage()),
    ("loss_value_attacker", ["full", "retreat", "round"], "number",
     lambda b, bs: bs.attacking_army.value()[0] - b.attacking_army.value()),
    ("loss_value_defender", ["full", "retreat", "round"], "number",
     lambda b, bs: -bs.defending_army.value()[0] + b.defending_army.value()),
    ("loss_unit_attacker", ["full", "retreat", "round"], "number",
     lambda b, bs: bs.attacking_army.unit_count()[0] - b.attacking_army.unit_count()),
    ("loss_unit_defender", ["full", "retreat", "round"], "number",
     lambda b, bs: -bs.defending_army.unit_count()[0] + b.defending_army.unit_count()),
]


def main():
    graph = load_chance_graph("full")

    for typ in ['normal', 'trench']:
        for name, keys, plot_typ, mapper in VALUE_MAPPINGS:
            for key in keys:
                plot_value(plot_typ, get_mapper(graph, key, mapper),
                           "_tables/{}/{}_{}_{}.png".format(name, name, typ, key),
                           has_trench=typ == "trench")


def load_chance_graph(name):
    print("loading pkl {}...".format(name))
    with (gzip.open("_graph/" + name + ".pkl", "rb") if USE_GZIP else open("_graph/" + name + ".pkl", "rb")) as fil:
        chance_graph = load(fil)
    return chance_graph


def get_mapper(graph, key, value_mapping):
    return lambda battle: value_mapping(battle, graph.node[battle][key]) if battle in graph.node and key in graph.node[
        battle] else pylab.nan


def plot_value(plot_typ, mapper, name, has_trench=False):
    print("plotting", name)
    # TODO find in graph instead of this?
    att_armies = generate_armies_attacker()
    def_armies = generate_armies_defender()
    value_matrix = get_value_matrix(att_armies, def_armies, mapper, has_trench)
    plot_matrix(att_armies, def_armies, value_matrix, name, plot_typ)


def generate_armies_attacker():
    armies = [Army(*args) for args in itertools.product(range(MAX_INFANTRY + 1), range(MAX_ARTILLERY + 1))]
    armies = [a for a in armies if 0 < a.value() <= MAX_VALUE]
    armies.sort(key=lambda x: (x.value(), x.artillery))
    return armies


def generate_armies_defender():
    armies = [Army(infantry, 0) for infantry in range(1, MAX_INFANTRY + 1)]
    return [a for a in armies if a.unit_count() <= MAX_VALUE]


def get_value_matrix(att_armies, def_armies, mapper, has_trench):
    values = pylab.zeros((len(def_armies), len(att_armies)))
    for i, defender in enumerate(def_armies):
        for j, attacker in enumerate(att_armies):
            values[i, j] = mapper(BattleState(attacker, defender, has_trench))
    return values


def plot_matrix(att_armies, def_armies, value_matrix, name, plot_typ):
    fig, ax = pylab.plt.subplots()

    if plot_typ == "chance diff":
        cmap = pylab.cm.coolwarm
        cmap.set_bad(color="black")
        cax = ax.matshow(value_matrix, cmap=cmap, vmin=0, vmax=1, interpolation='nearest', aspect='equal')
        value_txt = [(i, j, 'D' if numpy.abs(z) < 1e-4 else 'A' if numpy.abs(z - 1) < 1e-4 else "{:.0f}".format(
            numpy.round(z * 100))) for
                     (i, j), z in pylab.ndenumerate(value_matrix)]
    elif plot_typ == "chance":
        cmap = pylab.cm.Greens
        cmap.set_bad(color="black")
        cax = ax.matshow(value_matrix, cmap=cmap, vmin=0, vmax=1, interpolation='nearest', aspect='equal')
        value_txt = [(i, j, "{:.0f}".format(numpy.round(z * 100))) for (i, j), z in pylab.ndenumerate(value_matrix)]
    elif plot_typ == "number":
        cmap = pylab.cm.coolwarm
        cmap.set_bad(color="black")
        cax = ax.matshow(value_matrix, cmap=cmap, vmin=-5, vmax=5, interpolation='nearest', aspect='equal')
        value_txt = [(i, j, "{:.1f}".format(z)) for (i, j), z in pylab.ndenumerate(value_matrix)]
    else:
        assert False
    # fig.colorbar(cax)

    ax.set_xticklabels([""] + list(map(army_label, att_armies)), family="monospace", rotation="vertical")
    ax.set_yticklabels([""] + list(map(unit_label, def_armies)), family="monospace")
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.xaxis.set_label_position('top')
    ax.tick_params(axis='both', which='both', length=0)

    ax.set_xlabel("Attacker")
    ax.set_ylabel("Defender")

    for i, j, t in value_txt:
        txt = ax.text(j, i, t, ha='center', va='center', fontsize=5)
        txt.set_path_effects([patheffects.withStroke(linewidth=1, foreground='w')])

    val = 0
    xs = []
    for i, a in enumerate(att_armies):
        if a.value() != val:
            val = a.value()
            pylab.axvline(i - .5, c="k", alpha=.6, linewidth=.6)
            xs.append(i)
    xs.append(len(att_armies))

    val = 0
    ys = []
    for i, a in enumerate(def_armies):
        if a.value() != val:
            val = a.value()
            pylab.axhline(i - .5, c="k", alpha=.6, linewidth=.6)
            ys.append(i)
    ys.append(len(def_armies))

    if 'trench' in name:
        ys = [e / 2 for e in ys]
    pylab.plot(numpy.array(xs) - .5, numpy.array(ys) - .5, alpha=.1, c='k')

    os.makedirs(os.path.dirname(name), exist_ok=True)
    pylab.savefig(name, transparent=True, bbox_inches='tight', dpi=300)
    pylab.close()


if __name__ == "__main__":
    if PROFILE:
        cProfile.run("main()")
    else:
        main()
