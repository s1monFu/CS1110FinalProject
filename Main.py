"""
Main
"""
from Country import country
from Player_country import player_country
import Troop
import time
from threading import Thread
import Map
from Strategy import strategy
"""
Random Attack
"""



"""
Preset
"""
"""
AI_country1 = country(0)
AI_country1.add_troop(10, 'Rangers')
AI_country2 = country(1)
AI_country2.add_troop(10, 'Swordsman')

Player = player_country( 2, 'Kindom')
Player.add_troop(10,'Rangers')
Player.show_troop()

Player.attack_countries(AI_country1)
rangerA = Troop.Rangers()
print(str(rangerA.health))
"""



answer = None

def check():
    time.sleep(2)
    if answer != None:
        return
    print ("Too Slow")

Thread(target = check).start()

answer = input("Input something: ")
hil = Map.Hi("oh")
hil.showShop()



