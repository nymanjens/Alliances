from numpy.random import randint

from army import Army, StochasticArmy
from util import dot_if_zero, avg_and_std


class BattleState(object):
    def __init__(self, attacking_army, defending_army, has_trench, retreater=None, aftermath=False, winner=None):
        self.attacking_army = attacking_army
        self.defending_army = defending_army
        self.has_trench = has_trench
        assert not retreater
        self.retreater = retreater
        self.aftermath = aftermath
        self.winner = winner

    @staticmethod
    def from_units(att_infantry, att_artillery, def_infantry, def_artillery):
        return BattleState(Army(att_infantry, att_artillery), Army(def_infantry, def_artillery), False)

    def simulate(self):
        assert not self.has_ended(), "can't simulate an ended battle"
        return self._simulate_artillery()._simulate_infantry()

    def attacker_retreats(self):
        assert False

    def defender_retreats(self):
        assert False

    def with_trench(self):
        return BattleState(self.attacking_army, self.defending_army, True, self.retreater, aftermath=self.aftermath)

    def has_ended(self):
        return not self.attacking_army.can_battle() or not self.defending_army.can_battle() or self.aftermath

    def attacker_won(self):
        return self.aftermath and self.winner == 'attacker'

    def defender_won(self):
        return self.aftermath and self.winner == 'defender'

    def unit_advantage(self):
        return self.attacking_army.unit_count() - self.defending_army.unit_count()

    def value_advantage(self):
        return self.attacking_army.value() - self.defending_army.value()

    def _simulate_artillery(self):
        # TODO
        return BattleState(self.attacking_army, self.defending_army.kill(self.attacking_army.artillery),
                           self.has_trench)

    def _simulate_infantry(self):
        # TODO
        # Note: speed beats fanciness here
        attack_kills, attack_wounds = 0, 0
        defend_kills, defend_wounds = 0, 0
        for _ in range(self._attacker_rolls()):
            throw = randint(1, 7)
            if throw in [5, 6]:
                attack_kills += 1
            elif throw in [3, 4] and not self.has_trench:
                attack_wounds += 1
        for _ in range(self._defender_rolls()):
            throw = randint(1, 7)
            if throw in [5, 6]:
                defend_kills += 1
            elif throw in [1, 2, 3, 4]:
                defend_wounds += 1

        attacking_army = self.attacking_army.kill(defend_kills).wound(defend_wounds)
        defending_army = self.defending_army.kill(attack_kills).wound(attack_wounds)

        winner = None
        factor = 1 if self.has_trench else 1
        if attacking_army.healthy_count() + attacking_army.artillery > factor*defending_army.healthy_count():
            winner = 'attacker'
        elif defending_army.unit_count() > 0 and factor*defending_army.healthy_count() >= attacking_army.healthy_count() + attacking_army.artillery:
            winner = 'defender'

        return BattleState(attacking_army, defending_army, self.has_trench, aftermath=True, winner=winner)

    def _attacker_rolls(self):
        # TODO
        return self.attacking_army.infantry

    def _defender_rolls(self):
        # TODO
        rolls = self.defending_army.infantry + self.defending_army.artillery
        return rolls if not self.has_trench else 2 * rolls

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return self.__dict__ != other.__dict__

    def __str__(self):
        return "|I| {:>2}/{:<2} | {:>1}/{:<1} |A|   >   |I| {:>2}/{:<2} | {:>1}/{:<1} |A|".format(
            dot_if_zero(self.attacking_army.infantry),
            dot_if_zero(self.attacking_army.wounded_infantry),
            dot_if_zero(self.attacking_army.artillery),
            dot_if_zero(self.attacking_army.wounded_artillery),
            dot_if_zero(self.defending_army.infantry),
            dot_if_zero(self.defending_army.wounded_infantry),
            dot_if_zero(self.defending_army.artillery),
            dot_if_zero(self.defending_army.wounded_artillery),
        )

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(
            (self.attacking_army, self.defending_army, self.has_trench, self.retreater, self.aftermath, self.winner))


class StochasticBattleState(object):
    """Only used for analysis"""

    def __init__(self, states, chances):
        assert abs(sum(chances) - 1) < 1e-4
        self.attacking_army = StochasticArmy(list(map(lambda s: s.attacking_army, states)), chances)
        self.defending_army = StochasticArmy(list(map(lambda s: s.defending_army, states)), chances)

        self.has_ended_chance = sum(c for s, c in zip(states, chances) if s.has_ended())
        self.attacker_won_chance = sum(c for s, c in zip(states, chances) if s.attacker_won())
        self.defender_won_chance = sum(c for s, c in zip(states, chances) if s.defender_won())

        self.unit_advantage_avg, self.std_unit_advantage = avg_and_std(list(map(lambda s: s.unit_advantage(), states)),
                                                                       chances)
        self.value_advantage_avg, self.std_value_advantage = avg_and_std(
            list(map(lambda s: s.value_advantage(), states)),
            chances)

        self.attacker_retreat_chance = sum(
            c for s, c in zip(states, chances) if hasattr(s, 'retreater') and s.retreater == "attacker")
        self.defender_retreat_chance = sum(
            c for s, c in zip(states, chances) if hasattr(s, 'retreater') and s.retreater == "defender")

        self.rounds = 0  # will be set later

    @staticmethod
    def from_dict(state_chances_dict):
        return StochasticBattleState(state_chances_dict.keys(), list(state_chances_dict.values()))

    def has_ended(self):
        return self.has_ended_chance

    def attacker_won(self):
        return self.attacker_won_chance

    def defender_won(self):
        return self.defender_won_chance

    def unit_advantage(self):
        return self.unit_advantage_avg, self.std_unit_advantage

    def value_advantage(self):
        return self.value_advantage_avg, self.std_value_advantage

    def attacker_retreat(self):
        return self.attacker_retreat_chance

    def defender_retreat(self):
        return self.defender_retreat_chance

    def __str__(self):
        return str(self.attacking_army) + "   >   " + str(self.defending_army)

    def __repr__(self):
        return self.__str__()
