from util import avg_and_std


class Army(object):
    def __init__(self, infantry, artillery, wounded_infantry=0, wounded_artillery=0):
        assert infantry >= 0
        assert artillery >= 0
        assert wounded_infantry >= 0
        assert wounded_artillery >= 0

        self.infantry = infantry
        self.artillery = artillery
        self.wounded_infantry = wounded_infantry
        self.wounded_artillery = wounded_artillery

    def kill(self, nr_of_units):
        assert nr_of_units >= 0

        # Note: speed beats fanciness here
        infantry, _, still_to_remove = Army._unit_removal(self.infantry, nr_of_units)
        artillery, _, still_to_remove = Army._unit_removal(self.artillery, still_to_remove)
        wounded_infantry, _, still_to_remove = Army._unit_removal(self.wounded_infantry, still_to_remove)
        wounded_artillery, _, _ = Army._unit_removal(self.wounded_artillery, still_to_remove)
        return Army(infantry, artillery, wounded_infantry, wounded_artillery)

    def wound(self, nr_of_units):
        assert nr_of_units >= 0

        # Note: speed beats fanciness here
        infantry, removed_infantry, still_to_remove = Army._unit_removal(self.infantry, nr_of_units)
        artillery, removed_artillery, _ = Army._unit_removal(self.artillery, still_to_remove)
        return Army(infantry, artillery, self.wounded_infantry + removed_infantry,
                    self.wounded_artillery + removed_artillery)

    def remove_wounded(self):
        return Army(self.infantry, self.artillery)

    def can_battle(self):
        return self.healthy_count() > 0

    def unit_count(self):
        return self.healthy_count() + self.wounded_count()

    def healthy_count(self):
        return self.infantry + self.artillery

    def wounded_count(self):
        return self.wounded_infantry + self.wounded_artillery

    def value(self):
        return self.healthy_value() + self.wounded_value()

    def healthy_value(self):
        return self.infantry + 2 * self.artillery

    def wounded_value(self):
        return self.wounded_infantry + 2 * self.wounded_artillery

    @staticmethod
    def _unit_removal(units_to_remove_from, units_to_remove):
        if units_to_remove == 0:
            return units_to_remove_from, 0, 0
        elif units_to_remove_from > units_to_remove:
            return units_to_remove_from - units_to_remove, units_to_remove, 0
        else:
            return 0, units_to_remove_from, units_to_remove - units_to_remove_from

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return self.__dict__ != other.__dict__

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash((self.infantry, self.artillery, self.wounded_infantry, self.wounded_artillery))


class StochasticArmy(object):
    """Only used for analysis"""

    def __init__(self, armies, chances):
        """Note: total sum of chances must equal 1"""
        infantries, artillery, wounded_infantries, wounded_artillery = StochasticArmy._extract(armies)

        self.infantry, self.std_infantry = avg_and_std(infantries, chances)
        self.artillery, self.std_artillery = avg_and_std(artillery, chances)
        self.wounded_infantry, self.std_wounded_infantry = avg_and_std(wounded_infantries, chances)
        self.wounded_artillery, self.std_wounded_artillery = avg_and_std(wounded_artillery, chances)

        self.can_battle_chance = sum(c for a, c in zip(armies, chances) if a.can_battle())

        self.unit_count_avg, self.stdUnitCount = avg_and_std(list(map(lambda a: a.unit_count(), armies)), chances)
        self.healthy_count_avg, self.std_healthy_count = avg_and_std(list(map(lambda a: a.healthy_count(), armies)), chances)
        self.wounded_count_avg, self.std_wounded_count = avg_and_std(list(map(lambda a: a.wounded_count(), armies)), chances)

        self.value_avg, self.std_value = avg_and_std(list(map(lambda a: a.value(), armies)), chances)
        self.healthy_value_avg, self.std_healthy_value = avg_and_std(list(map(lambda a: a.healthy_value(), armies)), chances)
        self.wounded_value_avg, self.std_wounded_value = avg_and_std(list(map(lambda a: a.wounded_value(), armies)), chances)

    def can_battle(self):
        return self.can_battle_chance

    def unit_count(self):
        return self.unit_count_avg, self.stdUnitCount

    def healthy_count(self):
        return self.healthy_count_avg, self.std_healthy_count

    def wounded_count(self):
        return self.wounded_count_avg, self.std_wounded_count

    def value(self):
        return self.value_avg, self.std_value

    def healthy_value(self):
        return self.healthy_value_avg, self.std_healthy_value

    def wounded_value(self):
        return self.wounded_value_avg, self.std_wounded_value

    @staticmethod
    def _extract(armies):
        return zip(*[(a.infantry, a.artillery, a.wounded_infantry, a.wounded_artillery) for a in armies])

    def __str__(self):
        return u"|I| {:4.1f}\u00b1{:4.1f}/{:4.1f}\u00b1{:3.1f} | {:3.1f}\u00b1{:3.1f}/{:3.1f}\u00b1{:3.1f} |A|".format(
            self.infantry,
            self.std_infantry,
            self.wounded_infantry,
            self.std_wounded_infantry,
            self.artillery,
            self.std_artillery,
            self.wounded_artillery,
            self.std_wounded_artillery,
        ).replace(" 0.0", "  . ").replace(u"\u00b10.0", u"\u00b1 . ").replace("/0.0", "/ . ").encode("utf-8")

    def __repr__(self):
        return self.__str__()
