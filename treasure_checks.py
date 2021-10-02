import re
from random import randint
from openfile import * 
from array_result import *
import math

# bag of beans
# bag of tricks
# book of infinite spells
# necklace of prayer beads

def check_special_item(magic_item):
	#
	# BIG IF cuz they can't be all types
	#
	# check for scroll
	magic_item = check_if_scroll(magic_item)
	# check for sword
	magic_item = check_if_sword(magic_item)
	# check for rod
	magic_item = check_if_rod(magic_item)
	# check for staff
	magic_item = check_if_staff(magic_item)
	# check for wand
	magic_item = check_if_wand(magic_item)

	if magic_item == 'ring of protection':
		item_array = openfile('ring-protection')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'ring of spell storing':
		spells_list = []
		array = openfile('scroll-type')
		spellcasting_class = array_result(array)
		num_spells = randint(2,5)
		min_range = 1
		max_range = 7
		if spellcasting_class != "magic-user":
			max_range = 5
		else:
			pass
		i = 0
		while i < num_spells:
			rNum = randint(min_range, max_range)
			page = 'spells-' + spellcasting_class + '-' + str(rNum)
			f_array = openfile(page)
			randomly_rolled_spell = array_result(f_array)
			spells_list.append(randomly_rolled_spell)
			i += 1
		final_spells_list = ", ".join(spells_list)
		final_magic_item = f"ring of spell storing [{final_spells_list}]"
		return(final_magic_item)

	elif magic_item == 'ring of telekinesis':
		item_array = openfile('ring-telekinesis')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'ring of wizardry':
		item_array = openfile('ring-wizardry')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'ring of multiple wishes':
		rNum = randint(2, 8)
		wishes = str(rNum)
		magic_item = magic_item + " (" + wishes + " wishes)"
		return(magic_item)

	elif magic_item == 'bag of holding':
		item_array = openfile('misc-bag-holding')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'beaker of plentiful potions':
		potions_list = []
		pNum = randint(2, 5)
		i = 0
		while i < pNum:
			array = openfile('potion')
			potion_result = array_result(array)
			dNum = randint(2,5)
			final_potion_result = f"{potion_result} ({dNum} doses)"
			potions_list.append(final_potion_result)
			i += 1
		final_potions_list = ", ".join(potions_list)
		final_magic_item = f"beaker of plentiful potions [{final_potions_list}]"
		return(final_magic_item)

	elif magic_item == 'bracers of defense':
		item_array = openfile('misc-bracers-defense')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == "Bucknard's everfull purse":
		item_array = openfile('misc-everfull-purse')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'cloak of protection':
		item_array = openfile('misc-cloak-protection')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'crystal ball':
		item_array = openfile('misc-crystal-ball')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'carpet of flying':
		item_array = openfile('misc-carpet-flying')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'dust of appearance':
		rNum = randint(5, 50)
		number = str(rNum)
		magic_item = magic_item + " (" + number + " containers)"
		return(magic_item)

	elif magic_item == 'dust of disappearance':
		rNum = randint(5, 50)
		number = str(rNum)
		magic_item = magic_item + " (" + number + " containers)"
		return(magic_item)

	elif magic_item == 'figurine of wondrous power':
		item_array = openfile('misc-figurine-wondrous')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'girdle of giant strength':
		item_array = openfile('misc-girdle-giant')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'horn of Valhalla':
		item_array = openfile('misc-horn-Valhalla')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'incense of meditation':
		rNum = randint(2, 8)
		q = str(rNum)
		magic_item = magic_item + " (x " + q + ")"
		return(magic_item)

	elif magic_item == 'incense of obsession':
		rNum = randint(2, 8)
		q = str(rNum)
		magic_item = magic_item + " (x " + q + ")"
		return(magic_item)

	elif magic_item == 'instrument of the bards':
		item_array = openfile('misc-instrument-bards')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'ioun stones':
		rNum = randint(1,10)
		stones_list = []
		i = 0
		while i < rNum:
			array = openfile('misc-ioun-stone')
			stone_result = array_result(array)
			if stone_result != "dull gray stone (burned out)":
				if stone_result in stones_list:
					stones_list.append("dull gray stone (burned out)")
				else:
					stones_list.append(stone_result)
			else:
				stones_list.append(stone_result)
			i += 1
		final_stones_list = ", ".join(stones_list)
		final_magic_item = f"ioun stones (x{rNum}) [{final_stones_list}]"
		return final_magic_item

	elif magic_item == 'iron flask':
		item_array = openfile('misc-iron-flask')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'javelin of lightning':
		rNum = randint(2, 5)
		q = str(rNum)
		magic_item = magic_item + " (x " + q + ")"
		return(magic_item)

	elif magic_item == 'javelin of piercing':
		rNum = randint(2, 8)
		q = str(rNum)
		magic_item = magic_item + " (x " + q + ")"
		return(magic_item)

	elif magic_item == 'manual of golems':
		item_array = openfile('misc-manual-golems')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'medallion of ESP':
		item_array = openfile('misc-medallion-ESP')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'necklace of missiles':
		item_array = openfile('misc-necklace-missiles')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == "Nolzur's marvelous pigments":
		rNum = randint(1, 4)
		number = str(rNum)
		magic_item = magic_item + " (" + number + " containers)"
		return(magic_item)

	elif magic_item == "Quaal's feather token":
		item_array = openfile('misc-feather-token')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'pearl of power':
		item_array = openfile('misc-pearl-power')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'periapt of proof against poison':
		item_array = openfile('misc-periapt-poison')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'robe of the archmagi':
		item_array = openfile('misc-robe-archmagi')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'scarab of enraging enemies':
		rNum = randint(19, 24)
		charges = str(rNum)
		magic_item = magic_item + " (" + charges + " charges)"
		return(magic_item)

	elif magic_item == 'scarab of insanity':
		rNum = randint(9, 16)
		charges = str(rNum)
		magic_item = magic_item + " (" + charges + " charges)"
		return(magic_item)

	elif magic_item == 'ARTIFACT OR RELIC':
		item_array = openfile('artifactrelic')
		final_magic_item = array_result(item_array).upper()
		return(final_magic_item)

	elif magic_item == 'potion of animal control':
		item_array = openfile('potion-animal-control')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'potion of dragon control':
		item_array = openfile('potion-dragon-control')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'potion of giant control':
		item_array = openfile('potion-giant-control')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'potion of giant strength':
		item_array = openfile('potion-giant-strength')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'potion of human control':
		item_array = openfile('potion-human-control')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'potion of undead control':
		item_array = openfile('potion-undead-control')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'scroll of protection from elementals':
		item_array = openfile('scroll-protection-elementals')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'scroll of protection from lycanthropes':
		item_array = openfile('scroll-protection-lycanthropes')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'ring of contrariness':
		item_array = openfile('ring-contrariness')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'ring of elemental command':
		item_array = openfile('ring-elemental-command')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'ring of regeneration':
		item_array = openfile('ring-regeneration')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'arrow of slaying':
		item_array = openfile('weapon-arrow-slaying')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'scimitar +2':
		item_array = openfile('weapon-scimitar')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	else:
		return(magic_item)

