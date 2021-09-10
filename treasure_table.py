from openfile import * 
from array_result import *

def treasure_category(treasure_type):
	# dict = category : [quantity/number of dice, size of dice, multiplier, %chance, magic item category]
	if treasure_type == 'A':
		treasure_dict = {
			'Copper': [1, 3, 1000, 25, 'na'], 
			'Silver': [2, 10, 100, 30, 'na'], 
			'Gold': [1, 6, 1000, 40, 'na'], 
			'Platinum or Electrum': [3, 6, 100, 35, 'na'], 
			'Gems': [1, 4, 10, 60, 'na'], 
			'Jewelry': [2, 6, 1, 50, 'na'], 
			'Magic Items or maps': [3, 1, 1, 30, 'any']}
		return(treasure_dict)
	elif treasure_type == 'B':
		treasure_dict = {
			'Copper': [1, 6, 1000, 50, 'na'], 
			'Silver': [1, 3, 1000, 25, 'na'], 
			'Gold': [2, 10, 100, 25, 'na'], 
			'Platinum or Electrum': [1, 10, 100, 25, 'na'], 
			'Gems':[1, 8, 1, 30, 'na'], 
			'Jewelry': [1, 4, 1, 20, 'na'], 
			'Magic Items or maps': [1, 1, 1, 10, 'armor or weapon']}
		return(treasure_dict)
	elif treasure_type == 'C':
		treasure_dict = {
			'Copper': [1, 10, 1000, 20, 'na'], 
			'Silver': [1, 6, 1000, 30, 'na'], 
			'Gold': [1, 1, 1, 0, 'na'], 
			'Platinum or Electrum': [1, 6, 100, 10, 'na'], 
			'Gems':[1, 6, 1, 25, 'na'], 
			'Jewelry': [1, 3, 1, 20, 'na'], 
			'Magic Items or maps': [2, 1, 1, 10, 'any']}
		return(treasure_dict)
	elif treasure_type == 'D':
		treasure_dict = {
			'Copper': [1, 6, 1000, 10, 'na'], 
			'Silver': [1, 10, 1000, 15, 'na'], 
			'Gold': [1, 3, 1000, 50, 'na'], 
			'Platinum or Electrum': [1, 6, 100, 15, 'na'], 
			'Gems':[1, 10, 1, 30, 'na'], 
			'Jewelry': [1, 6, 1, 25, 'na'], 
			'Magic Items or maps': [2, 1, 1, 15, 'any + 1 potion']}
		return(treasure_dict)
	elif treasure_type == 'E':
		treasure_dict = {
			'Copper': [1, 6, 1000, 5, 'na'], 
			'Silver': [1, 10, 1000, 25, 'na'], 
			'Gold': [1, 4, 1000, 25, 'na'], 
			'Platinum or Electrum': [3, 6, 100, 25, 'na'], 
			'Gems':[1, 12, 1, 15, 'na'], 
			'Jewelry': [1, 6, 1, 10, 'na'], 
			'Magic Items or maps': [3, 1, 1, 25, 'any + 1 scroll']}
		return(treasure_dict)
	elif treasure_type == 'F':
		treasure_dict = {
			'Copper': [1, 1, 1, 0, 'na'], 
			'Silver': [3, 6, 1000, 10, 'na'], 
			'Gold': [1, 6, 1000, 40, 'na'], 
			'Platinum or Electrum': [1, 4, 1000, 15, 'na'], 
			'Gems':[2, 10, 1, 20, 'na'], 
			'Jewelry': [1, 8, 1, 10, 'na'], 
			'Magic Items or maps': [5, 1, 1, 30, 'non-weapon']}
		return(treasure_dict)
	elif treasure_type == 'G':
		treasure_dict = {
			'Copper': [1, 1, 1, 0, 'na'], 
			'Silver': [1, 1, 1, 0, 'na'], 
			'Gold': [2, 10, 1000, 50, 'na'], 
			'Platinum or Electrum': [1, 10, 1000, 50, 'na'], 
			'Gems':[3, 6, 1, 30, 'na'], 
			'Jewelry': [1, 6, 1, 25, 'na'], 
			'Magic Items or maps': [5, 1, 1, 35, 'any']}
		return(treasure_dict)
	elif treasure_type == 'H':
		treasure_dict = {
			'Copper': [3, 6, 1000, 25, 'na'], 
			'Silver': [2, 10, 1000, 40, 'na'], 
			'Gold': [2, 10, 1000, 55, 'na'], 
			'Platinum or Electrum': [1, 8, 1000, 40, 'na'], 
			'Gems':[3, 10, 1, 50, 'na'], 
			'Jewelry': [2, 10, 1, 50, 'na'], 
			'Magic Items or maps': [6, 1, 1, 15, 'any']}
		return(treasure_dict)
	elif treasure_type == 'I':
		treasure_dict = {
			'Copper': [1, 1, 1, 0, 'na'], 
			'Silver': [1, 1, 1, 0, 'na'], 
			'Gold': [1, 1, 1, 0, 'na'], 
			'Platinum or Electrum': [1, 6, 100, 30, 'na'], 
			'Gems':[2, 6, 1, 55, 'na'], 
			'Jewelry': [2, 4, 1, 50, 'na'], 
			'Magic Items or maps': [1, 1, 1, 15, 'any']}
		return(treasure_dict)
	elif treasure_type == 'J':
		treasure_dict = {
			'Copper': [3, 8, 1, 100, 'na'], 
			'Silver': [1, 1, 1, 0, 'na'], 
			'Gold': [1, 1, 1, 0, 'na'], 
			'Platinum or Electrum': [1, 1, 1, 0, 'na'], 
			'Gems': [1, 1, 1, 0, 'na'],  
			'Jewelry': [1, 1, 1, 0, 'na'], 
			'Magic Items or maps': [1, 1, 1, 0, 'na']}
		return(treasure_dict)
	elif treasure_type == 'K':
		treasure_dict = {
			'Copper': [1, 1, 1, 0, 'na'], 
			'Silver': [3, 6, 1, 100, 'na'], 
			'Gold': [1, 1, 1, 0, 'na'], 
			'Platinum or Electrum': [1, 1, 1, 0, 'na'], 
			'Gems': [1, 1, 1, 0, 'na'],  
			'Jewelry': [1, 1, 1, 0, 'na'], 
			'Magic Items or maps': [1, 1, 1, 0, 'na']}
		return(treasure_dict)
	elif treasure_type == 'L':
		treasure_dict = {
			'Copper': [1, 1, 1, 0, 'na'], 
			'Silver': [1, 1, 1, 0, 'na'], 
			'Gold': [1, 1, 1, 0, 'na'], 
			'Platinum or Electrum': [2, 6, 1, 100, 'na'], 
			'Gems': [1, 1, 1, 0, 'na'],  
			'Jewelry': [1, 1, 1, 0, 'na'], 
			'Magic Items or maps': [1, 1, 1, 0, 'na']}
		return(treasure_dict)
	elif treasure_type == 'M':
		treasure_dict = {
			'Copper': [1, 1, 1, 0, 'na'], 
			'Silver': [1, 1, 1, 0, 'na'], 
			'Gold': [2, 4, 1, 100, 'na'], 
			'Platinum or Electrum': [1, 1, 1, 0, 'na'], 
			'Gems': [1, 1, 1, 0, 'na'],  
			'Jewelry': [1, 1, 1, 0, 'na'], 
			'Magic Items or maps': [1, 1, 1, 0, 'na']}
		return(treasure_dict)
	elif treasure_type == 'N':
		treasure_dict = {
			'Copper': [1, 1, 1, 0, 'na'], 
			'Silver': [1, 1, 1, 0, 'na'], 
			'Gold': [1, 1, 1, 0, 'na'], 
			'Platinum or Electrum': [1, 6, 1, 100, 'na'], 
			'Gems': [1, 1, 1, 0, 'na'],  
			'Jewelry': [1, 1, 1, 0, 'na'], 
			'Magic Items or maps': [1, 1, 1, 0, 'na']}
		return(treasure_dict)
	elif treasure_type == 'O':
		treasure_dict = {
			'Copper': [1, 4, 10, 100, 'na'], 
			'Silver': [1, 3, 10, 100, 'na'], 
			'Gold': [1, 1, 1, 0, 'na'], 
			'Platinum or Electrum': [1, 1, 1, 0, 'na'], 
			'Gems': [1, 1, 1, 0, 'na'],  
			'Jewelry': [1, 1, 1, 0, 'na'], 
			'Magic Items or maps': [1, 1, 1, 0, 'na']}
		return(treasure_dict)
	elif treasure_type == 'P':
		treasure_dict = {
			'Copper': [1, 1, 1, 0, 'na'], 
			'Silver': [1, 6, 10, 100, 'na'], 
			'Gold': [1, 1, 1, 0, 'na'], 
			'Platinum or Electrum': [1, 20, 1, 100, 'na'], 
			'Gems': [1, 1, 1, 0, 'na'],  
			'Jewelry': [1, 1, 1, 0, 'na'], 
			'Magic Items or maps': [1, 1, 1, 0, 'na']}
		return(treasure_dict)
	elif treasure_type == 'Q':
		treasure_dict = {
			'Copper': [1, 1, 1, 0, 'na'], 
			'Silver': [1, 1, 1, 0, 'na'], 
			'Gold': [1, 1, 1, 0, 'na'], 
			'Platinum or Electrum': [1, 1, 1, 0, 'na'], 
			'Gems': [1, 4, 1, 100, 'na'],  
			'Jewelry': [1, 1, 1, 0, 'na'], 
			'Magic Items or maps': [1, 1, 1, 0, 'na']}
		return(treasure_dict)
	elif treasure_type == 'R':
		treasure_dict = {
			'Copper': [1, 1, 1, 0, 'na'], 
			'Silver': [1, 1, 1, 0, 'na'], 
			'Gold': [2, 10, 1, 100, 'na'], 
			'Platinum or Electrum': [1, 6, 10, 100, 'na'], 
			'Gems': [2, 4, 1, 100, 'na'],  
			'Jewelry': [1, 3, 1, 100, 'na'], 
			'Magic Items or maps': [1, 1, 1, 0, 'na']}
		return(treasure_dict)
	elif treasure_type == 'S':
		treasure_dict = {
			'Copper': [1, 1, 1, 0, 'na'], 
			'Silver': [1, 1, 1, 0, 'na'], 
			'Gold': [1, 1, 1, 0, 'na'], 
			'Platinum or Electrum': [1, 1, 1, 0, 'na'], 
			'Gems': [1, 1, 1, 0, 'na'],  
			'Jewelry': [1, 1, 1, 0, 'na'], 
			'Magic Items or maps': [1, 8, 1, 100, 'potion']}
		return(treasure_dict)
	elif treasure_type == 'T':
		treasure_dict = {
			'Copper': [1, 1, 1, 0, 'na'], 
			'Silver': [1, 1, 1, 0, 'na'], 
			'Gold': [1, 1, 1, 0, 'na'], 
			'Platinum or Electrum': [1, 1, 1, 0, 'na'], 
			'Gems': [1, 1, 1, 0, 'na'],  
			'Jewelry': [1, 1, 1, 0, 'na'], 
			'Magic Items or maps': [1, 4, 1, 100, 'scroll']}
		return(treasure_dict)
	elif treasure_type == 'U':
		treasure_dict = {
			'Copper': [1, 1, 1, 0, 'na'], 
			'Silver': [1, 1, 1, 0, 'na'], 
			'Gold': [1, 1, 1, 0, 'na'], 
			'Platinum or Electrum': [1, 1, 1, 0, 'na'], 
			'Gems': [2, 8, 1, 90, 'na'],  
			'Jewelry': [1, 6, 1, 80, 'na'], 
			'Magic Items or maps': [1, 1, 1, 70, 'any']}
		return(treasure_dict)
	elif treasure_type == 'V':
		treasure_dict = {
			'Copper': [1, 1, 1, 0, 'na'], 
			'Silver': [1, 1, 1, 0, 'na'], 
			'Gold': [1, 1, 1, 0, 'na'], 
			'Platinum or Electrum': [1, 1, 1, 0, 'na'], 
			'Gems': [1, 1, 1, 0, 'na'],  
			'Jewelry': [1, 1, 1, 0, 'na'], 
			'Magic Items or maps': [2, 1, 1, 100, 'any']}
		return(treasure_dict)
	elif treasure_type == 'W':
		treasure_dict = {
			'Copper': [1, 1, 1, 0, 'na'], 
			'Silver': [1, 1, 1, 0, 'na'], 
			'Gold': [5, 6, 1, 100, 'na'], 
			'Platinum or Electrum': [1, 8, 1, 100, 'na'], 
			'Gems': [2, 8, 1, 60, 'na'],  
			'Jewelry': [1, 8, 1, 50, 'na'], 
			'Magic Items or maps': [2, 1, 1, 60, 'any']}
		return(treasure_dict)
	elif treasure_type == 'X':
		treasure_dict = {
			'Copper': [1, 1, 1, 0, 'na'], 
			'Silver': [1, 1, 1, 0, 'na'], 
			'Gold': [1, 1, 1, 0, 'na'], 
			'Platinum or Electrum': [1, 1, 1, 0, 'na'], 
			'Gems': [1, 1, 1, 0, 'na'],  
			'Jewelry': [1, 1, 1, 0, 'na'], 
			'Magic Items or maps': [2, 1, 1, 100, 'potion']}
		return(treasure_dict)
	elif treasure_type == 'Y':
		treasure_dict = {
			'Copper': [1, 1, 1, 0, 'na'], 
			'Silver': [1, 1, 1, 0, 'na'], 
			'Gold': [2, 6, 100, 100, 'na'], 
			'Platinum or Electrum': [1, 1, 1, 0, 'na'], 
			'Gems': [1, 1, 1, 0, 'na'],  
			'Jewelry': [1, 1, 1, 0, 'na'], 
			'Magic Items or maps': [1, 1, 1, 0, 'na']}
		return(treasure_dict)
	elif treasure_type == 'Z':
		treasure_dict = {
			'Copper': [1, 3, 100, 100, 'na'], 
			'Silver': [1, 4, 100, 100, 'na'], 
			'Gold': [1, 6, 100, 100, 'na'], 
			'Platinum or Electrum': [1, 4, 100, 100, 'na'], 
			'Gems': [1, 6, 1, 55, 'na'],  
			'Jewelry': [2, 6, 1, 50, 'na'], 
			'Magic Items or maps': [3, 1, 1, 50, 'any']}
		return(treasure_dict)
	else:
		print("[-] Something went wrong")
	


