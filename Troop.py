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
    def getName(self):
        return self.name
    def isMercenary(self):
        return
'''
Rangers
'''
class Rangers(Troops):
    def __init__(self):
        super().__init__(10,15,10)
        self.name = "Rangers"

    def isMercenary(self):
        return False
'''
Swordsman
'''
class Swordsman(Troops):
    def __init__(self):
        super().__init__(30, 10, 15)
        self.name = "Swordsman"
    def isMercenary(self):
        return False
"""
Priest
"""
class Priest(Troops):
    def __init__(self):
        super().__init__(40, 5, 30)
        self.name = "Priest"
    def heal(self):
        print("I can heal")

    def isMercenary(self):
        return False
"""
Spearman
"""
class Spearman(Troops):
    def __init__(self):
        super().__init__(20, 20, 20)
        self.name = "Spearman"

    def isMercenary(self):
        return False
"""
Calvary Raider
"""
class CalvaryRaider(Troops):
    def __init__(self):
        super().__init__(35, 25, 30)
        self.name = "CalvaryRiader"

    def isMercenary(self):
        return False
"""
BlackSmith
"""
class BlackSmith(Troops):
    def __init__(self):
        super().__init__(20, 25, 40)
        self.name = "BlackSmith"
    def add_attack(self):
        print("I can add teammates' attack")
    def isMercenary(self):
        return False
"""
Ballista
"""
class Ballsita(Troops):
    def __init__(self):
        super().__init__(75, 45, 50)
        self.name = "Ballista"
    def isMercenary(self):
        return False
"""
Dragon
"""
class Dragon(Troops):
    def __init__(self):
        super().__init__(85, 70, 70)
        self.name = "Dragon"
    def isMercenary(self):
        return False
