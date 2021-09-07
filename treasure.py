from openfile import * 
from array_result import *

def treasure_category(treasure_type):
	if treasure_type == 'A':
		treasure_dict = {
			'Copper': [1, 3, 1000, 25], 
			'Silver': [2, 10, 100, 30], 
			'Gold': [1, 6, 1000, 40], 
			'Platinum or Electrum': [3, 6, 100, 35], 
			'Gems':[1, 4, 10, 60], 
			'Jewelry': [2, 6, 1, 50], 
			'Magic Items or maps': [3, 1, 1, 30, 'any']}
		return(treasure_dict)
	elif treasure_type == 'B':
		treasure_dict = {
			'Copper': [1, 6, 1000, 50], 
			'Silver': [1, 3, 1000, 25], 
			'Gold': [2, 10, 100, 25], 
			'Platinum or Electrum': [1, 10, 100, 25], 
			'Gems':[1, 8, 1, 30], 
			'Jewelry': [1, 4, 1, 20], 
			'Magic Items or maps': [1, 1, 1, 10, 'armor or weapon']}
		return(treasure_dict)
	elif treasure_type == 'C':
		treasure_dict = {
			'Copper': [1, 10, 1000, 20], 
			'Silver': [1, 6, 1000, 30], 
			'Gold': [1, 1, 1, 0], 
			'Platinum or Electrum': [1, 6, 100, 10], 
			'Gems':[1, 6, 1, 25], 
			'Jewelry': [1, 3, 1, 20], 
			'Magic Items or maps': [2, 1, 1, 10, 'any']}
		return(treasure_dict)
	elif treasure_type == 'D':
		treasure_dict = {
			'Copper': [1, 6, 1000, 10], 
			'Silver': [1, 10, 1000, 15], 
			'Gold': [1, 3, 1000, 50], 
			'Platinum or Electrum': [1, 6, 100, 15], 
			'Gems':[1, 10, 1, 30], 
			'Jewelry': [1, 6, 1, 25], 
			'Magic Items or maps': [2, 1, 1, 15, 'any + 1 potion']}
		return(treasure_dict)
	elif treasure_type == 'E':
		treasure_dict = {
			'Copper': [1, 6, 1000, 5], 
			'Silver': [1, 10, 1000, 25], 
			'Gold': [1, 4, 1000, 25], 
			'Platinum or Electrum': [3, 6, 100, 25], 
			'Gems':[1, 12, 1, 15], 
			'Jewelry': [1, 6, 1, 10], 
			'Magic Items or maps': [3, 1, 1, 25, 'any + 1 scroll']}
		return(treasure_dict)
	elif treasure_type == 'F':
		treasure_dict = {
			'Copper': [1, 1, 1, 0], 
			'Silver': [3, 6, 1000, 10], 
			'Gold': [1, 6, 1000, 40], 
			'Platinum or Electrum': [1, 4, 1000, 15], 
			'Gems':[2, 10, 1, 20], 
			'Jewelry': [1, 8, 1, 10], 
			'Magic Items or maps': [5, 1, 1, 30, 'non-weapon']}
		return(treasure_dict)
	elif treasure_type == 'G':
		treasure_dict = {
			'Copper': [1, 1, 1, 0], 
			'Silver': [1, 1, 1, 0], 
			'Gold': [2, 10, 1000, 50], 
			'Platinum or Electrum': [1, 10, 1000, 50], 
			'Gems':[3, 6, 1, 30], 
			'Jewelry': [1, 6, 1, 25], 
			'Magic Items or maps': [5, 1, 1, 35, 'any']}
		return(treasure_dict)
	elif treasure_type == 'H':
		treasure_dict = {
			'Copper': [3, 6, 1000, 25], 
			'Silver': [2, 10, 1000, 40], 
			'Gold': [2, 10, 1000, 55], 
			'Platinum or Electrum': [1, 8, 1000, 40], 
			'Gems':[3, 10, 1, 50], 
			'Jewelry': [2, 10, 1, 50], 
			'Magic Items or maps': [6, 1, 1, 15, 'any']}
		return(treasure_dict)
	elif treasure_type == 'I':
		treasure_dict = {
			'Copper': [1, 1, 1, 0], 
			'Silver': [1, 1, 1, 0], 
			'Gold': [1, 1, 1, 0], 
			'Platinum or Electrum': [1, 6, 100, 30], 
			'Gems':[2, 6, 1, 55], 
			'Jewelry': [2, 4, 1, 50], 
			'Magic Items or maps': [1, 1, 1, 15, 'any']}
		return(treasure_dict)
	elif treasure_type == 'J':
		treasure_dict = {
			'Copper': [3, 8, 1, 100], 
			'Silver': [1, 1, 1, 0], 
			'Gold': [1, 1, 1, 0], 
			'Platinum or Electrum': [1, 1, 1, 0], 
			'Gems': [1, 1, 1, 0],  
			'Jewelry': [1, 1, 1, 0], 
			'Magic Items or maps': [1, 1, 1, 0]}
		return(treasure_dict)
	elif treasure_type == 'K':
		treasure_dict = {
			'Copper': [1, 1, 1, 0], 
			'Silver': [3, 6, 1, 100], 
			'Gold': [1, 1, 1, 0], 
			'Platinum or Electrum': [1, 1, 1, 0], 
			'Gems': [1, 1, 1, 0],  
			'Jewelry': [1, 1, 1, 0], 
			'Magic Items or maps': [1, 1, 1, 0]}
		return(treasure_dict)
	elif treasure_type == 'L':
		treasure_dict = {
			'Copper': [1, 1, 1, 0], 
			'Silver': [1, 1, 1, 0], 
			'Gold': [1, 1, 1, 0], 
			'Platinum or Electrum': [2, 6, 1, 100], 
			'Gems': [1, 1, 1, 0],  
			'Jewelry': [1, 1, 1, 0], 
			'Magic Items or maps': [1, 1, 1, 0]}
		return(treasure_dict)
	elif treasure_type == 'M':
		treasure_dict = {
			'Copper': [1, 1, 1, 0], 
			'Silver': [1, 1, 1, 0], 
			'Gold': [2, 4, 1, 100], 
			'Platinum or Electrum': [1, 1, 1, 0], 
			'Gems': [1, 1, 1, 0],  
			'Jewelry': [1, 1, 1, 0], 
			'Magic Items or maps': [1, 1, 1, 0]}
		return(treasure_dict)
	elif treasure_type == 'N':
		treasure_dict = {
			'Copper': [1, 1, 1, 0], 
			'Silver': [1, 1, 1, 0], 
			'Gold': [1, 1, 1, 0], 
			'Platinum or Electrum': [1, 6, 1, 100], 
			'Gems': [1, 1, 1, 0],  
			'Jewelry': [1, 1, 1, 0], 
			'Magic Items or maps': [1, 1, 1, 0]}
		return(treasure_dict)
	elif treasure_type == 'O':
		treasure_dict = {
			'Copper': [1, 4, 10, 100], 
			'Silver': [1, 3, 10, 100], 
			'Gold': [1, 1, 1, 0], 
			'Platinum or Electrum': [1, 1, 1, 0], 
			'Gems': [1, 1, 1, 0],  
			'Jewelry': [1, 1, 1, 0], 
			'Magic Items or maps': [1, 1, 1, 0]}
		return(treasure_dict)
	elif treasure_type == 'P':
		treasure_dict = {
			'Copper': [1, 1, 1, 0], 
			'Silver': [1, 6, 10, 100], 
			'Gold': [1, 1, 1, 0], 
			'Platinum or Electrum': [1, 20, 1, 100], 
			'Gems': [1, 1, 1, 0],  
			'Jewelry': [1, 1, 1, 0], 
			'Magic Items or maps': [1, 1, 1, 0]}
		return(treasure_dict)
	elif treasure_type == 'Q':
		treasure_dict = {
			'Copper': [1, 1, 1, 0], 
			'Silver': [1, 1, 1, 0], 
			'Gold': [1, 1, 1, 0], 
			'Platinum or Electrum': [1, 1, 1, 0], 
			'Gems': [1, 4, 1, 100],  
			'Jewelry': [1, 1, 1, 0], 
			'Magic Items or maps': [1, 1, 1, 0]}
		return(treasure_dict)
	elif treasure_type == 'R':
		treasure_dict = {
			'Copper': [1, 1, 1, 0], 
			'Silver': [1, 1, 1, 0], 
			'Gold': [2, 10, 1, 100], 
			'Platinum or Electrum': [1, 6, 10, 100], 
			'Gems': [2, 4, 1, 100],  
			'Jewelry': [1, 3, 1, 100], 
			'Magic Items or maps': [1, 1, 1, 0]}
		return(treasure_dict)
	elif treasure_type == 'S':
		treasure_dict = {
			'Copper': [1, 1, 1, 0], 
			'Silver': [1, 1, 1, 0], 
			'Gold': [1, 1, 1, 0], 
			'Platinum or Electrum': [1, 1, 1, 0], 
			'Gems': [1, 1, 1, 0],  
			'Jewelry': [1, 1, 1, 0], 
			'Magic Items or maps': [1, 8, 1, 100, 'potion']}
		return(treasure_dict)
	elif treasure_type == 'T':
		treasure_dict = {
			'Copper': [1, 1, 1, 0], 
			'Silver': [1, 1, 1, 0], 
			'Gold': [1, 1, 1, 0], 
			'Platinum or Electrum': [1, 1, 1, 0], 
			'Gems': [1, 1, 1, 0],  
			'Jewelry': [1, 1, 1, 0], 
			'Magic Items or maps': [1, 4, 1, 100, 'scroll']}
		return(treasure_dict)
	elif treasure_type == 'U':
		treasure_dict = {
			'Copper': [1, 1, 1, 0], 
			'Silver': [1, 1, 1, 0], 
			'Gold': [1, 1, 1, 0], 
			'Platinum or Electrum': [1, 1, 1, 0], 
			'Gems': [2, 8, 1, 90],  
			'Jewelry': [1, 6, 1, 80], 
			'Magic Items or maps': [1, 1, 1, 70, 'any']}
		return(treasure_dict)
	elif treasure_type == 'V':
		treasure_dict = {
			'Copper': [1, 1, 1, 0], 
			'Silver': [1, 1, 1, 0], 
			'Gold': [1, 1, 1, 0], 
			'Platinum or Electrum': [1, 1, 1, 0], 
			'Gems': [1, 1, 1, 0],  
			'Jewelry': [1, 1, 1, 0], 
			'Magic Items or maps': [2, 1, 1, 100, 'any']}
		return(treasure_dict)
	elif treasure_type == 'W':
		treasure_dict = {
			'Copper': [1, 1, 1, 0], 
			'Silver': [1, 1, 1, 0], 
			'Gold': [5, 6, 1, 100], 
			'Platinum or Electrum': [1, 8, 1, 100], 
			'Gems': [2, 8, 1, 60],  
			'Jewelry': [1, 8, 1, 50], 
			'Magic Items or maps': [2, 1, 1, 60, 'any']}
		return(treasure_dict)
	elif treasure_type == 'X':
		treasure_dict = {
			'Copper': [1, 1, 1, 0], 
			'Silver': [1, 1, 1, 0], 
			'Gold': [1, 1, 1, 0], 
			'Platinum or Electrum': [1, 1, 1, 0], 
			'Gems': [1, 1, 1, 0],  
			'Jewelry': [1, 1, 1, 0], 
			'Magic Items or maps': [2, 1, 1, 100, 'potion']}
		return(treasure_dict)
	elif treasure_type == 'Y':
		treasure_dict = {
			'Copper': [1, 1, 1, 0], 
			'Silver': [1, 1, 1, 0], 
			'Gold': [2, 6, 100, 100], 
			'Platinum or Electrum': [1, 1, 1, 0], 
			'Gems': [1, 1, 1, 0],  
			'Jewelry': [1, 1, 1, 0], 
			'Magic Items or maps': [1, 1, 1, 0]}
		return(treasure_dict)
	elif treasure_type == 'Z':
		treasure_dict = {
			'Copper': [1, 3, 100, 100], 
			'Silver': [1, 4, 100, 100], 
			'Gold': [1, 6, 100, 100], 
			'Platinum or Electrum': [1, 4, 100, 100], 
			'Gems': [1, 6, 1, 55],  
			'Jewelry': [2, 6, 1, 50], 
			'Magic Items or maps': [3, 1, 1, 50, 'any']}
		return(treasure_dict)
	else:
		print("[-] Something went wrong")
	
#def generate_hoard(treasure_dict):

	# generate coins

# 	for x in treasure_dict:
# 		# open file and populate array
# 		f_array = openfile(x)
# 		# generate effect
# 		effect = array_result(f_array)
# 		# print(effect)
# 		# check for conditionals in the effect, such as duration or direction
# 		crit_duration = check_duration(effect)
# 		# print(c_effect)
# 		# check for random die rolls in the effect, such as random damage ranges
# 		crit_roll_calc = check_dieroll(crit_duration)
# 		crit_result.append(crit_roll_calc.replace('\n', ''))
# 		# print(calculated)
# 	# check for multiple x2 damage
# 	crit_multiplier = duplicate_dmg(crit_result)
# 	#final_crit_result = check_damage_add(crit_multiplier)
# 	final_crit_result = crit_multiplier

# 	return(final_crit_result)

