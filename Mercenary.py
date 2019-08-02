from Country import*
import random
from Time import*
class CrossbowMan(Troop):
    def __init__(self):
        super().__init__(60,80,65)
class warElephant(Troop):
        super().__init__(120,50,70)
class Merchant():
    def __init__(self):
        self.currentCountry = random.sample(country.countryList,1)
        self.mercenaryList = [CrossbowMan(),WarElephant()]
        '''
        must assign its value to a variable when using it
        '''
        self.moveAround()
    def moveAround(self):
        if not Time.setTimeDays(2):
            self.currentCountry = random.sample(self.currentCountry.adjacent_countries(),1)
    """
    this method should be called at the end of each main loop
    """