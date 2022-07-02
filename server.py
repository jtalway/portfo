from flask import Flask, render_template, url_for, request, redirect, abort
import csv
from critical import *
from fumble import *
from abilityscore import *
from dice_roller import *
from treasure_table import *
from treasure import *
from dungeon import *
from npc import *
from calculations import *
from hex import *
from encounter_road import *
import random
import re
from collections import Counter
from jinja2 import TemplateNotFound

app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/index')
@app.route('/index.html')
def index():
	return render_template('generators.html')


@app.route('/character')
def character():
    return render_template('generator-character.html')

@app.route('/combat')
def combat():
    return render_template('generator-combat.html')

@app.route('/adventure')
def adventure():
    return render_template('generator-adventure.html')

@app.route('/treasure')
def treasure():
    return render_template('generator-treasure.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')


# DICE ROLLER
@app.route('/diceroller', methods=['POST', 'GET'])
def diceroller():
    if request.method == 'POST':
        quantity = request.form['quantity']
        dice = request.form['dice']
        mod = request.form['mod']
        mod_value = request.form['mod_value']
        adv = request.form['adv']
        roll_result = check_for_modifier(quantity, dice, mod, mod_value, adv)
        return render_template('diceroller.html', total = roll_result[0], quantity = roll_result[1], dice = roll_result[2], mod = mod, mod_value = mod_value)
    else:
        return render_template('diceroller.html')


# NPC FACTS
@app.route('/npcfacts', methods=['POST', 'GET'])
def npcfacts():
    if request.method == 'POST':
        npc = npc_fact_generation()
        alignment = npc[0]
        age = npc[2]
        possessions = npc[1]
        appearance = npc[3]
        sanity = npc[4]
        tendencies = npc[5]
        personality = npc[6]
        disposition = npc[7]
        intellect = npc[8]
        nature = npc[9]
        materialism = npc[10]
        honesty = npc[11]
        bravery = npc[12]
        morals = npc[13]
        piety = npc[14]
        energy = npc[15]
        thrift = npc[16]
        interests = npc[17]

        return render_template('npcfacts.html', 
            alignment = alignment,
            age = age, 
            possessions = possessions,
            appearance = appearance,
            sanity = sanity,
            tendencies = tendencies,
            personality = personality,
            disposition = disposition,
            intellect = intellect,
            nature = nature,
            materialism = materialism,
            honesty = honesty,
            bravery = bravery,
            morals = morals,
            piety = piety,
            energy = energy,
            thrift = thrift,
            interests = interests)
    else:
        return render_template('npcfacts.html')

# NPC NAME
@app.route('/npcname', methods=['POST', 'GET'])
def npcname():
    if request.method == 'POST':
        name_quantity = request.form['quantity']
        fantasy_names = determine_fantasy_name(name_quantity)
        return render_template('npcname.html', 
            fantasy_names = fantasy_names)
    else:
        return render_template('npcname.html')

# NPC NAME
@app.route('/helpermonkey', methods=['POST', 'GET'])
def helpermonkey():
    if request.method == 'POST':
        action_quantity = request.form['quantity']
        monkey_actions = helper_monkey_action(action_quantity)
        return render_template('helpermonkey.html', 
            monkey_actions = monkey_actions)
    else:
        return render_template('helpermonkey.html')

# CRITICALS
@app.route('/critical', methods=['POST', 'GET'])
def critical():
    if request.method == 'POST':
        weaponDmg = request.form['weaponDmg']
        selected = request.form.getlist('severity')
        severity = selected.count('1')
        total_severity = int(weaponDmg) + severity
        crit_array = severity_gen(total_severity)
        critical_effects = crit_gen(crit_array)
        # check for duplicate results and add/multiply numeric values
        return render_template('critical.html', critical_effects = critical_effects)
    else:
        return render_template('critical.html')

