"""
import Troop
from Player_country import *

class CrossbowMan(Troop):
    cost = 65
    def __init__(self):
        super().__init__(60,80,65)
        self.name = "CrossbowMan"
    def isMercenary(self):
        return True
class WarElephant(Troop):
    cost = 70
    def __init__(self):
        super().__init__(120,50,70)
        self.name = "WarElephant"

    def isMercenary(self):
        return True
"""
"""
class Merchant():
    currentCountry = random.sample(country.countryList, 1)
    mercenaryList = [CrossbowMan(), WarElephant()]
    inPlayerCountry = False
    def __init__(self):
        pass
    def moveAround(self):
        Merchant.currentCountry = random.sample(Merchant.currentCountry.adjacent_countries(),1)
        if type(Merchant.currentCountry) == Player_country:
            map.alert_popup("", "The merchant is currently in your country", "You can buy " + [i.getName() for i in Merchant.mercenaryList] + " to purchase this.")
            Merchant.inPlayerCountry = True
        else:
            Merchant.inPlayerCountry = False

    this method should be called at the end of each main loop
    
"""
