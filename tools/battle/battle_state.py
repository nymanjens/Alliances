from numpy.random import randint
from army import Army, StochasticArmy
from util import dotIfZero, avgAndStd

class BattleState(object):
    
    def __init__(self, attackingArmy, defendingArmy):
        self.attackingArmy = attackingArmy
        self.defendingArmy = defendingArmy
    
    @staticmethod
    def fromUnits(attInfantry, attArtillery, defInfantry, defArtillery):
        return BattleState(Army(attInfantry, attArtillery), Army(defInfantry, defArtillery))
    
    ### create new modified battle state ###
    
    def simulate(self):
        return self._simulateArtillery()._simulateInfantry()
    
    def switchSides(self):
        return BattleState(self.defendingArmy, self.attackingArmy)
    
    ### object information ###
    
    def hasEnded(self):
        return not self.attackingArmy.canBattle() or not self.defendingArmy.canBattle()
    
    def attackerWon(self):
        return self.attackingArmy.canBattle() and not self.defendingArmy.canBattle()
    
    def defenderWon(self):
        return not self.attackingArmy.canBattle() and self.defendingArmy.unitCount()>0
    
    def unitAdvantage(self):
        return self.attackingArmy.unitCount() - self.defendingArmy.unitCount()
    
    def valueAdvantage(self):
        return self.attackingArmy.value() - self.defendingArmy.value()
    
    ### utility methods ###
    
    def _simulateArtillery(self):
        return BattleState(self.attackingArmy, self.defendingArmy.kill(self.attackingArmy.artillery))
    
    def _simulateInfantry(self):
        # Note: speed beats fancyness here
        attackKills, attackWounds = 0, 0
        defendKills, defendWounds = 0, 0
        for _ in xrange(self.attackingArmy.infantry):
            throw = randint(1,7)
            if throw in [5, 6]: attackKills += 1
            elif throw in [3, 4]: attackWounds += 1
        for _ in xrange(self.defendingArmy.infantry + self.defendingArmy.artillery):
            throw = randint(1,7)
            if throw>=5: defendKills += 1
            elif throw<=4: defendWounds += 1
        
        attackingArmy = self.attackingArmy.kill(defendKills).wound(defendWounds)
        defendingArmy = self.defendingArmy.kill(attackKills).wound(attackWounds)
        return BattleState(attackingArmy, defendingArmy)
    
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
        return hash((self.attackingArmy, self.defendingArmy))


class SimpleBattleState(object):
    '''Limits number of possible states without affecting battle chances'''
    
    def __init__(self, attackingArmy, defendingArmy):
        simpleAttackingArmy = attackingArmy.removeWounded()
        simpleDefendingArmy = Army(defendingArmy.infantry + defendingArmy.artillery, 0)
        self.battleState = BattleState(simpleAttackingArmy, simpleDefendingArmy)
        
        # to support accessing these directly
        self.attackingArmy = simpleAttackingArmy
        self.defendingArmy = simpleDefendingArmy
    
    @staticmethod
    def fromUnits(attInfantry, attArtillery, defInfantry, defArtillery):
        return SimpleBattleState(Army(attInfantry, attArtillery), Army(defInfantry, defArtillery))
    
    @staticmethod
    def fromBattleState(battleState):
        return SimpleBattleState(battleState.attackingArmy, battleState.defendingArmy)
    
    ### create new modified battle state ###
    
    def simulate(self):
        return SimpleBattleState.fromBattleState(self.battleState.simulate())
    
    ### object information ###
    
    def hasEnded(self):
        return self.battleState.hasEnded()
    
    def attackerWon(self):
        return self.battleState.attackerWon()
    
    def defenderWon(self):
        return self.battleState.defenderWon()
    
    ### overrides ###
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __ne__(self, other):
        return self.__dict__ != other.__dict__
    
    def __str__(self):
        return "|I| {:>2} | {:>1} |A|   >   |U| {:>2}".format(
            dotIfZero(self.battleState.attackingArmy.infantry),
            dotIfZero(self.battleState.attackingArmy.artillery),
            dotIfZero(self.battleState.defendingArmy.infantry),
        )
    
    def __repr__(self):
        return self.__str__()
    
    def __hash__(self):
        return hash(self.battleState)

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
    
    ### overrides ###
    
    def __str__(self):
        return str(self.attackingArmy)+ "   >   " + str(self.defendingArmy)
    
    def __repr__(self):
        return self.__str__()
