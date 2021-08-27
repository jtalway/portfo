from openfile import * 
from array_result import *
from check_duration import *
from check_dieroll import *


def fseverity_gen():
	f_array = openfile('fsev')
	fsev_result = array_result(f_array)
	return(fsev_result)
	

def fsev_gen(fsev_array):
	fsev_result = []
	for x in fsev_array:
		# open file and populate array
		f_array = openfile(x)
		# generate effect
		effect = array_result(f_array)
		# print(effect)
		# check for conditionals in the effect, such as duration or direction
		f_effect = check_duration(effect)
		# print(c_effect)
		# check for random die rolls in the effect, such as random damage ranges
		calculated = check_dieroll(f_effect)
		fsev_result.append(calculated.replace('\n', ''))

	return(fsev_result)

