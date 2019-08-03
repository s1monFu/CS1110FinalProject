from Country import*
import random
from Time import*
from Player_country import Player_country
from Map import *
class CrossbowMan(Troop):
    def __init__(self):
        super().__init__(60,80,65)
        self.name = "CrossbowMan"
    def isMercenary(self):
        return True
class WarElephant(Troop):
    def __init__(self):
        super().__init__(120,50,70)
        self.name = "WarElephant"

    def isMercenary(self):
        return True
class Merchant():
    def __init__(self):
        Merchant.currentCountry = random.sample(country.countryList,1)
        Merchant.mercenaryList = [CrossbowMan(),WarElephant()]
        '''
        must assign its value to a variable when using it
        '''
        Merchant.moveAround()
    def moveAround(self):
        if Time.setTimeDays(2):
            Merchant.currentCountry = random.sample(Merchant.currentCountry.adjacent_countries(),1)
        if type(Merchant.currentCountry) == Player_country:
            map.alert_popup("", "The merchant is currently in your country", "You can buy " + [i.getName() for i in Merchant.mercenaryList] + " to purchase this.")
    """
    this method should be called at the end of each main loop
    """