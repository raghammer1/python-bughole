#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 2 (22T3) 

You can use this file to test your find_edge_after().

This file containing 8 test cases which you can choose by
adjusting the variable test_index in Line 19. 

You can use this file to come out with additional tests. 
"""

# %% import 
import find_edge_after as after # For the function to be tested 
import numpy as np 

# %% Tests 
test_index = 7 # test_num can be 0, 1, 2, 3, 4, 5, 6, 7

if test_index == 0:
    array_bool = \
        np.array([False, False, False, False, True,  True,  True,  True, 
                  False, False, False,  True, True, False, False, False])
    start_index = 4 
    expected_answer = 8 

elif test_index == 1:
    array_bool = \
    np.array([False, False, False, False, True,  True,  True,  True, 
              False, False, False,  True, True, False, False, False])
    start_index = 6 
    expected_answer = 8
 
elif test_index == 2:
    array_bool = \
    np.array([False, False, False, False, True,  True,  True,  True, 
              False, False, False,  True, True, False, False, False])
    start_index = 11 
    expected_answer = 13    
 
elif test_index == 3:
    array_bool = \
    np.array([False, False, False, False, True,  True,  True,  True, 
              False, False, False,  True, True, False, False, False])
    start_index = 12 
    expected_answer = 13 
    
elif test_index == 4:    
    array_bool = \
    np.array([True,  True,  True, True,
              False, False, False, True,  True, False, False, False])
    start_index = 0
    expected_answer = 4

elif test_index == 5:    
    array_bool = \
    np.array([True,  True,  True,  True, False, False, 
              False, True,  True, False, False, False])
    start_index = 2
    expected_answer = 4
    
elif test_index == 6:    
    array_bool = \
    np.array([ True,  True, True, True, False, 
              False, False, True, True])
    start_index = 8
    expected_answer = 9

elif test_index == 7:    
    array_bool = \
    np.array([False,  True, True, True, False, 
              False, False, True, False])
    start_index = 7
    expected_answer = 8    

# %% Run the function and check the answers

# Call the function find_concrete_crack_bool() and store the answer in your_answer
your_answer = after.find_edge_after(array_bool, start_index)

print('Your function returns',your_answer)
print('The expected answer is',expected_answer)

try:       
    if your_answer == expected_answer:
        print('Your answer is correct')
    else:
        print('Your answer is NOT correct')          
except:
    print('Your answer is NOT correct.')
    print('Possibly because your answer is not an integer.')
