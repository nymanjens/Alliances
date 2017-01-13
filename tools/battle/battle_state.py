from numpy.random import randint
from army import Army, StochasticArmy
from util import dotIfZero, avgAndStd

class BattleState(object):
    
    def __init__(self, attackingArmy, defendingArmy, hasTrench, retreater=None):
        assert retreater in [None, 'attacker', 'defender']
        if retreater: assert attackingArmy.canBattle() and defendingArmy.canBattle(), "can't retreat if battle already over"
        
        self.attackingArmy = attackingArmy
        self.defendingArmy = defendingArmy
        self.hasTrench = hasTrench
        self.retreater = retreater
    
    @staticmethod
    def fromUnits(attInfantry, attArtillery, defInfantry, defArtillery):
        return BattleState(Army(attInfantry, attArtillery), Army(defInfantry, defArtillery), False)
    
    @staticmethod
    def fromUnitsWithTrench(attInfantry, attArtillery, defInfantry, defArtillery):
        return BattleState(Army(attInfantry, attArtillery), Army(defInfantry, defArtillery), True)
    
    ### create new modified battle state ###
    
    def simulate(self):
        assert not self.hasEnded(), "can't simulate an ended battle"
        return self._simulateArtillery()._simulateInfantry()
    
    def switchSides(self):
        assert not self.hasEnded(), "only supported for non-ended battles"
        # note: assuming not retreated and no trench for the retreat-attack strategy
        return BattleState(self.defendingArmy, self.attackingArmy, False)
    
    def attackerRetreats(self):
        assert self.retreater==None, "can't retreat, because already retreated"
        return BattleState(self.attackingArmy, self.defendingArmy, self.hasTrench, 'attacker')
    
    def defenderRetreats(self):
        assert self.retreater==None, "can't retreat, because already retreated"
        return BattleState(self.attackingArmy, self.defendingArmy, self.hasTrench, 'defender')
    
    def withTrench(self):
        return BattleState(self.attackingArmy, self.defendingArmy, True, self.retreater)
    
    ### object information ###
    
    def hasEnded(self):
        return self.retreater!=None or not self.attackingArmy.canBattle() or not self.defendingArmy.canBattle()
    
    def attackerWon(self):
        return self.retreater=="defender" or (self.attackingArmy.canBattle() and not self.defendingArmy.canBattle())
    
    def defenderWon(self):
        return self.retreater=="attacker" or (not self.attackingArmy.canBattle() and self.defendingArmy.unitCount()>0)
    
    def unitAdvantage(self):
        return self.attackingArmy.unitCount() - self.defendingArmy.unitCount()
    
    def valueAdvantage(self):
        return self.attackingArmy.value() - self.defendingArmy.value()
    
    ### utility methods ###
    
    def _simulateArtillery(self):
        return BattleState(self.attackingArmy, self.defendingArmy.kill(self.attackingArmy.artillery), self.hasTrench)
    
    def _simulateInfantry(self):
        # Note: speed beats fancyness here
        attackKills, attackWounds = 0, 0
        defendKills, defendWounds = 0, 0
        for _ in xrange(self._attackerRolls()):
            throw = randint(1,7)
            if not self.hasTrench and throw in [5, 6]:
                attackKills += 1
            elif throw not in [1, 2]:
                attackWounds += 1
        for _ in xrange(self._defenderRolls()):
            throw = randint(1,7)
            if throw>=5:
                defendKills += 1
            elif throw<=4:
                defendWounds += 1
        
        attackingArmy = self.attackingArmy.kill(defendKills).wound(defendWounds)
        defendingArmy = self.defendingArmy.kill(attackKills).wound(attackWounds)
        return BattleState(attackingArmy, defendingArmy, self.hasTrench)
    
    def _attackerRolls(self):
        return self.attackingArmy.infantry
    
    def _defenderRolls(self):
        rolls = self.defendingArmy.infantry + self.defendingArmy.artillery
        return rolls if not self.hasTrench else 2*rolls
    
    ### overrides ###
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __ne__(self, other):
        return self.__dict__ != other.__dict__
    
    def __str__(self):
        return "|I| {:>2}/{:<2} | {:>1}/{:<1} |A|   >   |I| {:>2}/{:<2} | {:>1}/{:<1} |A|".format(
            dotIfZero(self.attackingArmy.infantry),
            dotIfZero(self.attackingArmy.woundedInfantry),
            dotIfZero(self.attackingArmy.artillery),
            dotIfZero(self.attackingArmy.woundedArtillery),
            dotIfZero(self.defendingArmy.infantry),
            dotIfZero(self.defendingArmy.woundedInfantry),
            dotIfZero(self.defendingArmy.artillery),
            dotIfZero(self.defendingArmy.woundedArtillery),
        )
    
    def __repr__(self):
        return self.__str__()
    
    def __hash__(self):
        return hash((self.attackingArmy, self.defendingArmy, self.hasTrench, self.retreater))


class StochasticBattleState(object):
    '''Only used for analysis'''
    
    def __init__(self, states, chances):
        assert abs(sum(chances)-1)<1e-4
        self.attackingArmy = StochasticArmy(map(lambda s: s.attackingArmy, states), chances)
        self.defendingArmy = StochasticArmy(map(lambda s: s.defendingArmy, states), chances)
        
        self.hasEndedChance = sum(c for s,c in zip(states, chances) if s.hasEnded())
        self.attackerWonChance = sum(c for s,c in zip(states, chances) if s.attackerWon())
        self.defenderWonChance = sum(c for s,c in zip(states, chances) if s.defenderWon())
        
        self.unitAdvantageAvg, self.stdUnitAdvantage = avgAndStd(map(lambda s: s.unitAdvantage(), states), chances)
        self.valueAdvantageAvg, self.stdValueAdvantage = avgAndStd(map(lambda s: s.valueAdvantage(), states), chances)
        
        self.attackerRetreatChance = sum(c for s,c in zip(states, chances) if hasattr(s, 'retreater') and s.retreater=="attacker")
        self.defenderRetreatChance = sum(c for s,c in zip(states, chances) if hasattr(s, 'retreater') and s.retreater=="defender")
    
    @staticmethod
    def fromDict(stateChancesDict):
        return StochasticBattleState(stateChancesDict.keys(), stateChancesDict.values())
    
    ### object information ###
    
    def hasEnded(self):
        return self.hasEndedChance
    
    def attackerWon(self):
        return self.attackerWonChance
    
    def defenderWon(self):
        return self.defenderWonChance
    
    def unitAdvantage(self):
        return self.unitAdvantageAvg, self.stdUnitAdvantage
    
    def valueAdvantage(self):
        return self.valueAdvantageAvg, self.stdValueAdvantage
    
    def attackerRetreat(self):
        return self.attackerRetreatChance
    
    def defenderRetreat(self):
        return self.defenderRetreatChance
    
    ### overrides ###
    
    def __str__(self):
        return str(self.attackingArmy)+ "   >   " + str(self.defendingArmy)
    
    def __repr__(self):
        return self.__str__()