def find_magic_items(magic_item_type, q):
	if magic_item_type == 'any':
		calc_magic_item_types = []
		i = 0
		while i < q:
			f_array = openfile('magic-items')
			data = array_result(f_array)
			calc_magic_item_types.append(data.replace('\n', ''))
			i+=1
		return(calc_magic_item_types)
		
	elif magic_item_type == 'armor or weapon':
		calc_magic_item_types = []
		i = 0
		while i < q:
			f_array = openfile('armor-weapon')
			data = array_result(f_array)
			calc_magic_item_types.append(data.replace('\n', ''))
			i+=1
		return(calc_magic_item_types)

	elif magic_item_type == 'any + 1 potion':
		calc_magic_item_types = []
		i = 0
		while i < q:
			f_array = openfile('magic-items')
			data = array_result(f_array)
			calc_magic_item_types.append(data.replace('\n', ''))
			i+=1
		p = 0
		while p < q/2:
			calc_magic_item_types.append('potion')
			p+=1
		return(calc_magic_item_types)

	elif magic_item_type == 'any + 1 scroll':
		calc_magic_item_types = []
		i = 0
		while i < q:
			f_array = openfile('magic-items')
			data = array_result(f_array)
			calc_magic_item_types.append(data.replace('\n', ''))
			i+=1
		p = 0
		while p < q/3:
			calc_magic_item_types.append('scroll')
			p+=1
		return(calc_magic_item_types)

	elif magic_item_type == 'non-weapon':
		calc_magic_item_types = []
		i = 0
		while i < q:
			f_array = openfile('non-weapon')
			data = array_result(f_array)
			calc_magic_item_types.append(data.replace('\n', ''))
			i+=1
		return(calc_magic_item_types)

	elif magic_item_type == 'potion':
		calc_magic_item_types = []
		i = 0
		while i < q:
			calc_magic_item_types.append('potion')
			i+=1
		return(calc_magic_item_types)

	elif magic_item_type == 'scroll':
		calc_magic_item_types = []
		i = 0
		while i < q:
			calc_magic_item_types.append('scroll')
			i+=1
		return(calc_magic_item_types)



