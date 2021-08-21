from openfile import * 
from array_result import *
from check_duration import *
from check_dieroll import *


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
		c_effect = check_duration(effect)
		# print(c_effect)
		# check for random die rolls in the effect, such as random damage ranges
		calculated = check_dieroll(c_effect)
		crit_result.append(calculated.replace('\n', ''))
		# print(calculated)

	# for i in crit_result:
	# 	print(i)

	return(crit_result)

