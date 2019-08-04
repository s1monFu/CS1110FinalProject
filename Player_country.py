from Country import country
class player_country(country):

    def __init__(self, ID,name):
        super().__init__(ID,name)


    def attack_countries(self, other_country):
        """This function is used to attack other countries
            A country wins by having more points than others
            Points come from the number of troops, their health and attack, and your strategy"""
        print("\n>>>\tEncounter enemy!")
        my_point = self.get_total_cp(self.troop_list, other_country)
        enemy_point = other_country.get_total_cp(other_country.troop_list, self)
        if my_point <= 0:
            return False
        elif enemy_point <= 0:
            return True
        if my_point > enemy_point:
            for key in self.troop_list:
                if self.troop_list[key][0] > 0:
                    if self.troop_list[key][0] >= 2:
                        self.troop_list[key][0] -= 2
                    if self.troop_list[key][1].health > 10:
                        self.troop_list[key][1].health -= 10
                    if self.troop_list[key][1].attack >= 5:
                        self.troop_list[key][1].attack -= 5
            for key in other_country.troop_list:
                if other_country.troop_list[key][0] > 0:
                    if other_country.troop_list[key][0] >= 3:
                        other_country.troop_list[key][0] -= 3
                    if other_country.troop_list[key][1].health > 15:
                        other_country.troop_list[key][1].health -= 15
                    if other_country.troop_list[key][1].attack >=10:
                        other_country.troop_list[key][1].attack -= 10
        if enemy_point >= my_point:
            for key in self.troop_list:
                if self.troop_list[key][0] > 0:
                    if self.troop_list[key][0] >= 3:
                        self.troop_list[key][0] -= 3
                    if self.troop_list[key][1].health > 15:
                        self.troop_list[key][1].health -= 15
                    if self.troop_list[key][1].attack >= 10:
                        self.troop_list[key][1].attack -= 10
            for key in other_country.troop_list:
                if other_country.troop_list[key][0] > 0:
                    if other_country.troop_list[key][0] >= 2:
                        other_country.troop_list[key][0] -= 2
                    if other_country.troop_list[key][1].health > 10:
                        other_country.troop_list[key][1].health -= 10
                    if other_country.troop_list[key][1].attack >= 5:
                        other_country.troop_list[key][1].attack -= 5



    #def after_attack(self):
    #    if self.troop_list['Priest'][0] > 0:


    def technologyTree(self):
        while True:
            print("-------------------------------Actions To Take-------------------------------")
            print("1. Increase health(Current level: " + self.healthLevel() + "( Cost" + self.healthCost + ")")
            print("2. Increase attack(Current level: " + self.attackLevel() + "( Cost" + self.attackCost + ")")
            print("3. Unlock new soldier( Cost" + str(self.newCost) + ")")
            print(
                "4. Increase the maximum number of soldiers( Current number: " + str(self.max_troop) + ")" + "( Cost: " + str(self.expandCost) + ")")
            print(
                "5. Invest" + "(Current times of gold gained: " + str(self.times) + ")" + "( Cost: " + str(self.investCost) + ")")
            print("6. Quit")
            a = input()
            if a == 1:
                self.healthLevel += 1
                for i in self.troop_list:
                    i.health = i.health * 1.5
                if self.num_gold > self.healthCost:
                    self.num_gold = self.num_gold - self.healthCost
                else:
                    print("Not enough gold")
                self.healthCost = self.healthCost * 1.8
            elif a == 2:
                self.attackLevel += 1
                for i in self.troop_list:
                    i.attack = i.attack * 1.3
                if self.num_gold > self.healthCost:
                    self.num_gold = self.num_gold - self.attackCost
                else:
                    print("Not enough gold")
                self.attackCost = int(self.attackCost * 1.5)
            elif a == 3:
                pass
            elif a == 4:
                self.max_troop = int(self.max_troop * 1.5)
                if self.num_gold > self.expandCost:
                    self.num_gold = self.num_gold - self.expandCost
                else:
                    print("Not enough gold")
            elif a == 5:
                self.goldGainTimes = int(self.goldGainTimes * 1.7)
                if self.num_gold > self.investCost:
                    self.num_gold = self.num_gold - self.investCost
                else:
                    print("Not enough gold")
            elif a == 6:
                break

    def get_gold(self):
        self.num_gold += self.gold_per_day * self.goldGainTimes

    def show_gold(self):
        print("\n>>>\tI have " + str(self.num_gold))
"""
test = player_country(0,'kindom')
test.add_troop(10,'Ranger')
test2 = player_country(1,'bla')
test2.add_troop(10,'Swordsman')

test.attack_countries(test2)
"""
