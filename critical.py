from openfile import * 
from array_result import *
from crit_checks import *


def severity_gen(total_severity):
	if total_severity == 1:
		crit_array = ['1']
		return(crit_array)
	elif total_severity == 2:
		crit_array = ['2', '1']
		return(crit_array)
	elif total_severity == 3:
		crit_array = ['3', '1']
		return(crit_array)
	elif total_severity == 4:
		crit_array = ['4', '1']
		return(crit_array)
	elif total_severity == 5:
		crit_array = ['4', '2', '1']
		return(crit_array)
	elif total_severity == 6:
		crit_array = ['4', '3', '1']
		return(crit_array)
	elif total_severity == 7:
		crit_array = ['4', '3', '2']
		return(crit_array)
	elif total_severity == 8:
		crit_array = ['4', '3', '2', '1']
		return(crit_array)
	elif total_severity == 9:
		crit_array = ['4', '3', '2', '2']
		return(crit_array)
	elif total_severity == 10:
		crit_array = ['4', '3', '3', '3']
		return(crit_array)
	else:
		print("[-] Something went wrong")
	

def crit_gen(crit_array):
	crit_result = []
	for x in crit_array:
		# open file and populate array
		f_array = openfile(x)
		# generate effect
		effect = array_result(f_array)
		# print(effect)
		# check for conditionals in the effect, such as duration or direction
		crit_duration = check_duration(effect)
		# print(c_effect)
		# check for random die rolls in the effect, such as random damage ranges
		crit_roll_calc = check_dieroll(crit_duration)
		crit_result.append(crit_roll_calc.replace('\n', ''))
		# print(calculated)
	# check for multiple x2 damage
	crit_multiplier = duplicate_dmg(crit_result)
	#final_crit_result = check_damage_add(crit_multiplier)
	final_crit_result = crit_multiplier

	return(final_crit_result)