# FUMBLES
@app.route('/fumble', methods=['POST', 'GET'])
def fumble():
    if request.method == 'POST':
        proficient = request.form['proficient']
        # if non-proficient there MUST be a result
        # get list of deductions from fsev criteria on form
        selected = request.form.getlist('fsev')
        # calculate number of reductions
        fseverity = selected.count('1')
        # get number of fumble severity from file by random roll
        fsev_result = fseverity_gen()
        # convert result into a list 
        convert_fsev = int(fsev_result) * ['fumble']
        prelim_fumble_effects = fsev_gen(convert_fsev)
        reduce_fumble_effects = int(proficient) + fseverity
        if reduce_fumble_effects >= len(prelim_fumble_effects):
            fumble_effects = ['no effect']
        elif reduce_fumble_effects < len(prelim_fumble_effects):
            x = len(prelim_fumble_effects) - reduce_fumble_effects
            fumble_effects = prelim_fumble_effects[0:x]
        else:
            return "[-] ERROR > server.py > fumble > reduce_fumble_effects"

        # check for duplicate results and add/multiply numeric values
        return render_template('fumble.html', fumble_effects = fumble_effects)
    else:
        return render_template('fumble.html')

# ABILITY SCORES
@app.route('/abilityscore', methods=['POST', 'GET'])
def abilityscore():
    if request.method == 'POST':
        method = request.form['abilityscoremethod']
        ability_scores = abilityscore_gen(method)
        return render_template('abilityscore.html', ability_scores = ability_scores)
    else:
        return render_template('abilityscore.html')

# TREASURE
@app.route('/treasuretype', methods=['POST', 'GET'])
def treasuretype():
    if request.method == 'POST':
        treasure_type = request.form['treasure']
        treasure_quantity = request.form['quantity']
        # find details on treasure type
        treasure_dict = treasure_category(treasure_type)
        treasure_result = []
        # COINS
        copper_result = calculate_chance(treasure_dict['Copper'], treasure_quantity)
        if copper_result[0] > 0:
            # commas for thousands ("{:,}".format(num))
            coppers = str("{:,}".format(copper_result[0]))
        else:
            coppers = ''
        silver_result = calculate_chance(treasure_dict['Silver'], treasure_quantity)
        if silver_result[0] > 0:
            silvers = str("{:,}".format(silver_result[0]))
        else:
            silvers = ''
        electrum_result = calculate_chance(treasure_dict['Electrum'], treasure_quantity)
        if electrum_result[0] > 0:
            electrums = str("{:,}".format(electrum_result[0]))
        else:
            electrums = ''
        gold_result = calculate_chance(treasure_dict['Gold'], treasure_quantity)
        if gold_result[0] > 0:
            golds = str("{:,}".format(gold_result[0]))
        else:
            golds = ''
        platinum_result = calculate_chance(treasure_dict['Platinum'], treasure_quantity)
        if platinum_result[0] > 0:
            platinums = str("{:,}".format(platinum_result[0]))
        else:
            platinums = ''
        # GEMS
        gem_result = calculate_chance(treasure_dict['Gems'], treasure_quantity)
        gems, gem_value, gem_count = determine_gems(str(gem_result[0]))
        # JEWELRY
        jewelry_result = calculate_chance(treasure_dict['Jewelry'], treasure_quantity)
        jewelry, jewelry_value, jewelry_count = determine_jewelry(str(jewelry_result[0]))
        # MAGIC ITEMS
        magic_item_result, magic_item_type = calculate_chance(treasure_dict['Magic Items or maps'], treasure_quantity)
        magic_items = determine_magic_items(magic_item_result[0], magic_item_type)
        # add comma to each entry except the last
        #formatted_magic_items = [x + ', ' if x != magic_items[-1] else x for x in magic_items]
        # HOARDS
        
        # add comma to each entry except the last
        formatted_gem_hoard = [x + ', ' if x != gems[-1] else x for x in gems]
        formatted_jewelry_hoard = [x + ', ' if x != jewelry[-1] else x for x in jewelry]
        gem_hoard = formatted_gem_hoard
        jewelry_hoard = formatted_jewelry_hoard
        treasure_hoard = magic_items
        # print('[+] ...... NEW TREASURE HOARD GENERATED ......')
        # print(f' CP: {copper_result}, SP: {silver_result}, EP: {electrum_result}, GP: {gold_result}, PP: {platinum_result}')
        # print(f' Gems: {gem_result}, Jewelry: {jewelry_result}, Magic Items: {magic_item_result} lots')
        # print('[-] ...... END TREASURE HOARD ......')
        return render_template('treasuretype.html', 
            treasure_hoard = treasure_hoard, 
            coppers = coppers,
            silvers = silvers,
            electrums = electrums,
            golds = golds,
            platinums = platinums,
            gem_hoard = gem_hoard, 
            jewelry_hoard = jewelry_hoard, 
            jewelry_value = jewelry_value, 
            jewelry_count = jewelry_count, 
            gem_value = gem_value, 
            gem_count = gem_count,
            treasure_type = treasure_type,
            treasure_quantity = treasure_quantity)
    else:
        return render_template('treasuretype.html')

