"""
Main
"""
from Country import country
from Player_country import player_country
import Troop
import time
from threading import Thread
import Map
#from Strategy import strategy
"""
Random Attack
"""



"""
Preset
"""

AI_countrya = country(0)
AI_countrya.add_troop(10, 'Rangers')
AI_countryb = country(1)
AI_countryb.add_troop(10, 'Swordsman')

Player = player_country( 2, 'Kindom')
Player.add_troop(10,'Ranger')
Player.add_troop(15,'Swordsman')
Player.show_troop()
print(str(Player.getSoldiersNum()))
"""
Player.attack_countries(AI_country1)
rangerA = Troop.Rangers()
print(str(rangerA.health))
"""
"""
shop = Map.MainShop('Big shop')
main_map = Map.map()

shop.showShop(Player)
shop = Map.MainShop('Big shop')
"""

