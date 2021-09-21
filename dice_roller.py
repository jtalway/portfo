from random import randint

def check_for_modifier(quantity, dice, mod, mod_value, adv):
	print(quantity, dice, mod, mod_value, adv)
	mv = int(mod_value)
	if adv == "advantage" or "disadvantage":
		roll_result = calculate_dice_roll(1, 20, adv)
	else:
		roll_result = calculate_dice_roll(quantity, dice, adv)
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

def calculate_dice_roll(quantity, dice, adv):
	q = int(quantity)
	die = int(dice)
	tmp = 0
	i = 0
	if adv == 'advantage':
		rNum1 = randint(1, 20)
		rNum2 = randint(1, 20)
		roll_result = max(rNum1, rNum2)
		print(rNum1, rNum2, roll_result)
	elif adv == 'disadvantage':
		rNum1 = randint(1, 20)
		rNum2 = randint(1, 20)
		roll_result = min(rNum1, rNum2)
		print(rNum1, rNum2, roll_result)
	else:
		while i < q:
		    rNum = randint(1, die)
		    print(rNum)
		    tmp = rNum + tmp
		    i += 1
		roll_result = tmp
	return(roll_result)