# MAGIC ITEM
@app.route('/magicitem', methods=['POST', 'GET'])
def magicitem():
    if request.method == 'POST':
        magic_item_type = request.form['treasure']
        magic_item_quantity = request.form['quantity']
        magic_items = determine_magic_items(magic_item_quantity, magic_item_type)
        treasure_hoard = magic_items
        if magic_item_type == "rodstaffwand":
            magic_item_type = "Rod, Staff, or Wand"
        elif magic_item_type == "miscX":
            magic_item_type = "Miscellaneous Magic Item"
        elif magic_item_type == "armorshield":
            magic_item_type = "Armor or Shield"
        elif magic_item_type == "weapon":
            magic_item_type = "Miscellaneous Weapon"
        else:
            pass

        return render_template('magicitem.html', 
            treasure_hoard = treasure_hoard,
            magic_item_type = magic_item_type,
            magic_item_quantity = magic_item_quantity)
    else:
        return render_template('magicitem.html')

# GEMS
@app.route('/gem', methods=['POST', 'GET'])
def gem():
    if request.method == 'POST':
        gem_quantity = request.form['quantity']
        gem_list, gem_value, gem_count = determine_gems(gem_quantity)
        treasure_hoard = gem_list
        return render_template('gem.html', 
            treasure_hoard = treasure_hoard, 
            gem_value = gem_value, 
            gem_count = gem_count)
    else:
            return render_template('gem.html')

# JEWELRY
@app.route('/jewelry', methods=['POST', 'GET'])
def jewelry():
    if request.method == 'POST':
        jewelry_quantity = request.form['quantity']
        jewelry_list, jewelry_value, jewelry_count = determine_jewelry(jewelry_quantity)
        treasure_hoard = jewelry_list
        return render_template('jewelry.html', 
            treasure_hoard = treasure_hoard, 
            jewelry_value = jewelry_value, 
            jewelry_count = jewelry_count)
    else:
            return render_template('jewelry.html')

