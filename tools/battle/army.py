from util import avgAndStd

class Army(object):
    
    def __init__(self, infantry, artillery, woundedInfantry=0, woundedArtillery=0):
        assert infantry>=0
        assert artillery>=0
        assert woundedInfantry>=0
        assert woundedArtillery>=0
        
        self.infantry = infantry
        self.artillery = artillery
        self.woundedInfantry = woundedInfantry
        self.woundedArtillery = woundedArtillery
    
    ### create new modified army ###
    
    def kill(self, nrOfUnits):
        assert nrOfUnits>=0
        
        # Note: speed beats fancyness here
        infantry, _, stillToRemove = Army._unitRemoval(self.infantry, nrOfUnits)
        artillery, _, stillToRemove = Army._unitRemoval(self.artillery, stillToRemove)
        woundedInfantry, _, stillToRemove = Army._unitRemoval(self.woundedInfantry, stillToRemove)
        woundedArtillery, _, _ = Army._unitRemoval(self.woundedArtillery, stillToRemove)
        return Army(infantry, artillery, woundedInfantry, woundedArtillery)
    
    def wound(self, nrOfUnits):
        assert nrOfUnits>=0
        
        # Note: speed beats fancyness here
        infantry, removedInfantry, stillToRemove = Army._unitRemoval(self.infantry, nrOfUnits)
        artillery, removedArtillery, _ = Army._unitRemoval(self.artillery, stillToRemove)
        return Army(infantry, artillery, self.woundedInfantry + removedInfantry, self.woundedArtillery + removedArtillery)
    
    def removeWounded(self):
        return Army(self.infantry, self.artillery)
    
    ### object information ###
    
    def canBattle(self):
        return self.healthyCount()>0
    
    def unitCount(self):
        return self.healthyCount() + self.woundedCount()
    
    def healthyCount(self):
        return self.infantry + self.artillery
    
    def woundedCount(self):
        return self.woundedInfantry + self.woundedArtillery
    
    def value(self):
        return self.healthyValue() + self.woundedValue()
    
    def healthyValue(self):
        return self.infantry + 2*self.artillery
    
    def woundedValue(self):
        return self.woundedInfantry + 2*self.woundedArtillery
    
    ### utility methods ###
    
    @staticmethod
    def _unitRemoval(unitsToRemoveFrom, unitsToRemove):
        if unitsToRemove==0:
            return unitsToRemoveFrom, 0, 0
        elif unitsToRemoveFrom>unitsToRemove:
            return unitsToRemoveFrom - unitsToRemove, unitsToRemove, 0
        else:
            return 0, unitsToRemoveFrom, unitsToRemove - unitsToRemoveFrom
    
    ### overrides ###
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __ne__(self, other):
        return self.__dict__ != other.__dict__
    
    def __str__(self):
        return str(self.__dict__)
    
    def __repr__(self):
        return self.__str__()
    
    def __hash__(self):
        return hash((self.infantry, self.artillery, self.woundedInfantry, self.woundedArtillery))


class StochasticArmy(object):
    '''Only used for analysis'''
    
    def __init__(self, armies, chances):
        '''Note: total sum of chances must equal 1'''
        infantries, artilleries, woundedInfantries, woundedArtilleries = StochasticArmy._extract(armies)
        
        self.infantry, self.stdInfantry = avgAndStd(infantries, chances)
        self.artillery, self.stdArtillery = avgAndStd(artilleries, chances)
        self.woundedInfantry, self.stdWoundedInfantry = avgAndStd(woundedInfantries, chances)
        self.woundedArtillery, self.stdWoundedArtillery = avgAndStd(woundedArtilleries, chances)
        
        self.canBattleChance = sum(c for a,c in zip(armies, chances) if a.canBattle())
        
        self.unitCountAvg, self.stdUnitCount = avgAndStd(map(lambda a: a.unitCount(), armies), chances)
        self.healthyCountAvg, self.stdHealtyCount = avgAndStd(map(lambda a: a.healthyCount(), armies), chances)
        self.woundedCountAvg, self.stdWoundedCount = avgAndStd(map(lambda a: a.woundedCount(), armies), chances)
        
        self.valueAvg, self.stdValue = avgAndStd(map(lambda a: a.value(), armies), chances)
        self.healthyValueAvg, self.stdHealtyValue = avgAndStd(map(lambda a: a.healthyValue(), armies), chances)
        self.woundedValueAvg, self.stdWoundedValue = avgAndStd(map(lambda a: a.woundedValue(), armies), chances)
    
    ### object information ###
    
    def canBattle(self):
        return self.canBattleChance
    
    def unitCount(self):
        return self.unitCountAvg, self.stdUnitCount
    
    def healthyCount(self):
        return self.healthyCountAvg, self.stdHealtyCount
    
    def woundedCount(self):
        return self.woundedCountAvg, self.stdWoundedCount
    
    def value(self):
        return self.valueAvg, self.stdValue
    
    def healthyValue(self):
        return self.healthyValueAvg, self.stdHealtyValue
    
    def woundedValue(self):
        return self.woundedValueAvg, self.stdWoundedValue
    
    ### utility methods ###
    
    @staticmethod
    def _extract(armies):
        return zip(*[(a.infantry, a.artillery, a.woundedInfantry, a.woundedArtillery) for a in armies])
    
    ### overrides ###
    
    def __str__(self):
        return u"|I| {:4.1f}\u00b1{:4.1f}/{:4.1f}\u00b1{:3.1f} | {:3.1f}\u00b1{:3.1f}/{:3.1f}\u00b1{:3.1f} |A|".format(
            self.infantry,
            self.stdInfantry,
            self.woundedInfantry,
            self.stdWoundedInfantry,
            self.artillery,
            self.stdArtillery,
            self.woundedArtillery,
            self.stdWoundedArtillery,
        ).replace(" 0.0", "  . ").replace(u"\u00b10.0", u"\u00b1 . ").replace("/0.0", "/ . ").encode("utf-8")
    
    def __repr__(self):
        return self.__str__()
