# IMPORTS
import re
from random import randint
from openfile import * 
from array_result import *
from collections import Counter
from treasure_table import *
from treasure_checks import *

# FUNCTIONS

def calculate_chance(treasure_var, treasure_quantity):
    q = treasure_var[0]
    die = treasure_var[1]
    mult = treasure_var[2]
    chance = treasure_var[3]
    magic_item_type = treasure_var[4]
    x = 0
    grand_total = 0
    category_result = []
    while x < int(treasure_quantity):
        rNum = randint(1, 100)
        if rNum <= chance:
            count = 0
            i = 0
            # sum dice rolls
            while i < q:
                dice = randint(1, die)
                count = count + dice
                i+=1
            # treasure multiplier
            total = mult * count
            # running total
            grand_total = grand_total + total
            x+=1
        else:
            x+=1
            continue
    category_result.append(grand_total)
    # returns
    if magic_item_type == 'na':
    	# non-magical treasure
    	return(category_result)
    else:
    	# magic item generation info
    	return(category_result, magic_item_type)

def determine_gems(gem_quantity):
	x = 0
	gem_collection = []
	final_gem_hoard = []
	formatted_gem_hoard = []
	# loop thru generators for each gem quantity indicated
	while x < int(gem_quantity):
		gem_base_value_array = openfile('gem-base-value')
		# calculate gem base value
		base_value = array_result(gem_base_value_array)
		gem_type_array = openfile('gem' + base_value.replace('\n', ''))
		# find gem type
		gem_type = array_result(gem_type_array)
		# combine gem type and base value
		gem = gem_type.replace('\n', '') + ' ' + base_value.replace('\n', '') + ' gp'
		# add gem to the collection
		gem_collection.append(gem)
		x+=1
	# FIND TOTAL GP VALUE
	# list comprehension 
	gem_total_gp_value = sum([int(word) for item in gem_collection for word in item.split() if word.isnumeric()])
	# GET TOTAL COUNT
	gem_total_count = len(gem_collection)
	# get duplicates
	gem_hoard = Counter(gem_collection)
	# sort by highest quantity
	sorted_gem_hoard = dict(sorted(gem_hoard.items(), key=lambda item: item[1], reverse=True))
	for key in sorted_gem_hoard:
		quantity = sorted_gem_hoard[key]
		# attach quantities > 1
		if quantity > 1:
			gem_result = key + ' (x ' + str(quantity) + ')'
		else:
			gem_result = key
		# add finished gem to hoard
		final_gem_hoard.append(gem_result)
		# add comma to each entry except the last
		formatted_gem_hoard = [x + ', ' if x != final_gem_hoard[-1] else x for x in final_gem_hoard]
	return formatted_gem_hoard, gem_total_gp_value, gem_total_count

def determine_jewelry(jewelry_quantity):
	x = 0
	jewelry_collection = []
	final_jewelry_hoard = []
	formatted_jewelry_hoard = []
	# loop thru generators for each jewelry quantity indicated
	while x < int(jewelry_quantity):
		# read jewelry info file
		jewelry_base_value_array = openfile('jewelry-base-value')
		# get jewelry info
		base_value = array_result(jewelry_base_value_array)
		jewelry = base_value.replace('\n', '')
		# determine material
		jewelry_material = check_material(jewelry)
		# determine jewelry type
		jewelry_type = find_jewelry_type(jewelry_material).replace('\n', '')
		# calculate gp value
		final_jewelry_item = calculate_value(jewelry_type)
		# add jewelry to the collection
		jewelry_collection.append(final_jewelry_item)
		x+=1
	# FIND TOTAL GP VALUE
	# code below does same as the following list comprehension used instead
	# numlist = list()
	# for item in jewelry_collection:
	# 	for word in item.split():
	# 		if word.isnumeric():
	# 			numlist.append(int(word))
	# list comprehension 
	jewelry_total_gp_value = sum([int(word) for item in jewelry_collection for word in item.split() if word.isnumeric()])
	# GET TOTAL COUNT
	jewelry_total_count = len(jewelry_collection)
	# get duplicates
	jewelry_hoard = Counter(jewelry_collection)
	# sort by highest quantity
	sorted_jewelry_hoard = dict(sorted(jewelry_hoard.items(), key=lambda item: item[1], reverse=True))
	for key in sorted_jewelry_hoard:
		quantity = sorted_jewelry_hoard[key]
		# attach quantities > 1
		if quantity > 1:
			jewelry_result = key + ' (x ' + str(quantity) + ')'
		else:
			jewelry_result = key
		# add finished jewelry to hoard
		final_jewelry_hoard.append(jewelry_result)
		# add comma to each entry except the last
		formatted_jewelry_hoard = [x + ', ' if x != final_jewelry_hoard[-1] else x for x in final_jewelry_hoard]
	return formatted_jewelry_hoard, jewelry_total_gp_value, jewelry_total_count

