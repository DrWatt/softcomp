# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

rule30 = {"000": '.',
          "00.": '.',
          "0.0": '.',
          "...": '.',
          "0..": '0',
          ".00": '0',
          ".0.": '0',
          "..0": '0',
         }

def simulation(nsteps):
    
    initial_state = generate_state()
    states_seq = [initial_state]
    for i in range(nsteps):
        old_state = states_seq[-1]
        new_state = evolve(old_state)
        states_seq.append(new_state)
    return states_seq

def generate_state():
    return "0000.0.000000"

def evolve(stato):
    #fin=""
    chunk = len(stato)
    chunk_size = 3
    stato_split = [stato[i:i+chunk_size] for i in range(0, chunk, chunk_size)]
    for i in rule30.keys():    
        for j,k in enumerate(stato_split):
            if k == i:
                stato_split[j] = rule30[i] 
    
    return ''.join(stato_split)


#########################
    """
def test_generation_valid_state():
    state = generate_state()
    assert set(state) == {'.', '0'}
    

def test_generation_single_alive():
    state = generate_state()
    num_of_0 = sum(1 for i in state if i=='0')
    assert num_of_0 == 1
    """