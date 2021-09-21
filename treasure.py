# IMPORTS
from random import randint
from openfile import * 
from array_result import *
from collections import Counter
from treasure_table import *

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
            grand_total = grand_total + total
            x+=1
        else:
            x+=1
            continue
    category_result.append(grand_total)
    if magic_item_type == 'na':
    	return(category_result)
    else:
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
		gem = gem_type.replace('\n', '') + ' ' + base_value.replace('\n', '') + 'gp'
		# add gem to the collection
		gem_collection.append(gem)
		x+=1
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
	return(formatted_gem_hoard)

def determine_jewelry(quantity):
	return(quantity)

def determine_magic_items(quantity, magic_item_type):
	formatted_magic_items = []
	magic_items_rolled_list = []
	final_magic_item_hoard = []
	#
	# ADD MAP CHECK IN
	#
	magic_item_collection = find_magic_items(quantity, magic_item_type)
	# generate individual items
	for mi in magic_item_collection:
		magic_item_rolled = roll_magic_items(mi).replace('\n', '')
		magic_items_rolled_list.append(magic_item_rolled)
	#
	# CHECK FOR SPECIALTY ITEMS THAT REQUIRE FURTHER ROLLS/DETERMINATIONS
	#
	# get duplicates
	magic_item_hoard = Counter(magic_items_rolled_list)
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


