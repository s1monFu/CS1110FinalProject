import random
class strategy:
    def __init__(self):
        self.strategy_dic = {1: "Encirclement – Both a strategy and tactic designed to isolate and surround enemy forces",
                             2: "Flanking maneuver – Involves attacking the opponent from the side, or rear",
                             3: "Human wave attack – the attacker tries to move as many combatants as possible into "
                                "engaging close range combat with the defender",
                             4: "Penetration – A direct attack through enemy lines, then an attack on the rear once through"}

    def strategy_counter(self,user_choice):
        AI_choice = random.randint(1,5)
        if user_choice == 1 and AI_choice == 2:
            print("\n>>>\tYou chose " + self.strategy_dic[1])
            return 50
        if user_choice == 2 and AI_choice == 3:
            return 50
        if user_choice == 3 and AI_choice == 4:
            return 50
        if user_choice == 4 and AI_choice == 1:
            return 50
        return -50

    def show_all_strategies(self):
        for _ in range(1,5):
            print("\n>>>\tChoice " + str(_) + " is: " + self.strategy_dic[_])