def determine_magic_items(quantity, magic_item_type):
	formatted_magic_items = []
	magic_items_rolled_list = []
	final_magic_item_list = []
	final_magic_item_hoard = []
	magic_item_collection = find_magic_items(quantity, magic_item_type)
	# generate individual items
	for mi in magic_item_collection:
		magic_item_rolled = roll_magic_items(mi)
		magic_items_rolled_list.append(magic_item_rolled.replace('\n', ''))
	#
	# CHECK FOR SPECIALTY ITEMS THAT REQUIRE FURTHER ROLLS/DETERMINATIONS
	for magic_item in magic_items_rolled_list:
		updated_magic_item = check_special_item(magic_item)
		final_magic_item_list.append(updated_magic_item.replace('\n', ''))		

	# get duplicates
	magic_item_hoard = Counter(final_magic_item_list)
	# sort by highest quantity
	sorted_magic_item_hoard = dict(sorted(magic_item_hoard.items(), key=lambda item: item[1], reverse=True))
	for key in sorted_magic_item_hoard:
		quantity = sorted_magic_item_hoard[key]
		#
		# CHECK FOR RANDOM QUANTITIES TO BE ROLLED, ITERATE FOR QUANTITY AND RETURN AS TOTAL QUANTITY
		#
		# attach quantities > 1
		if quantity > 1:
			magic_item_result = key + ' (x ' + str(quantity) + ')'
		else:
			magic_item_result = key
		# add finished item to hoard
		final_magic_item_hoard.append(magic_item_result)
		# add comma to each entry except the last
		formatted_magic_items = [x + ', ' if x != final_magic_item_hoard[-1] else x for x in final_magic_item_hoard]
	return(formatted_magic_items)


def calculate_value(data):
	# look for match like 2d6m10
	die_roll = re.findall(r'{(?P<q>.*?)d(?P<die>.*?)m(?P<mult>.*?)}', data)
	if die_roll:
		n = 0
		dice_sum = 0
		q = die_roll[0][0]
		die = die_roll[0][1]
		mult = die_roll[0][2]
		# LOOP thru quantity of dice
		while n < int(q):
			rNum = randint(1,int(die))
			dice_sum = dice_sum + rNum 
			n += 1
		# multiply dice result with multiplier value
		calc_die_roll = dice_sum * int(mult)
		# replace dice equation with calcuated value
		calculated = re.sub(r'{(?P<q>.*?)d(?P<die>.*?)m(?P<mult>.*?)}', str(calc_die_roll), data)
		return(calculated)
	else:
		return(data)

def check_material(data):
	# find material tag
    if re.findall(r'<material1>', data):
        # open file 
        f_array = openfile('material1')
        # find result from array
        result = array_result(f_array)
        # replace material with material type
        material_type = re.sub(r'<material1>', result, data)
        return(material_type)

    elif re.findall(r'<material2>', data):
        f_array = openfile('material2')
        result = array_result(f_array)
        material_type = re.sub(r'<material2>', result, data)
        return(material_type)

    else:
        return(data)

def find_jewelry_type(data):
	# find jewelry tag
    if re.findall(r'<jewelry>', data):
        # open file 
        f_array = openfile('jewelry-type')
        # find result from array
        result = array_result(f_array)
        # replace jewelry with jewelry type
        jewelry_type = re.sub(r'<jewelry>', result, data)
        return(jewelry_type)
    else:
        return(data)	