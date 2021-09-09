from flask import Flask, render_template, url_for, request, redirect
import csv
from critical import *
from fumble import *
from abilityscore import *
from dice_roller import *
from treasure_table import *
import random
import re

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
        roll_result = check_for_modifier(quantity, dice, mod, mod_value)
        return render_template('dice.html', total = roll_result[0], quantity = quantity, dice = dice, mod = mod, mod_value = mod_value)
    else:
        return 'something went wrong, try again!'

# TREASURE
@app.route('/generate_treasure', methods=['POST', 'GET'])
def generate_treasure():
    if request.method == 'POST':
        treasure_type = request.form['treasure']
        treasure_quantity = request.form['quantity']
        treasure_dict = treasure_category(treasure_type)
        #treasure_hoard = generate_hoard(treasure_dict)
        treasure_result = []
        for key in treasure_dict:
            q = treasure_dict[key][0]
            die = treasure_dict[key][1]
            mult = treasure_dict[key][2]
            chance = treasure_dict[key][3]
            magic_item_type = treasure_dict[key][4]
            x = 0
            grand_total = 0
            while x < int(treasure_quantity):
                #print(f'quantity: {q}, die: {die}, multiplier: {mult}, % chance: {chance}')
                rNum = randint(1, 100)
                #print(f'random: {rNum}, chance: {chance}%')
                if rNum <= chance:
                    count = 0
                    i = 0
                    while i < q:
                        dice = randint(1, die)
                        count = count + dice
                        #print(f'die roll: {dice}, count: {count}')
                        i+=1
                    total = mult * count
                    grand_total = grand_total + total
                    x+=1
                else:
                    x+=1
                    continue
            if grand_total > 0:
                coin_result = str(grand_total) + ' ' + key
                treasure_result.append(coin_result)
            else:
                continue

        magic_items = re.findall(r'Magic Items', str(treasure_result))
        print(magic_items)
        if magic_items:
            # q = die_roll[0][0]
            # die = die_roll[0][1]
            print(magic_item_type)
            # print("[+] Dice Quantity: " +  q + ", Die Size: " +  die + ", Random Die Roll Result: " + str(rNum))
            # calculated = re.sub(r'{(?P<q>.*?)d(?P<die>.*?)}', str(rNum), data)
            # return(calculated)
        else:
            print("[-] Magic Items NOT found")

        treasure_hoard = treasure_result
        print(treasure_hoard)
        return render_template('treasure.html', treasure_hoard = treasure_hoard)
    else:
        return 'something went wrong, try again!'

# @app.errorhandler(404)
# def not_found():
#     """Page not found."""
#     return make_response(
#         render_template("404.html"),
#         404
#      )


# @app.errorhandler(400)
# def bad_request():
#     """Bad request."""
#     return make_response(
#         render_template("400.html"),
#         400
#     )


# @app.errorhandler(500)
# def server_error():
#     """Internal server error."""
#     return make_response(
#         render_template("500.html"),
#         500
#     )

@app.route('/abilityscore')
def abilityscore():
     return generate_abilityscore()

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)