def check_if_scroll(magic_item):
	is_scroll = re.findall(r'^scroll of (?P<num_spells>.*?) spell(s\b|\b) {(?P<min_range>.*?)a(?P<max_range>.*?)}', magic_item)
	if is_scroll:
		i = 0
		scroll_list = []
		num_spells = int(is_scroll[0][0])
		min_range = int(is_scroll[0][2])
		max_range = int(is_scroll[0][3])
		f_array = openfile('scroll-type')
		spellcasting_class = array_result(f_array).replace('\n', '')
		if spellcasting_class == "magic-user":
			pass
		else:
			if max_range == 8:
				max_range = 6
			elif max_range == 9:
				max_range = 7
			else:
				pass
		while i < num_spells:
			rNum = randint(min_range, max_range)
			page = 'spells-' + spellcasting_class + '-' + str(rNum)
			f_array = openfile(page)
			randomly_rolled_spell = array_result(f_array).replace('\n', '')
			scroll_list.append(randomly_rolled_spell)
			i += 1
		scroll_header = spellcasting_class + " scroll ["
		scroll_footer = "]"
		generated_spells = ", ".join(scroll_list)
		complete_scroll = scroll_header + generated_spells + scroll_footer
		return(complete_scroll)

	else:
		return(magic_item)


def check_if_rod(magic_item):
	is_rod = re.findall(r'^\brod\b of \w+', magic_item)
	# check for rod not possessing charges
	if magic_item == 'rod of cancellation':
		return(magic_item)
	else:
		if is_rod:
			rNum = randint(0, 9)
			charges = str(50 - rNum)
			complete_rod = magic_item + " (" + charges + " charges)"
			return(complete_rod)
		else:
			return(magic_item)

