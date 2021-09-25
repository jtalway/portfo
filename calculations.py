import re
from random import randint

def calculate_quantity_with_multiplier(data, multiplier):
	# look for match like 2a6
	range_of_numbers = re.findall(r'{(?P<min_range>.*?)a(?P<max_range>.*?)}', data)
	if range_of_numbers:
		min_range = int(range_of_numbers[0][0])
		minimum_num = min_range
		max_range = int(range_of_numbers[0][1])
		maximum_num = max_range * multiplier
		number_appearing = randint(minimum_num, maximum_num)
		formatted_number = "(x " + str(number_appearing) +")"
		number_generated = re.sub(r'{(?P<q>.*?)a(?P<die>.*?)}', formatted_number, data)
		return(number_generated)
	else:
		return(data)

def calculate_level_difference_dungeon_to_monster(dungeon_level, monster_level):
	# using re.findall()
	# getting numbers from string 
	dl = re.findall(r'\w+-(?P<dl>.*[0-9]+?)', dungeon_level)
	ml = re.findall(r'\w+-(?P<ml>.*[0-9]+?)', monster_level)
	dl_num = int(dl[0])
	ml_num = int(ml[0])
	level_difference = dl_num - ml_num
	return(level_difference, dl_num)

def calculate_quantity_reduction_negative_level_difference(monster, level_difference):
	range_of_numbers = re.findall(r'{(?P<min_range>.*?)a(?P<max_range>.*?)}', monster)
	if range_of_numbers:
		min_range = int(range_of_numbers[0][0])
		max_range = int(range_of_numbers[0][1])
		number_appearing = randint(min_range, max_range)
		temp_num = number_appearing + level_difference
		if temp_num < 1:
			number_appearing = 1
		else:
			number_appearing = temp_num
		formatted_number = "(x " + str(number_appearing) +")"
		number_generated = re.sub(r'{(?P<q>.*?)a(?P<die>.*?)}', formatted_number, monster)
		return(number_generated)
	else:
		return(monster)


# def calculate_value(data):
# 	# look for match like 2d6m10
# 	die_roll = re.findall(r'{(?P<q>.*?)d(?P<die>.*?)m(?P<mult>.*?)}', data)
# 	if die_roll:
# 		n = 0
# 		dice_sum = 0
# 		q = die_roll[0][0]
# 		die = die_roll[0][1]
# 		mult = die_roll[0][2]
# 		# LOOP thru quantity of dice
# 		while n < int(q):
# 			rNum = randint(1,int(die))
# 			dice_sum = dice_sum + rNum 
# 			n += 1
# 		# multiply dice result with multiplier value
# 		calc_die_roll = dice_sum * int(mult)
# 		# replace dice equation with calcuated value
# 		calculated = re.sub(r'{(?P<q>.*?)d(?P<die>.*?)m(?P<mult>.*?)}', str(calc_die_roll), data)
# 		return(calculated)
# 	else:
# 		return(data)