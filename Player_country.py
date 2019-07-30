from Country import country
from Strategy import strategy
import Troop
class player_country(country):

    def __init__(self, ID,name):
        super().__init__(ID,name)
        self.my_strategy = strategy()

    def attack_countries(self, other_country):
        """This function is used to attack other countries
            A country wins by having more points than others
            Points come from the number of troops, their health and attack, and your strategy"""
        print("\n>>>\tEncounter enemy!")
        my_point = 0
        enemy_point = 0
        # My point
        ranger = self.troop_list['Rangers']
        my_point += ranger[0] * ranger[1].getPoint()
        swordsman = self.troop_list['Swordsman']
        my_point += swordsman[0] * swordsman[1].getPoint()
        # AI point
        ranger = other_country.troop_list['Rangers']
        enemy_point += ranger[0] * ranger[1].getPoint()
        swordsman = other_country.troop_list['Swordsman']
        enemy_point += swordsman[0] * swordsman[1].getPoint()

        print("\n>>>\tPlease enter your choice")
        choice = int(input())
        my_point += self.choose_strategy(choice)
        print("\n>>>\tMy Point:" + str(my_point))
        print("\n>>>\tEnemy Point:" + str(enemy_point))

        # Compare the points
        if my_point >= enemy_point:
            print("\n>>>\tCongrats! You won the battle")
        elif my_point < enemy_point:
            print("\n>>>\tThe enemy wins!")
    def choose_strategy(self, choice):
        return self.my_strategy.strategy_counter(choice)

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