def check_if_staff(magic_item):
	is_staff = re.findall(r'^\bstaff\b of \w+', magic_item)
	if is_staff:
		rNum = randint(0, 5)
		charges = str(25 - rNum)
		complete_staff = magic_item + " (" + charges + " charges)"
		return(complete_staff)
	else:
		return(magic_item)

def check_if_wand(magic_item):
	is_wand = re.findall(r'^\bwand\b of \w+', magic_item)
	if is_wand:
		rNum = randint(0, 19)
		charges = str(100 - rNum)
		complete_wand = magic_item + " (" + charges + " charges)"
		return(complete_wand)
	else:
		return(magic_item)

def check_if_sword(magic_item):
	is_sword = re.findall(r'^\bsword\b', magic_item)
	if is_sword:
		alignment = ''
		array = openfile('sword-type')
		sword_type = array_result(array).replace('\n', '')
		# CHECK FOR SPECIAL SWORD, I.E. INTELLIGENCE
		special_array = openfile('sword-intelligence')
		intelligence = array_result(special_array).replace('\n', '')
		extra_ability = ''
		num_primary = 0
		num_extraordinary = 0
		communication = 0
		languages_list = []
		ego_int = 0
		if intelligence == '0':
			pass
		elif intelligence == '12':
			num_primary = 1
			communication = 'semi-empathy'
		elif intelligence == '13':
			num_primary = 2
			communication = 'empathy'
		elif intelligence == '14':
			num_primary = 2
			communication = 'speech'
			languages_list = determine_languages()
		elif intelligence == '15':
			num_primary = 3
			communication = 'speech'
			languages_list = determine_languages()
		elif intelligence == '16':
			num_primary = 3
			communication = 'speech'
			languages_list = determine_languages()
			extra_ability = ' - read non-magical languages and maps'
			ego_int = 1
		elif intelligence == '17':
			num_primary = 3
			num_extraordinary = 1
			communication = 'speech and telepathy'
			languages_list = determine_languages()
			extra_ability = ' - read languages and magical writings'
			ego_int = 5
		else:
			print("[-] ERROR > treasure_checks.py > magic_item > checking if special sword")

		if intelligence != '0':
			# get alignment
			cursed_swords = {'sword +1 (cursed)', 'sword -2 (cursed)', 'sword (cursed berserking)'}
			if magic_item in cursed_swords:
				alignment = 'N'
			elif magic_item == 'sword +5 (holy avenger)':
				alignment = 'LG'
			elif magic_item == 'sword of sharpness':
				rNum = randint(1, 3)
				if rNum == 1:
					alignment = 'CG'
				elif rNum == 2:
					alignment = 'CE'
				else:
					alignment = 'CN'
			elif magic_item == 'sword (vorpal weapon)':
				rNum = randint(1, 3)
				if rNum == 1:
					alignment = 'LG'
				elif rNum == 2:
					alignment = 'LE'
				else:
					alignment = 'LN'
			else:
				array = openfile('sword-alignment')
				alignment = array_result(array).replace('\n', '')
			primary_ability_list = []
			extraordinary_ability_list = []
			special_purpose = ''
			languages_known = ", ".join(languages_list)
			if communication == 'speech' or communication == 'speech and telepathy':
				communication = f"{communication} - languages: {alignment}, {languages_known}"
			else:
				pass
			# get primary abilities
			# for each primary ability roll on table
			#print("------------------------------")
			#print(f"Prim: {num_primary}, Extra: {num_extraordinary}")
			p = 0
			while p < num_primary:
				pNum = randint(1, 100)
				# roll on extraordinary powers instead
				if pNum < 3:  # 3
					num_extraordinary = num_extraordinary + 1
					#print("[+] Primary resulted in Extraordinary")
					#print(f"Prim: {num_primary}, Extra: {num_extraordinary}")
				# roll twice on table ignoring this result
				elif pNum < 9:
					first_primary = determine_primary_abilities()
					primary_ability_list.append(first_primary)
					second_primary = determine_primary_abilities()
					primary_ability_list.append(second_primary)
					#print("[+] Double primary!")
				else:
					primary_power = determine_primary_abilities()
					primary_ability_list.append(primary_power)
				#print(f'Loop: {p}, NumPrimary: {num_primary}, random: {pNum}')
				p += 1
			#print(f"Primaries: {len(primary_ability_list)} {primary_ability_list}")
			e = 0
			while e < num_extraordinary:
				eNum = randint(1, 100)
				if eNum < 2:  # 2
					extraordinary_ability_list.append("character may choose one extraordinary power DMG 167")
					special_purpose = determine_special_purpose()
					#print("[+] Special Purpose and choose an extraordinary")
					#print(f"Prim: {num_primary}, Extra: {num_extraordinary}")
				elif eNum < 4:
					extraordinary_ability_list.append("character may choose one extraordinary power DMG 167")
				elif eNum < 7:
					first_extraordinary = determine_extraordinary_abilities()
					extraordinary_ability_list.append(first_extraordinary)
					second_extraordinary = determine_extraordinary_abilities()
					extraordinary_ability_list.append(second_extraordinary)
					#print("[+] Double extraordinary!")
				else:
					extraordinary_power = determine_extraordinary_abilities()
					extraordinary_ability_list.append(extraordinary_power)
				#print(f'Loop: {p}, NumExtraordinary: {num_extraordinary}, random: {eNum}')
				e += 1
			#print(f"Extraordinaries: {extraordinary_ability_list}")
			#print("------------------------------")
			formatted_primary_ability_list = ", ".join(primary_ability_list)
			formatted_extraordinary_ability_list = ", ".join(extraordinary_ability_list)
			ego_plus = find_ego_plus(magic_item)
			ego_primaries =  len(primary_ability_list)
			ego_extraordinaries = 2 * len(extraordinary_ability_list)
			if languages_list != []:
				ego_languages = math.ceil((len(languages_list) + 1) / 2)
				#print(f"Languages known: {languages_list}, Ego: {ego_languages}")
			else: 
				ego_languages = 0
			if special_purpose != '':
				ego_specialpurpose = 5
			else:
				ego_specialpurpose = 0

			total_ego = ego_plus + ego_primaries + ego_extraordinaries + ego_specialpurpose + ego_languages + ego_int

			if special_purpose != '':
				complete_sword = f"{sword_type} {magic_item} [AL: {alignment}, Int: {intelligence}, Ego: {total_ego}, Communication: {communication + extra_ability}; {formatted_primary_ability_list}, {formatted_extraordinary_ability_list}, {special_purpose}]"
			elif formatted_extraordinary_ability_list != '' and formatted_primary_ability_list == '':
				complete_sword = f"{sword_type} {magic_item} [AL: {alignment}, Int: {intelligence}, Ego: {total_ego}, Communication: {communication + extra_ability}; {formatted_extraordinary_ability_list}]"
			elif formatted_extraordinary_ability_list != '' and formatted_primary_ability_list != '':
				complete_sword = f"{sword_type} {magic_item} [AL: {alignment}, Int: {intelligence}, Ego: {total_ego}, Communication: {communication + extra_ability}; {formatted_primary_ability_list}, {formatted_extraordinary_ability_list}]"
			else:
				complete_sword = f"{sword_type} {magic_item} [AL: {alignment}, Int: {intelligence}, Ego: {total_ego}, Communication: {communication + extra_ability}; {formatted_primary_ability_list}]"
		else:
			complete_sword = f"{sword_type} {magic_item}"
		return(complete_sword)
	else:
		return(magic_item)

