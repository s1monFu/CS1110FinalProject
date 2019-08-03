import random
class strategy:
    def __init__(self):
        self.strategy_dic = {1: "Encirclement – Both a strategy and tactic designed to isolate and surround enemy forces",
                             2: "Flanking maneuver – Involves attacking the opponent from the side, or rear",
                             3: "Human wave attack – the attacker tries to move as many combatants as possible into "
                                "engaging close range combat with the defender",
                             4: "Penetration – A direct attack through enemy lines, then an attack on the rear once through"}

    def aggressive(self, my_country):
        my_total = 0
        for key in my_country.troop_list:
            if key == 'Dragon' or 'Swordsman' or 'CalvaryRaider':
                my_total += my_country.troop_list[key][0]
        return my_total

    def neutral(self, my_country):
        my_total = 0
        for key in my_country.troop_list:
            if key == 'Priest' or 'BlackSmith':
                my_total += my_country.troop_list[key][0]
        return my_total

    def defensive(self, my_country):
        my_total = 0
        for key in my_country.troop_list:
            if key == 'Spearman' or 'Ballista' or 'Ranger':
                my_total += my_country.troop_list[key][0]
        return my_total

