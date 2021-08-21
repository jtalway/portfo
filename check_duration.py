from array_result import *
from openfile import *
from check_dieroll import *
import re

def check_duration(effect):
	if re.findall(r'<duration>', effect):
		# open file 
		f_array = openfile('duration')
		# find result from array
		result = array_result(f_array)
		# check if die roll necessary
		c_effect = check_dieroll(result).replace('\n', '')
		d_effect = re.sub(r'<duration>', c_effect, effect)
		return(d_effect)

	elif re.findall(r'<duration2>', effect):
		f_array = openfile('duration2')
		result = array_result(f_array)
		c_effect = check_dieroll(result).replace('\n', '')
		d_effect = re.sub(r'<duration2>', c_effect, effect)
		return(d_effect)

	elif re.findall(r'<direction>', effect):
		f_array = openfile('direction')
		result = array_result(f_array)
		c_effect = check_dieroll(result).replace('\n', '')
		d_effect = re.sub(r'<direction>', c_effect, effect)
		return(d_effect)

	else:
		return(effect)