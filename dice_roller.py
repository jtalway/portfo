from random import randint

def check_for_modifier(quantity, dice, mod, mod_value):
	mv = int(mod_value)
	roll_result = calculate_dice_roll(quantity, dice)
	if mv != 0:
	    if mod == '+':
	    	mod_result = roll_result + mv
	    	return(mod_result, quantity, dice, mod, mod_value)
	    elif mod == '-':
	    	mod_result = roll_result - mv
	    	return(mod_result, quantity, dice, mod, mod_value)
	    else:
	    	print('something went wrong')
	else:
	    return(roll_result, quantity, dice, mod, mod_value)

def calculate_dice_roll(quantity, dice):
	q = int(quantity)
	die = int(dice)
	tmp = 0
	i = 0
	while i < q:
	    rNum = randint(1, die)
	    print(rNum)
	    tmp = rNum + tmp
	    i += 1
	roll_result = tmp
	return(roll_result)