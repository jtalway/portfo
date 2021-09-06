import re
from random import randint
from openfile import *
from array_result import *

def check_dieroll(data):

    die_roll = re.findall(r'{(?P<q>.*?)d(?P<die>.*?)}', data)
    # print(match)
    if die_roll:
        q = die_roll[0][0]
        die = die_roll[0][1]
        rNum = randint(1,int(die))* int(q) 
        # print("[+] Dice Quantity: " +  q + ", Die Size: " +  die + ", Random Die Roll Result: " + str(rNum))
        calculated = re.sub(r'{(?P<q>.*?)d(?P<die>.*?)}', str(rNum), data)
        return(calculated)

    else:
        # print("[-] Die roll NOT found")
        return(data)

def check_duration(effect):
    if re.findall(r'<duration>', effect):
        # open file 
        f_array = openfile('duration')
        # find result from array
        result = array_result(f_array)
        # check if die roll necessary
        c_effect = check_dieroll(result).replace('\n', '')
        d_effect = re.sub(r'<duration>', c_effect, effect)
        return(d_effect)

    elif re.findall(r'<duration2>', effect):
        f_array = openfile('duration2')
        result = array_result(f_array)
        c_effect = check_dieroll(result).replace('\n', '')
        d_effect = re.sub(r'<duration2>', c_effect, effect)
        return(d_effect)

    elif re.findall(r'<direction>', effect):
        f_array = openfile('direction')
        result = array_result(f_array)
        c_effect = check_dieroll(result).replace('\n', '')
        d_effect = re.sub(r'<direction>', c_effect, effect)
        return(d_effect)

    else:
        return(effect)

def duplicate_dmg(data):
    count = 0
    checktext = 'x2 weapon damage'
    for effect in data:
        if effect == checktext:
            count = count + 1 
        else:
            continue
    data[:] = [x for x in data if x != checktext]
    if count:
        dmg_mult = count + 1
        mult_dmg_effect = 'x' + str(dmg_mult) + ' weapon damage'
        data.append(mult_dmg_effect)
    return(data)

# def check_damage_add(data):
#     damage_count = 0
#     add_dmg = 0
#     checktext = r'(\+)(?P<q>.*?)damage'
#     print(data)
#     damage = re.findall(checktext, str(data))
#     for i, effect in enumerate(damage):
#         print(damage)
#         if damage:
#             q = damage[0][1]
#             damage_count = damage_count + int(q)
#             print(damage_count)
#             print(data)
#         else:
#             continue
#     data[:] = [x for x in data if x != damage]
#     print(data)
#     if damage_count:
#         add_dmg = '+' + str(damage_count) + ' damage'
#         data.append(add_dmg)
#         print(add_dmg)
#         print(data)
#     return(data)