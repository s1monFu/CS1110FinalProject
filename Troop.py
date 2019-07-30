"""
Troop
"""

class Troops:
    def __init__(self, hEALTH, aTTACK):
        self.health = hEALTH
        self.attack = aTTACK

    def getPoint(self):
        return int(self.health+self.attack)
'''
Rangers
'''
class Rangers(Troops):
    def __init__(self):
        super().__init__(10,15)

'''
Swordsman
'''
class Swordsman(Troops):
    def __init__(self):
        super().__init__(20,10)
