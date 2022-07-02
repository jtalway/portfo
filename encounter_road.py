from openfile import * 

def road_encounter_generation(quantity):
    q = int(quantity)
    i = 0
    encounter_list = []

    while i < q:
        res = randomchoice('encounter-road')
        encounter_list.append(res)
        i += 1

    return(encounter_list)