def determine_primary_abilities():
	array = openfile('sword-primary')
	primary_ability = array_result(array).replace('\n', '')
	return primary_ability

def determine_extraordinary_abilities():
	array = openfile('sword-extraordinary')
	extraordinary_ability = array_result(array).replace('\n', '')
	return extraordinary_ability

def determine_special_purpose():
	array = openfile('sword-purpose')
	special_purpose = array_result(array).replace('\n', '')
	pp_array = openfile('sword-purpose-power')
	special_purpose_power = array_result(pp_array).replace('\n', '')
	sword_special_purpose = f"Special Purpose: {special_purpose}, Special Purpose Power: {special_purpose_power}"
	return sword_special_purpose

def determine_languages():
	languages_list = []
	array = openfile('sword-languages')
	num_languages = array_result(array).replace('\n', '')
	i = 0
	#print(f"[+] START with {num_languages}")
	while i < int(num_languages):
		lang_array = openfile('languages')
		language = array_result(lang_array).replace('\n', '')
		#print(language)
		if language in languages_list:
			#print("!!! DUPLICATE LANGUAGE !!!")
			continue
		else:
			languages_list.append(language)
			i += 1
	#print(languages_list)
	return languages_list

def find_ego_plus(magic_item):
	plus_zero = {'sword -2 (cursed)'}
	plus_one = {'sword +1'}
	plus_two = {'sword +1 (luck blade)', 'sword +2', 'sword of wounding', 'sword of sharpness', 'sword +1 (cursed)'}
	plus_three = {'sword +1 (+2 vs magic-using and enchanted creatures)', 'sword +3', 'sword (cursed berserking)'}
	plus_four = {'sword +1 (+3 vs lycanthropes and shape changers)', 'sword +1 (+3 vs regenerating creatures)', 'sword +2 (nine lives stealer)', 'sword +4', 'sword of life stealing'}
	plus_five = {'sword +1 (+4 vs reptiles)', 'sword +1 (flame tongue)', 'sword +2 (giant slayer)', 'sword +5', 'sword of dancing'}
	plus_six = {'sword +2 (dragon slayer)', 'sword (vorpal weapon)'}
	plus_eight = {'sword +4 (defender)'}
	plus_nine = {'sword +3 (frost brand)'}
	plus_ten = {'sword +5 (defender)', 'sword +5 (holy avenger)'}
	if magic_item in plus_one:
		ego_plus = 1
	elif magic_item in plus_two:
		ego_plus = 2
	elif magic_item in plus_three:
		ego_plus = 3
	elif magic_item in plus_four:
		ego_plus = 4
	elif magic_item in plus_five:
		ego_plus = 5
	elif magic_item in plus_six:
		ego_plus = 6
	elif magic_item in plus_eight:
		ego_plus = 8
	elif magic_item in plus_nine:
		ego_plus = 9
	elif magic_item in plus_ten:
		ego_plus = 10
	else:
		ego_plus = 0

	return ego_plus

