from flask import Flask, render_template, url_for, request, redirect, abort
import csv
from critical import *
from fumble import *
from abilityscore import *
from dice_roller import *
from treasure_table import *
from treasure import *
import random
import re
from collections import Counter
from jinja2 import TemplateNotFound

app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/index')
@app.route('/index.html')
def my_home():
	return render_template('index.html')

@app.route('/critical')
@app.route('/criticals')
@app.route('/criticalhit')
def critical():
    return render_template('critical.html')

@app.route('/fumble')
@app.route('/fumbles')
def fumble():
    return render_template('fumble.html')

@app.route('/treasure')
def treasure():
    return render_template('treasure.html')

@app.route('/dungeon_dressing')
def dungeon_dressing():
    return render_template('dungeon-dressing.html')

@app.route('/die')
@app.route('/dice')
@app.route('/roller')
def roller():
    return render_template('dice.html')

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
        return 'something went wrong, try again!'

# CRITICALS
@app.route('/generate_critical', methods=['POST', 'GET'])
def generate_critical():
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
        return 'something went wrong, try again!'

# FUMBLES
@app.route('/generate_fumble', methods=['POST', 'GET'])
def generate_fumble():
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
            return 'something is amiss'

        # check for duplicate results and add/multiply numeric values
        return render_template('fumble.html', fumble_effects = fumble_effects)
    else:
        return 'something went wrong, try again!'

# ABILITY SCORES
@app.route('/generate_abilityscore', methods=['POST', 'GET'])
def generate_abilityscore():
    if request.method == 'POST':
        method = request.form['abilityscoremethod']
        ability_scores = abilityscore_gen(method)
        return render_template('abilityscore.html', ability_scores = ability_scores)
    else:
        return 'something went wrong, try again!'

# DICE ROLLER
@app.route('/roll_dice', methods=['POST', 'GET'])
def roll_dice():
    if request.method == 'POST':
        quantity = request.form['quantity']
        dice = request.form['dice']
        mod = request.form['mod']
        mod_value = request.form['mod_value']
        adv = request.form['adv']
        roll_result = check_for_modifier(quantity, dice, mod, mod_value, adv)
        return render_template('dice.html', total = roll_result[0], quantity = roll_result[1], dice = roll_result[2], mod = mod, mod_value = mod_value)
    else:
        return 'something went wrong, try again!'

# TREASURE
@app.route('/generate_treasure', methods=['POST', 'GET'])
def generate_treasure():
    if request.method == 'POST':
        treasure_type = request.form['treasure']
        treasure_quantity = request.form['quantity']
        # find details on treasure type
        treasure_dict = treasure_category(treasure_type)
        treasure_result = []
        # COINS
        copper_result = calculate_chance(treasure_dict['Copper'], treasure_quantity)
        coppers = str(copper_result[0]) + ' cp'
        silver_result = calculate_chance(treasure_dict['Silver'], treasure_quantity)
        silvers = str(silver_result[0]) + ' sp'
        electrum_result = calculate_chance(treasure_dict['Electrum'], treasure_quantity)
        electrums = str(electrum_result[0]) + ' ep'
        gold_result = calculate_chance(treasure_dict['Gold'], treasure_quantity)
        golds = str(gold_result[0]) + ' gp'
        platinum_result = calculate_chance(treasure_dict['Platinum'], treasure_quantity)
        platinums = str(platinum_result[0]) + ' pp'
        # GEMS
        gem_result = calculate_chance(treasure_dict['Gems'], treasure_quantity)
        gems = determine_gems(str(gem_result[0]))
        # JEWELRY
        jewelry_result = calculate_chance(treasure_dict['Jewelry'], treasure_quantity)
        jewelry = determine_jewelry(str(jewelry_result[0]))
        # MAGIC ITEMS
        magic_item_result, magic_item_type = calculate_chance(treasure_dict['Magic Items or maps'], treasure_quantity)
        magic_items = determine_magic_items(magic_item_result[0], magic_item_type)
        # HOARDS
        coin_hoard = [coppers, silvers, electrums, golds, platinums]
        gem_hoard = gems
        jewelry_hoard = jewelry
        treasure_hoard = magic_items
        # print('[+] ...... NEW TREASURE HOARD GENERATED ......')
        # print(f' CP: {copper_result}, SP: {silver_result}, EP: {electrum_result}, GP: {gold_result}, PP: {platinum_result}')
        # print(f' Gems: {gem_result}, Jewelry: {jewelry_result}, Magic Items: {magic_item_result} lots')
        # print('[-] ...... END TREASURE HOARD ......')
        return render_template('treasure.html', treasure_hoard = treasure_hoard, coin_hoard = coin_hoard, gem_hoard = gem_hoard, jewelry_hoard = jewelry_hoard)
    else:
        return 'something went wrong, try again!'

@app.route('/generate_dungeon_dressing', methods=['POST', 'GET'])
def generate_dungeon_dressing():
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
            furnishing_result = array_result(furnishing_array).replace('\n', '')
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
        
        return render_template('dungeon-dressing.html', 
            feel = feel, see = see, smell = smell, hear = hear, general = general, formatted_furnishings = formatted_furnishings, utensil_personal_item = utensil_personal_item)
    else:
        return 'something went wrong, try again!'

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

@app.route('/abilityscore')
def abilityscore():
     return generate_abilityscore()

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

if __name__=="__main__":
    app.run(debug=True)