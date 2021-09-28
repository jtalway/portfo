from openfile import * 
from array_result import *

def npc_fact_generation():
    npc_alignment = openfile('npc-alignment')
    alignment = array_result(npc_alignment)
    npc_possessions = openfile('npc-possessions')
    possessions = array_result(npc_possessions)
    npc_age = openfile('npc-age')
    age = array_result(npc_age)
    npc_appearance = openfile('npc-appearance')
    appearance = array_result(npc_appearance)
    npc_sanity = openfile('npc-sanity')
    sanity = array_result(npc_sanity)
    npc_tendencies = openfile('npc-tendencies')
    tendencies = array_result(npc_tendencies)
    npc_personality = openfile('npc-personality')
    personality = array_result(npc_personality)
    npc_disposition = openfile('npc-disposition')
    disposition = array_result(npc_disposition)
    npc_intellect = openfile('npc-intellect')
    intellect = array_result(npc_intellect)
    npc_nature = openfile('npc-nature')
    nature = array_result(npc_nature)
    npc_materialism = openfile('npc-materialism')
    materialism = array_result(npc_materialism)
    npc_honesty = openfile('npc-honesty')
    honesty = array_result(npc_honesty)
    npc_bravery = openfile('npc-bravery')
    bravery = array_result(npc_bravery)
    npc_morals = openfile('npc-morals')
    morals = array_result(npc_morals)
    npc_piety = openfile('npc-piety')
    piety = array_result(npc_piety)
    npc_energy = openfile('npc-energy')
    energy = array_result(npc_energy)
    npc_thrift = openfile('npc-thrift')
    thrift = array_result(npc_thrift)
    npc_interests = openfile('npc-interests')
    interests = array_result(npc_interests)
    return [alignment,
        possessions,
        age,
        appearance,
        sanity,
        tendencies,
        personality,
        disposition,
        intellect,
        nature,
        materialism,
        honesty,
        bravery,
        morals,
        piety,
        energy,
        thrift,
        interests]



# FANTASY NAMES
def determine_fantasy_name(name_quantity):
    x = 0
    name_list = []
    # loop thru generators for each name quantity indicated
    while x < int(name_quantity):
        name1 = openfile('fantasy-name-01')
        begin_name = array_result(name1).replace('\n', '')
        name2 = openfile('fantasy-name-02')
        mid_name = array_result(name2).replace('\n', '')
        name3 = openfile('fantasy-name-03')
        end_name = array_result(name3).replace('\n', '')
        full_name = begin_name + mid_name + end_name
        name_list.append(full_name)
        x+=1
    # capitalize
    capitalized_names = [x.capitalize() for x in name_list]
    return capitalized_names