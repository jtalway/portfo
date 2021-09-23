import re
from random import randint
from openfile import * 
from array_result import *

# ring of spell storing
# ARTIFACT or RELIC
# bag of beans
# bag of tricks
# beaker of plentiful potions
# book of infinite spells
# ioun stones
# necklace of prayer beads
# <sword>

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
		final_magic_item = array_result(item_array)
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
		scroll_header = spellcasting_class + " scroll ("
		scroll_footer = ")"
		generated_spells = ", ".join(scroll_list)
		complete_scroll = scroll_header + generated_spells + scroll_footer
		return(complete_scroll)

	else:
		return(magic_item)


def check_if_rod(magic_item):
	is_rod = re.findall(r'^\brod\b of \w+', magic_item)
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
		array = openfile('sword-type')
		sword_type = array_result(array).replace('\n', '')
		complete_sword = sword_type + " " + magic_item
		return(complete_sword)
	else:
		return(magic_item)