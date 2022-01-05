import random
from openfile import * 
from array_result import *


def encounter_generation(quantity, environment):
    q = int(quantity)
    i = 0
    encounter = []
    # local filepath
    # filepath = './static/assets/'
    
    # remote filepath
    filepath = "/home/jtalway/portfo/static/assets/"
    
    while i < q:
        rNum1 = randint(1, 6)
        rNum2 = randint(1, 6)
        rNum3 = randint(1, 6)
        rNum4 = randint(1, 6)
        priNum = rNum1 + rNum2
        secNum = rNum3 + rNum4
        # TEST RESULTS
        # priNum = 7


        number = ""

        if priNum == 2:
            category = "Mishap"
            if secNum == 2:
                res = "Disease"
            elif secNum == 3:
                res = "Minor Injury"
            elif secNum == 4:
                res = "Major Illness"
            elif secNum == 5:
                res = "Minor Illness"
            elif secNum == 6:
                res = "Lost Item"
            elif secNum == 7:
                res = "Equipment Failure"
            elif secNum == 8:
                res = "Lost/Stolen Item"
            elif secNum == 9:
                res = "Minor Infection"
            elif secNum == 10:
                res = "Major Infection"
            elif secNum == 11:
                res = "Major Injury"
            elif secNum == 12:
                res = "Disease"
            else:
                res = "ERROR"

            result = f"[{priNum}, {secNum}] {category} - {res}"
            encounter.append(result)


        elif priNum == 3:
            category = "Hazard"
            # Terrain Event (rockslide, quicksand, avalanche, cave-in, landslide, deadfall)
            # detour, low visibility
            # geyser, lavaflow, lightning storm
            if secNum == 2:
                res = "Earthquake"
            elif secNum == 3:
                res = "Tremor"
            elif secNum == 4:
                res = "Lightning Strike"
            elif secNum == 5:
                res = "Storm"
            elif secNum == 6:
                # Danger
                res = random.choice(list(open(filepath + 'hazard-danger.txt')))
            elif secNum == 7:
                res = "Weather Change"
            elif secNum == 8:
                # Obstacle
                res = random.choice(list(open(filepath + 'hazard-obstacle.txt')))
            elif secNum == 9:
                res = "Fire/Smoke"
            elif secNum == 10:
                res = "Supernatural Weather"
            elif secNum == 11:
                res = "Flash Flood"
            elif secNum == 12:
                res = "Sinkhole"
            else:
                res = "ERROR"

            result = f"[{priNum}, {secNum}] {category} - {res}"
            encounter.append(result)

        elif priNum == 4:
            category = "Roamer (surrounding countryside)"
            number = number_appearing(filepath)
            monster = "monster that travel this area"
            # patrols
            if secNum == 2:
                res = "rare species"
            elif secNum == 3:
                res = "construction for a new Lair"
            elif secNum == 4:
                res = "Ambush"
            elif secNum == 5:
                res = "Ambush"
            elif secNum == 6:
                res = "Spoor"
            elif secNum == 7:
                res = "Encounter"
            elif secNum == 8:
                res = "Spoor"
            elif secNum == 9:
                res = "Spoor"
            elif secNum == 10:
                res = "Champion (+1 AC/attack)"
            elif secNum == 11:
                res = "Champion (+1 AC/attack)"
            elif secNum == 12:
                res = "Alpha (x2 HP, +2 AC/attack)"
            else:
                res = "ERROR"

            if res == "Spoor":
                spoor_res = spoor_result(filepath)

            env = random_environment()
            mc = random_monster_classification()
            monster_wander = random.choice(list(open(filepath + env + mc + '.txt')))

            behavior = unintelligent_behavior(filepath)
            if res == "Encounter":
                result = f"[{priNum}, {secNum}] {number} {monster_wander} [{behavior}]"
            elif res == "Ambush":
                result = f"[{priNum}, {secNum}] ambushed by {number} {monster_wander}"
            elif res == "Spoor":
                result = f"[{priNum}, {secNum}] {spoor_res} of {number} {monster_wander} [{behavior}]"
            elif res == "rare species":
                result = f"[{priNum}, {secNum}] {number} {res} of {monster}"
            else:
                result = f"[{priNum}, {secNum}] {number} {monster_wander} with {res} [{behavior}]"
            encounter.append(result)

        elif priNum == 5:
            category = "Lair Monster"
            number = number_appearing(filepath)
            monster = "*Lair*"
            monster_default = random.choice(list(open(filepath + environment + '.txt'))).rstrip()
            prey = random.choice(list(open(filepath + environment + '-prey.txt'))).rstrip()
            if secNum == 2:
                res = "Special"
            elif secNum == 3:
                res = "Lair"
            elif secNum == 4:
                res = "Ambush"
            elif secNum == 5:
                res = "Chase"
                number2 = number_appearing(filepath)      
            elif secNum == 6:
                res = "Spoor"
            elif secNum == 7:
                res = "Encounter"
            elif secNum == 8:
                res = "Spoor"
            elif secNum == 9:
                res = "Kill"
            elif secNum == 10:
                res = "Champion (+1 AC/attack)"
            elif secNum == 11:
                res = "Lair"
            elif secNum == 12:
                res = "Alpha (x2 HP, +2 AC/attack)"
            else:
                res = "ERROR"

            if res == "Spoor":
                spoor_res = spoor_result(filepath)

            if res == "Special":
                res = random_character_class()

            behavior = unintelligent_behavior(filepath)
            if res == "Encounter":
                result = f"[{priNum}, {secNum}] {number} *{monster_default}* [{behavior}]"
            elif res == "Chase":
                result = f"[{priNum}, {secNum}] {number2} {prey} being chased by {number} *{monster_default}*"
            elif res == "Kill":
                result = f"[{priNum}, {secNum}] a dead {prey} being eaten by {number} *{monster_default}*"
            elif res == "Lair":
                result = f"[{priNum}, {secNum}] Lair of *{monster_default}*"
            elif res == "Ambush":
                result = f"[{priNum}, {secNum}] ambushed by {number} *{monster_default}*"
            elif res == "Spoor":
                result = f"[{priNum}, {secNum}] {spoor_res} of {number} *{monster_default}* [{behavior}]"
            else:
                result = f"[{priNum}, {secNum}] {number} *{monster_default}* with {res} [{behavior}]"
            encounter.append(result)

        elif priNum == 6:
            category = "Predator (environment)"
            number = number_appearing(filepath)
            monster = random.choice(list(open(filepath + environment + '-predator.txt')))
            if secNum == 2:
                res = "rare species"
            elif secNum == 3:
                res = "Lair"
            elif secNum == 4:
                res = "Ambush"
            elif secNum == 5:
                res = "fighting"
                number2 = number_appearing(filepath)
                monster2 = random.choice(list(open(filepath + environment + '-predator.txt')))
            elif secNum == 6:
                res = "Spoor"
            elif secNum == 7:
                res = "Encounter"
            elif secNum == 8:
                res = "Spoor"
            elif secNum == 9:
                res = "Spoor"
            elif secNum == 10:
                res = "Champion (+1 AC/attack)"
            elif secNum == 11:
                res = "Lair"
            elif secNum == 12:
                res = "Alpha (x2 HP, +2 AC/attack)"
            else:
                res = "ERROR"

            if res == "Spoor":
                spoor_res = spoor_result(filepath)
            if res == "Special":
                res = random_character_class()

            behavior = unintelligent_behavior(filepath)
            if res == "Encounter":
                result = f"[{priNum}, {secNum}] {number} {monster} [{behavior}]"
            elif res == "Lair":
                result = f"[{priNum}, {secNum}] Lair of {monster}"
            elif res == "Ambush":
                result = f"[{priNum}, {secNum}] ambushed by {number} {monster}"
            elif res == "Spoor":
                result = f"[{priNum}, {secNum}] {spoor_res} of {number} {monster} [{behavior}]"
            elif res == "rare species":
                result = f"[{priNum}, {secNum}] {number} {res} of {monster}"
            elif res == "fighting":
                result = f"[{priNum}, {secNum}] {number} {monster} {res} {number2} {monster2}"
            else:
                result = f"[{priNum}, {secNum}] {number} {monster} with {res} [{behavior}]"
            encounter.append(result)

        elif priNum == 7:
            category = "Location"
            if secNum == 2:
                # Unusual Constructed
                res = random.choice(list(open(filepath + 'unusual-constructed.txt'))).rstrip()
            elif secNum == 3:
                res = "New Construction"
                constructor = random.choice(list(open(filepath + environment + '-npc.txt'))).rstrip()
                construction_type = random.choice(list(open(filepath + 'construction.txt'))).rstrip()
                number = number_appearing(filepath)
            elif secNum == 4:
                # Military Settlements
                res = random.choice(list(open(filepath + 'settlement-military.txt'))).rstrip()
            elif secNum == 5:
                # Friendly Settlements
                res = random.choice(list(open(filepath + 'settlement-friendly.txt'))).rstrip()
            elif secNum == 6:
                # Natural Resource
                res = "Resource"
                resource_type = random.choice(list(open(filepath + 'resource.txt'))).rstrip()
                visitor = check_if_visitor_resource(filepath, environment)
            elif secNum == 7:
                # Geography
                res = random.choice(list(open(filepath + 'terrain-feature.txt'))).rstrip()
            elif secNum == 8:
                # Trail/Path
                res = random.choice(list(open(filepath + 'trail.txt'))).rstrip()
            elif secNum == 9:
                # Water Features
                res = random.choice(list(open(filepath + 'water.txt'))).rstrip()
            elif secNum == 10:
                # Ruins
                res = "Ruins"
                ruin_type = random.choice(list(open(filepath + 'ruins.txt'))).rstrip()
                inhabitant = check_if_occupied(filepath, environment)
            elif secNum == 11:
                # Caves
                res = "Caves"
                cave_type = random.choice(list(open(filepath + 'caves.txt'))).rstrip()
                inhabitant = check_if_occupied(filepath, environment)
            elif secNum == 12:
                # Unusual Natural
                res = random.choice(list(open(filepath + 'unusual-natural.txt'))).rstrip()
            else:
                res = "ERROR"

            if res == "Caves":
                result = f"[{priNum}, {secNum}] {cave_type} with {inhabitant}"
            elif res == "Ruins":
                result = f"[{priNum}, {secNum}] {ruin_type} with {inhabitant}"
            elif res == "Resource":
                result = f"[{priNum}, {secNum}] {resource_type} with {visitor}"
            elif res == "New Construction":
                result = f"[{priNum}, {secNum}] {number} {constructor} are building {construction_type}"
            else:
                result = f"[{priNum}, {secNum}] {category} - {res}"
            encounter.append(result)

        elif priNum == 8:
            category = "Prey (environment)"
            number = number_appearing(filepath)
            monster = random.choice(list(open(filepath + environment + '-prey.txt'))).rstrip()
            if secNum == 2:
                res = "rare species"
            elif secNum == 3:
                res = "Lair"
            elif secNum == 4:
                res = "Ambush"
            elif secNum == 5:
                res = "Spoor"
            elif secNum == 6:
                res = "Spoor"
            elif secNum == 7:
                res = "Encounter"
            elif secNum == 8:
                res = "Spoor"
            elif secNum == 9:
                res = "Spoor"
            elif secNum == 10:
                res = "Champion (+1 AC/attack)"
            elif secNum == 11:
                res = "Lair"
            elif secNum == 12:
                res = "Alpha (x2 HP, +2 AC/attack)"
            else:
                res = "ERROR"

            if res == "Spoor":
                spoor_res = spoor_result(filepath)

            behavior = unintelligent_behavior(filepath)
            if res == "Encounter":
                result = f"[{priNum}, {secNum}] {number} {monster} [{behavior}]"
            elif res == "Lair":
                result = f"[{priNum}, {secNum}] Lair of {monster}"
            elif res == "Ambush":
                result = f"[{priNum}, {secNum}] ambushed by {number} {monster}"
            elif res == "Spoor":
                result = f"[{priNum}, {secNum}] {spoor_res} of {number} {monster} [{behavior}]"
            elif res == "rare species":
                result = f"[{priNum}, {secNum}] {number} {res} of {monster}"
            else:
                result = f"[{priNum}, {secNum}] {number} {monster} with {res} [{behavior}]"
            encounter.append(result)

        elif priNum == 9:
            category = "Lair Monster"
            number = number_appearing(filepath)
            monster = "*Lair*"
            monster_default = random.choice(list(open(filepath + environment + '.txt'))).rstrip()
            prey = random.choice(list(open(filepath + environment + '-prey.txt'))).rstrip()
            if secNum == 2:
                res = "Special"
            elif secNum == 3:
                res = "Lair"
            elif secNum == 4:
                res = "Ambush"
            elif secNum == 5:
                res = "Chase"
                number2 = number_appearing(filepath)      
            elif secNum == 6:
                res = "Spoor"
            elif secNum == 7:
                res = "Encounter"
            elif secNum == 8:
                res = "Spoor"
            elif secNum == 9:
                res = "Kill"
            elif secNum == 10:
                res = "Champion (+1 AC/attack)"
            elif secNum == 11:
                res = "Lair"
            elif secNum == 12:
                res = "Alpha (x2 HP, +2 AC/attack)"
            else:
                res = "ERROR"

            if res == "Spoor":
                spoor_res = spoor_result(filepath)

            if res == "Special":
                res = random_character_class()

            behavior = intelligent_behavior(filepath)
            if res == "Encounter":
                result = f"[{priNum}, {secNum}] {number} *{monster_default}* [{behavior}]"
            elif res == "Chase":
                result = f"[{priNum}, {secNum}] {number2} {prey} being chased by {number} *{monster_default}*"
            elif res == "Kill":
                result = f"[{priNum}, {secNum}] a dead {prey} being eaten by {number} *{monster_default}*"
            elif res == "Lair":
                result = f"[{priNum}, {secNum}] Lair of *{monster_default}*"
            elif res == "Ambush":
                result = f"[{priNum}, {secNum}] ambushed by {number} *{monster_default}*"
            elif res == "Spoor":
                result = f"[{priNum}, {secNum}] {spoor_res} of {number} *{monster_default}* [{behavior}]"
            else:
                result = f"[{priNum}, {secNum}] {number} *{monster_default}* with {res} [{behavior}]"
            encounter.append(result)

        elif priNum == 10:
            category = "Humanoids"
            number = number_appearing(filepath)
            monster = random.choice(list(open(filepath + environment + '-npc.txt')))
            
            if secNum == 2:
                res = "Special"
            elif secNum == 3:
                res = "Lair"
            elif secNum == 4:
                res = "Ambush"
            elif secNum == 5:
                res = "Spoor"
            elif secNum == 6:
                res = "Spoor"
            elif secNum == 7:
                res = "Encounter"
            elif secNum == 8:
                res = "Spoor"
            elif secNum == 9:
                res = "Spoor"
            elif secNum == 10:
                res = "Champion (+1 AC/attack)"
            elif secNum == 11:
                res = "Lair"
            elif secNum == 12:
                res = "Alpha (x2 HP, +2 AC/attack)"
            else:
                res = "ERROR"

            if res == "Spoor":
                spoor_res = spoor_result(filepath)

            if res == "Special":
                res = random_character_class()

            behavior = intelligent_behavior(filepath)
            if res == "Encounter":
                result = f"[{priNum}, {secNum}] {number} {monster} [{behavior}]"
            elif res == "Lair":
                result = f"[{priNum}, {secNum}] Lair of {monster}"
            elif res == "Ambush":
                result = f"[{priNum}, {secNum}] ambushed by {number} {monster}"
            elif res == "Spoor":
                result = f"[{priNum}, {secNum}] {spoor_res} of {number} {monster} [{behavior}]"
            else:
                result = f"[{priNum}, {secNum}] {number} {monster} with {res} [{behavior}]"
            encounter.append(result)

        elif priNum == 11:
            category = "NPC"
            monster = random.choice(list(open(filepath + 'specificnpc.txt')))
            rNum = randint(1, 12)
            if rNum == 1:
                race = "Human"
            elif rNum == 2:
                race = "Hill Dwarf"
            elif rNum == 3:
                race = "Mountain Dwarf"
            elif rNum == 4:
                race = "Wood Elf"
            elif rNum == 5:
                race = "High Elf"
            elif rNum == 6:
                race = "Half-Elf"
            elif rNum == 7:
                race = "Lightfoot Halfling"
            elif rNum == 8:
                race = "Stout Halfling"
            elif rNum == 9:
                race = "Forest Gnome"
            elif rNum == 10:
                race = "Rock Gnome"
            elif rNum == 11:
                race = "Half-Orc"
            else:
                race = random.choice(list(open(filepath + 'specificrace.txt')))
            
            behavior = intelligent_behavior(filepath)
            result = f"[{priNum}, {secNum}] {race} {monster} [{behavior}]"
            encounter.append(result)

        elif priNum == 12:
            category = "Special"
            # Giant, Fey, Fiend, TARRASQUE
            if secNum == 2:
                res = "Campaign Nemesis"
            elif secNum == 3:
                # Celestial
                category = "Celestial"
                res = random.choice(list(open(filepath + 'monster-celestial.txt')))
            elif secNum == 4:
                # Invasion
                res = random.choice(list(open(filepath + 'invasion.txt')))
            elif secNum == 5:
                res = "Boss B"
            elif secNum == 6:
                # Apex Predator for environment
                category = "Apex Predator"
                res = random.choice(list(open(filepath + environment + '-apex.txt')))
            elif secNum == 7:
                # Dragon
                category = "Dragon"
                res = random.choice(list(open(filepath + environment + '-dragon.txt')))
            elif secNum == 8:
                # Apex Predator Fight
                res = "fighting"
                apex1 = random.choice(list(open(filepath + environment + '-apex.txt')))
                apex2 = random.choice(list(open(filepath + environment + '-apex.txt')))
            elif secNum == 9:
                res = "Boss A"
            elif secNum == 10:
                # Fiend
                category = "Fiend"
                res = random.choice(list(open(filepath + 'monster-fiend.txt')))
            elif secNum == 11:
                res = "WEIRD"
            elif secNum == 12:
                res = "Catastrophic Event/Alien Abduction"
            else:
                res = "ERROR"

            if res == "WEIRD":
                res = random.choice(list(open(filepath + 'special-weird.txt'))).rstrip()

            if res == "fighting":
                result = f"[{priNum}, {secNum}] {apex1} {res} {apex2}"
            else:
                result = f"[{priNum}, {secNum}] {category} - {res}"
            encounter.append(result)

        else:
            category = "ERROR"
            res = "ERROR"
            result = category + " - " +  res
            encounter.append(result)

        i += 1
    environment = environment.capitalize()
    return(encounter, environment)


