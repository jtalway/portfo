from random import randint

def abilityscore_gen(method):
	ability_scores = {'Strength': 0, 'Dexterity': 0, 'Constitution': 0, 'Intelligence': 0, 'Wisdom': 0, 'Charisma': 0}
	if method == '1':
		for ability, score in ability_scores.items():
			tmp = 0
			i = 0
			while i < 3:
				rNum = randint(1, 6)
				tmp = tmp + rNum
				i += 1
			ability_scores[ability] = tmp
		return(ability_scores)

	elif method == '2':
		for ability, score in ability_scores.items():
			rolls = []
			i = 0
			tmp = 0
			while i < 4:
				rNum = randint(1,6)
				rolls.append(rNum)
				i += 1
			sorted_rolls = sorted(rolls, reverse=True)
			tmp = sorted_rolls[0] + sorted_rolls[1] + sorted_rolls[2]
			ability_scores[ability] = tmp
		return(ability_scores)
