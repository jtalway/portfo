from random import randint

def array_result(array):
 	# find the highest number for range of random number generator
    h = int(array[-1].split(", ")[1])
    # generate a random number between 1 and highest number
    rNum = randint(1, h)
    # print(crit_array, rNum)
    array_length = len(array)
    for i in range(array_length):
        # determine the number of effect
        while rNum >= int(array[i].split(", ")[0]) and rNum <= int(array[i].split(", ")[1]):
            # grab the effect 
            effect = array[i].split(", ")[2]
            # print("Random Number from 1 to " + str(h) +": " + str(rNum))
            # print("Random Critical Effect: " + effect)
            return(effect)