def roll_magic_items(mi):
	if mi == 'potion':
		f_array = openfile(mi)
		data = array_result(f_array)
		return(data)
		
	elif mi == 'scroll':
		f_array = openfile(mi)
		data = array_result(f_array)
		return(data)

	elif mi == 'ring':
		f_array = openfile(mi)
		data = array_result(f_array)
		return(data)

	elif mi == 'rodstaff':
		f_array = openfile(mi)
		data = array_result(f_array)
		return(data)

	elif mi == 'wand':
		f_array = openfile(mi)
		data = array_result(f_array)
		return(data)

	elif mi == 'miscA':
		f_array = openfile(mi)
		data = array_result(f_array)
		return(data)

	elif mi == 'miscB':
		f_array = openfile(mi)
		data = array_result(f_array)
		return(data)

	elif mi == 'miscC':
		f_array = openfile(mi)
		data = array_result(f_array)
		return(data)

	elif mi == 'miscD':
		f_array = openfile(mi)
		data = array_result(f_array)
		return(data)

	elif mi == 'miscE':
		f_array = openfile(mi)
		data = array_result(f_array)
		return(data)

	elif mi == 'armorshield':
		f_array = openfile(mi)
		data = array_result(f_array)
		return(data)

	elif mi == 'weapon':
		rNum = randint(1, 100)
		if rNum <= 28:
			weapon_type = 'weaponA'
		elif rNum <=56:
			weapon_type = 'weaponB'
		else:
			weapon_type = 'sword'
		f_array = openfile(weapon_type)
		data = array_result(f_array)
		return(data)