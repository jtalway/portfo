import re
from random import randint

def check_dieroll(data):

    die_roll = re.findall(r'{(?P<q>.*?)d(?P<die>.*?)}', data)
    # print(match)
    if die_roll:
        q = die_roll[0][0]
        die = die_roll[0][1]
        rNum = randint(1,int(die))* int(q) 
        # print("[+] Dice Quantity: " +  q + ", Die Size: " +  die + ", Random Die Roll Result: " + str(rNum))
        calculated = re.sub(r'{(?P<q>.*?)d(?P<die>.*?)}', str(rNum), data)
        return(calculated)

    else:
        # print("[-] Die roll NOT found")
        return(data)
