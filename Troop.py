"""
Troop
"""

class Troops:
    def __init__(self, hEALTH, aTTACK,cost):
        self.health = hEALTH
        self.attack = aTTACK
        self.cost = cost

'''
Rangers
'''
class Rangers(Troops):
    def __init__(self):
        super().__init__(10,15,10)

    def getPoint(self, other_country):
        swordsman_num = other_country.troop_list['Swordsman'][0]
        if swordsman_num > 0:
            return int(self.health+self.attack+5)
        else:
            return int(self.health + self.attack)



'''
Swordsman
'''
class Swordsman(Troops):
    def __init__(self):
        super().__init__(30, 10, 15)
    def getPoint(self, other_country):
        Priest_num = other_country.troop_list['Priest'][0]
        Spearman_num = other_country.troop_list['Spearman'][0]
        if Priest_num > 0 or Spearman_num > 0:
            return int(self.health+self.attack+5)
        else:
            return int(self.health + self.attack)
"""
Priest
"""
class Priest(Troops):
    def __init__(self):
        super().__init__(40, 5, 30)
    def heal(self):
        print("I can heal")

    def getPoint(self, other_country):
        return int(self.health + self.attack)

"""
Spearman
"""
class Spearman(Troops):
    def __init__(self):
        super().__init__(20, 20, 20)
    def getPoint(self, other_country):
        Raider_num = other_country.troop_list['CalvaryRaider'][0]
        if Raider_num> 0:
            return int(self.health+self.attack+5)
        else:
            return int(self.health + self.attack)
"""
Calvary Raider
"""
class CalvaryRaider(Troops):
    def __init__(self):
        super().__init__(35, 25, 30)
    def getPoint(self, other_country):
        ranger_num = other_country.troop_list['Ranger'][0]
        Swordsman_num = other_country.troop_list['Swordsman'][0]
        if ranger_num > 0 or Swordsman_num > 0:
            return int(self.health+self.attack+5)
        else:
            return int(self.health + self.attack)
"""
BlackSmith
"""
class BlackSmith(Troops):
    def __init__(self):
        super().__init__(20, 25, 40)
    def add_attack(self):
        print("I can add teammates' attack")
    def getPoint(self, other_country):
        return int(self.health + self.attack)
"""
Ballista
"""
class Ballsita(Troops):
    def __init__(self):
        super().__init__(75, 45, 50)
    def getPoint(self, other_country):
        Dragon_num = other_country.troop_list['Dragon'][0]
        if Dragon_num > 0:
            return int(self.health+self.attack+20)
        else:
            return int(self.health + self.attack)
"""
Dragon
"""
class Dragon(Troops):
    def __init__(self):
        super().__init__(85, 70, 70)
    def getPoint(self, other_country):
        total_num = 0
        for key in other_country.troop_list:
            total_num += other_country.troop_list[key][0]
        if total_num > 10:
            return int(self.health+self.attack+100)
        else:
            return int(self.health + self.attack)
