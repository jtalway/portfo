import re
from random import randint
from openfile import * 
from array_result import *

# ring of multiple wishes
# ring of spell storing
# ring of telekinesis
# ring of wizardy
# <rod> charges 50 - {1d10-1}
# <staff> charges 25 - {1d6-1}
# <wand> charges 100 - {1d20-1}
# ARTIFACT or RELIC
# bag of beans
# bag of holding
# bag of tricks
# beaker of plentiful potions
# book of infinite spells
# Bucknard's everfull purse
# dust of appearance
# dust of disappearance
# incense of meditation
# incense of obsession
# ioun stones
# iron flask
# javelin of lightning
# javelin of piercing
# necklace of missiles
# necklace of prayer beads
# Nolzur's marvelous pigments
# Quaal's feather token
# robe of useful items
# scarab of enraging enemies
# scarab of insanity
# <sword>
# arrow of slaying
# scimitar +2

def check_special_item(magic_item):
	if magic_item == 'ring of protection':
		item_array = openfile('ring-protection')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'bracers of defense':
		item_array = openfile('misc-bracers-defense')
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

	elif magic_item == 'instrument of the bards':
		item_array = openfile('misc-instrument-bard')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'manual of golems':
		item_array = openfile('misc-manual-golems')
		final_magic_item = array_result(item_array)
		return(final_magic_item)

	elif magic_item == 'medallion of ESP':
		item_array = openfile('misc-medallion-ESP')
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

	else:
		return(magic_item)