# DUNGEON DRESSING
@app.route('/dungeondressing', methods=['POST', 'GET'])
def dungeondressing():
    if request.method == 'POST':
        sense_feel = openfile('dungeon-feel')
        feel = array_result(sense_feel)
        sense_see = openfile('dungeon-see')
        see = array_result(sense_see)
        sense_smell = openfile('dungeon-smell')
        smell = array_result(sense_smell)
        sense_hear = openfile('dungeon-hear')
        hear = array_result(sense_hear)
        sense_general = openfile('dungeon-general')
        general = array_result(sense_general)
        utensil_personal_array = openfile('dungeon-utensil-personal')
        utensil_personal_item = array_result(utensil_personal_array)

        rNum = randint(1, 2)
        i = 0
        furnishings = []
        final_furnishings = []
        while i < rNum:
            furnishing_array = openfile('dungeon-furnishings')
            furnishing_result = array_result(furnishing_array)
            furnishings.append(furnishing_result)
            i += 1
        # get duplicates
        total_furnishings = Counter(furnishings)
        # sort by highest quantity
        sorted_total_furnishings = dict(sorted(total_furnishings.items(), key=lambda item: item[1], reverse=True))
        for key in sorted_total_furnishings:
            quantity = sorted_total_furnishings[key]
            # attach quantities > 1
            if quantity > 1:
                furnishing_result = key + ' (x ' + str(quantity) + ')'
            else:
                furnishing_result = key
            # add finished furnishings to hoard
            final_furnishings.append(furnishing_result)
        # add comma to each entry except the last
        formatted_furnishings = [x + ', ' if x != final_furnishings[-1] else x for x in final_furnishings]
        
        return render_template('dungeondressing.html', 
            feel = feel, 
            see = see, 
            smell = smell, 
            hear = hear, 
            general = general, 
            formatted_furnishings = formatted_furnishings, 
            utensil_personal_item = utensil_personal_item)
    else:
        return render_template('dungeondressing.html')

# DUNGEON ENCOUNTER
@app.route('/dungeonencounter', methods=['POST', 'GET'])
def dungeonencounter():
    if request.method == 'POST':
        level = request.form['dungeon_level']
        q = request.form['quantity']
        monster_list, dl_num = dungeon_generator_monster_by_level(level, q)
        return render_template('dungeonencounter.html', 
            monster_list = monster_list, 
            dl_num = dl_num,
            q = q)
    else:
        return render_template('dungeonencounter.html')


# HEX ENCOUNTER
@app.route('/hexencounter', methods=['POST', 'GET'])
def hexencounter():
    if request.method == 'POST':
        environment = request.form['environment']
        quantity = request.form['quantity']
        encounter_list, environment = encounter_generation(quantity, environment)
        return render_template('hexencounter.html', 
            encounter_list = encounter_list, 
            quantity = quantity,
            environment = environment)
    else:
        return render_template('hexencounter.html')

# ROAD ENCOUNTER
@app.route('/roadencounter', methods=['POST', 'GET'])
def roadencounter():
    if request.method == 'POST':
        quantity = request.form['quantity']
        encounter_list = road_encounter_generation(quantity)
        return render_template('roadencounter.html', 
            encounter_list = encounter_list, 
            quantity = quantity)
    else:
        return render_template('roadencounter.html')


@app.route('/random_bird', methods=['POST', 'GET'])
def random_bird():
    if request.method == 'POST':
        bird = random_bird_generator()
        return render_template('random-bird.html', 
            bird = bird)
    else:
        return render_template('random-bird.html')
   

@app.route('/random_tree', methods=['POST', 'GET'])
def random_tree():
    if request.method == 'POST':
        tree = random_tree_generator()
        return render_template('random-tree.html', 
            tree = tree)
    else:
        return render_template('random-tree.html')
        
@app.route('/random_herb', methods=['POST', 'GET'])
def random_herb():
    if request.method == 'POST':
        herb = random_herb_generator()
        return render_template('random-herb.html', 
            herb = herb)
    else:
        return render_template('random-herb.html')
  


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return '[-] Did not save to database'
    else:
        return "[-] ERROR > server.py > submit_form > submit contact form"



@app.errorhandler(404)
def not_found():
    """Page not found."""
    return make_response(
        render_template("404.html"),
        404
     )


@app.errorhandler(400)
def bad_request():
    """Bad request."""
    return make_response(
        render_template("400.html"),
        400
    )


@app.errorhandler(500)
def server_error():
    """Internal server error."""
    return make_response(
        render_template("500.html"),
        500
    )

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


if __name__=="__main__":
    app.run(debug=True)