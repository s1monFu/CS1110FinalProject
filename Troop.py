"""
Troop
"""

class Troops:
    def __init__(self, hEALTH, aTTACK,cost):
        self.health = hEALTH
        self.attack = aTTACK
        self.cost = cost

    def getPoint(self):
        return int(self.health+self.attack)
'''
Rangers
'''
class Rangers(Troops):
    def __init__(self):
        super().__init__(10,15,10)

'''
Swordsman
'''
class Swordsman(Troops):
    def __init__(self):
        super().__init__(30, 10, 15)
"""
Priest
"""
class Priest(Troops):
    def __init__(self):
        super().__init__(40, 5, 30)
    def heal(self):
        print("I can heal")
"""
Spearman
"""
class Spearman(Troops):
    def __init__(self):
        super().__init__(20, 20, 20)
"""
Calvary Raider
"""
class CalvaryRaider(Troops):
    def __init__(self):
        super().__init__(35, 25, 30)
"""
BlackSmith
"""
class BlackSmith(Troops):
    def __init__(self):
        super().__init__(20, 25, 40)
    def add_attack(self):
        print("I can add teammates' attack")
"""
Ballista
"""
class Ballsita(Troops):
    def __init__(self):
        super().__init__(75, 45, 50)
"""
Dragon
"""
class Dragon(Troops):
    def __init__(self):
        super().__init__(85, 70, 70)