def intelligent_behavior(filepath):
    smart = random.choice(list(open(filepath + 'behavior-intelligent.txt'))).rstrip()
    return(smart)

def unintelligent_behavior(filepath):
    dumb = random.choice(list(open(filepath + 'behavior-unintelligent.txt'))).rstrip()
    return(dumb)

def number_appearing(filepath):
    number = random.choice(list(open(filepath + 'number-appearing.txt'))).rstrip()
    return(number)

def spoor_result(filepath):
    spoor = random.choice(list(open(filepath + 'spoor.txt'))).rstrip()
    return(spoor)

def check_if_occupied(filepath, environment):
    oNum = randint(1, 20)
    # empty, spoor, inhabited, lair
    if oNum >= 1 and oNum <=10:
        occupant_result = "no occupant"
    elif oNum >=11 and oNum <=15:
        # find spoor
        spoor_res = spoor_result(filepath)
        monster = random.choice(list(open(filepath + environment + '.txt')))
        number = number_appearing(filepath)
        occupant_result = f"{spoor_res} of {number} {monster}"
    elif oNum >=16 and oNum <=19:
        # find inhabitant
        monster = random.choice(list(open(filepath + environment + '.txt')))
        number = number_appearing(filepath)
        occupant_result = f"{number} {monster}"
    else:
        # find lair inhabitant
        monster = random.choice(list(open(filepath + environment + '.txt')))
        occupant_result = f"lair of {monster}"
    return(occupant_result)

