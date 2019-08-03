import Troop
class country:

    def __init__(self, ID,name = ''):
        self.name = name
        self.ID = ID
        self.level = 1
        self.troop_list = {'Ranger': [0,Troop.Rangers()], 'Swordsman': [0, Troop.Swordsman()], 'Priest': [0,Troop.Priest()],
                           'Spearman': [0,Troop.Spearman()], 'CalvaryRaider': [0,Troop.Spearman()], 'BlackSmith': [0,Troop.BlackSmith()],
                           'Ballista': [0,Troop.Ballsita()], 'Dragon': [0, Troop.Dragon()]}
        self.max_troop = 5
        self.num_gold = 400
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

    def get_total_cp(self, temp_troop, countryB):
        my_point = 0
        for key in temp_troop:
            my_point += temp_troop[key][0] * temp_troop[key][1].getPoint(countryB)
        return my_point

    def add_troop(self, num, type):
        for key in self.troop_list:
            if type == key:
                self.troop_list[key][0] += num

    def show_troop(self):
        for key in self.troop_list:
            print( key + ": " + str(self.troop_list[key][0]))

    def add_road(self, another_country):
        self.adjacent_countries.append(another_country)
        another_country.adjcacent_countris.append(another_country)

    def getSoldiersNum(self):
        total = 0
        for key in self.troop_list:
            total += self.troop_list[key][0]
        return total




