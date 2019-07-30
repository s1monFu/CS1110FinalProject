import Troop
class country:

    def __init__(self, ID,name = ''):
        self.name = name
        self.ID = ID
        self.troop_list = {'Rangers': [0,Troop.Rangers()], 'Swordsman': [0, Troop.Swordsman()]}
        self.max_troop = 5
        self.num_gold = 0
        self.gold_per_day = 10
        self.adjacent_countries = []
        # Technology Tree
        self.healthLevel = 1
        self.healthCost = 1
        self.attackLevel = 1
        self.attackCost = 1
        self.goldGainTimes = 1
        self.newCost = 10
        self.expandCost = 10
        self.investCost = 10
        self.times = 1

    def add_troop(self, num, type):
        if type == "Rangers":
            soldier = self.troop_list['Rangers']
            for _ in range(num):
                soldier[0] += 1
        if type == "Swordsman":
            soldier = self.troop_list['Swordsman']
            for _ in range(num):
                soldier[0] += 1

    def show_troop(self):
        troop  = self.troop_list['Rangers']
        print("Rangers: " + str(troop[0]))
        troop  = self.troop_list['Swordsman']
        print("Swordsman: " + str(troop[0]))

    def add_road(self, another_country):
        self.adjacent_countries.append(another_country)
        another_country.adjcacent_countris.append(another_country)