def check_if_visitor_resource(filepath, environment):
    vrNum = randint(1, 6)
    if vrNum >=1 and vrNum <=3:
        visitor_result = "no wildlife present"
    elif vrNum == 4:
        visitor_result = "songbirds"
    else:
        number = number_appearing(filepath)
        visitor = random.choice(list(open(filepath + environment + '-prey.txt')))
        visitor_result = f"{number} {visitor}"
    return(visitor_result)

def random_environment():
    eNum = randint(1, 11)
    if eNum == 1:
        env = "arctic"
    elif eNum == 2:
        env = "coastal"
    elif eNum == 3:
        env = "desert"
    elif eNum == 4:
        env = "forest"
    elif eNum == 5:
        env = "grassland"
    elif eNum == 6:
        env = "hill"
    elif eNum == 7:
        env = "mountain"
    elif eNum == 8:
        env = "swamp"
    elif eNum == 9:
        env = "underground"
    # elif eNum == 10:
    #     env = "underwater"
    elif eNum == 10:
        env = "urban"
    else:
        env = "grassland"
    return(env)

def random_monster_classification():
    mNum = randint(1, 6)
    if mNum == 1:
        mc = "-apex"
    elif mNum == 2:
        mc = "-dragon"
    elif mNum == 3:
        mc = "-npc"
    elif mNum == 4:
        mc = "-predator"
    elif mNum == 5:
        mc = "-prey"
    elif mNum == 6:
        mc = ""
    else:
        mc = ""
    return(mc)

def random_character_class():
    cNum = randint(1, 10)
    if cNum == 1:
        character_class = "Barbarian"
    elif cNum == 2:
        character_class = "Bard"
    elif cNum == 3:
        character_class = "Cleric"
    elif cNum == 4:
        character_class = "Druid"
    elif cNum == 5:
        character_class = "Fighter"
    elif cNum == 6:
        character_class = "Monk"
    elif cNum == 7:
        character_class = "Paladin"
    elif cNum == 8:
        character_class = "Ranger"
    elif cNum == 9:
        character_class = "Rogue"
    elif cNum == 10:
        character_class = "Sorcerer"
    elif cNum == 11:
        character_class = "Warlock"
    elif cNum == 12:
        character_class = "Wizard"
    else:
        character_class = "ERROR"
    return(character_class)
