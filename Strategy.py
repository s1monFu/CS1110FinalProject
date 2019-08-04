
def aggressive( my_country):
    my_total = 0
    for key in my_country.troop_list:
        if key == 'Dragon' or 'Swordsman' or 'CalvaryRaider':
            my_total += my_country.troop_list[key][0]
    return my_total

def neutral( my_country):
    my_total = 0
    for key in my_country.troop_list:
        if key == 'Priest' or 'BlackSmith':
            my_total += my_country.troop_list[key][0]
    return my_total

def defensive(my_country):
    my_total = 0
    for key in my_country.troop_list:
        if key == 'Spearman' or 'Ballista' or 'Ranger':
            my_total += my_country.troop_list[key][0]
    return my_total
