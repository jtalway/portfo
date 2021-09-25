import re
from random import randint
from openfile import * 
from array_result import *
from calculations import *

# DUNGEON MONSTER

# main function - monster generator by dungeon level
def dungeon_generator_monster_by_level(dungeon_level, q):
    q = int(q)
    i = 0
    monster_level = []
    monster_list = []
    while i < q:
        # get monster level based on dungeon level user input
        monster_file = get_monster_level(dungeon_level)
        monster_level.append(monster_file)
        i += 1
    for level in monster_level:
        # get monster type
        monster = get_monster_by_level(level)
        #print("[+] ---------------------------------------------------------------------")
        # check for special encounters (human, character, dragon, demon prince, arch-devil)
        monster = special_encounter(monster)
        # calculate level difference
        level_difference, dl_num = calculate_level_difference_dungeon_to_monster(dungeon_level, level)
        #print(f"calc_dungeon: {dungeon_level}, calc_monster: {level}, calc_level_dif: {level_difference}")
        # adjust encounter numbers based on dungeon level vs monster level
        # > 0 is multiplier to min/max range
        if level_difference > 0:
            number_of_monsters = calculate_quantity_with_multiplier(monster, level_difference + 1)
        # < 0 is reduction in quantity to a minimum of one
        elif level_difference < 0:
            number_of_monsters = calculate_quantity_reduction_negative_level_difference(monster, level_difference)
        # if 0 no adjustment needed
        elif level_difference == 0:
            number_of_monsters = calculate_quantity_with_multiplier(monster, 1)  
        else:
            print('[-] ERROR > dungeon.py > encounter > adjusting monster quantities')
        #print(f'monster: {monster}, number: {number_of_monsters}')
        #print("[-] ---------------------------------------------------------------------")
        monster_list.append(number_of_monsters)
    return(monster_list, dl_num)

# Monster Level
def get_monster_level(dungeon_level):
    array = openfile(dungeon_level)
    result = array_result(array)
    monster_file = "monster-" + result.replace("\n", "")
    return(monster_file)

# Monster Type
def get_monster_by_level(monster_level):
    array = openfile(monster_level)
    result = array_result(array)
    monster = result.replace("\n", "")
    return(monster)

# Special Monster check?
def special_encounter(monster):
    special_file = "monster-" + monster.lower()
    dragons = {"DRAGON-3", "DRAGON-4","DRAGON-5","DRAGON-6","DRAGON-7","DRAGON-8","DRAGON-9","DRAGON-10"}
    if monster == "HUMAN":
        human_num = randint(1,100)
        if human_num >45:
            # replace with character function when done (see next elif statement)
            monster = "group of characters"
        else:
            array = openfile(special_file)
            result = array_result(array)
            monster = result.replace("\n", "")
        return(monster)
    elif monster == "CHARACTER":
        monster = "group of characters"
        return(monster)
    elif monster in dragons:
        array = openfile(special_file)
        result = array_result(array)
        monster = result.replace("\n", "")
        return(monster)
    elif monster == "DEMON-PRINCE":
        array = openfile(special_file)
        result = array_result(array)
        monster = result.replace("\n", "")
        # add demon_retinue
        return(monster)
    elif monster == "DEVIL-ARCH":
        array = openfile(special_file)
        result = array_result(array)
        monster = result.replace("\n", "")
        # add devil_retinue
        return(monster)
    else:
        return(monster)


# # DUNGEON DRESSING
# def generate_dungeon_dressing():
#     if request.method == 'POST':
#         sense_feel = openfile('dungeon-feel')
#         feel = array_result(sense_feel)
#         sense_see = openfile('dungeon-see')
#         see = array_result(sense_see)
#         sense_smell = openfile('dungeon-smell')
#         smell = array_result(sense_smell)
#         sense_hear = openfile('dungeon-hear')
#         hear = array_result(sense_hear)
#         sense_general = openfile('dungeon-general')
#         general = array_result(sense_general)
#         utensil_personal_array = openfile('dungeon-utensil-personal')
#         utensil_personal_item = array_result(utensil_personal_array)

#         rNum = randint(1, 2)
#         i = 0
#         furnishings = []
#         final_furnishings = []
#         while i < rNum:
#             furnishing_array = openfile('dungeon-furnishings')
#             furnishing_result = array_result(furnishing_array).replace('\n', '')
#             furnishings.append(furnishing_result)
#             i += 1
#         # get duplicates
#         total_furnishings = Counter(furnishings)
#         # sort by highest quantity
#         sorted_total_furnishings = dict(sorted(total_furnishings.items(), key=lambda item: item[1], reverse=True))
#         for key in sorted_total_furnishings:
#             quantity = sorted_total_furnishings[key]
#             # attach quantities > 1
#             if quantity > 1:
#                 furnishing_result = key + ' (x ' + str(quantity) + ')'
#             else:
#                 furnishing_result = key
#             # add finished furnishings to hoard
#             final_furnishings.append(furnishing_result)
#         # add comma to each entry except the last
#         formatted_furnishings = [x + ', ' if x != final_furnishings[-1] else x for x in final_furnishings]
        
#         return render_template('dungeon-dressing.html', 
#             feel = feel, see = see, smell = smell, hear = hear, general = general, formatted_furnishings = formatted_furnishings, utensil_personal_item = utensil_personal_item)
#     else:
#         return 'something went wrong, try again!'