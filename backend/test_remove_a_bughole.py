#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 2 (22T3) 

You can use this file to test your remove_a_bughole().

This file containing 4 test cases which you can choose by
adjusting the variable test_index in Line 48. 

You can use this file to come out with additional tests. 
"""

# %% import 
import remove_a_bughole as remove # For the function to be tested 
import numpy as np 
import matplotlib.pyplot as plt # For plotting the image

# %% Define two Boolean arrays which will be used in the tests

concrete_bool_sample_0 = np.array(
     [[False, False, False, False, False, False, False, False, False, False],
      [False, False, False, False, False, False, False, False, False, False],
      [False, False, False,  True,  True, False, False, False, False, False],
      [False, False, False,  True,  True, False, False, False, False, False],
      [False, False, False,  True,  True, False,  True,  True,  True, False],
      [False, False, False, False, False, False,  True,  True,  True, False],
      [False, False, False, False, False, False, False, False, False, False],
      [False, False, False, False,  True,  True,  True,  True,  True,  True],
      [False, False, False, False,  True,  True,  True,  True,  True,  True],
      [False, False, False, False, False, False, False, False, False, False],
      [False, False, False, False, False, False, False, False, False, False],
      [False, False, False, False, False, False, False, False, False, False]])

concrete_bool_sample_1 = np.array(
    [[ True,  True,  True,  True, False, False, False, False, False, False, False, False],
     [ True,  True,  True,  True, False, False, False, False, False, False, False, False],
     [ True,  True,  True,  True, False, False, False, False, False,  True,  True,  True],
     [ True,  True,  True,  True, False, False, False, False, False,  True,  True,  True],
     [ True,  True,  True,  True, False, False, False, False, False,  True,  True,  True],
     [False, False, False, False, False, False, False, False, False,  True,  True,  True],
     [False, False, False, False, False, False, False, False, False, False, False, False],
     [False, False, False, False,  True,  True,  True,  True,  True, False, False, False],
     [False, False, False, False,  True,  True,  True,  True,  True, False, False, False],
     [False, False, False, False, False, False, False, False, False, False, False, False]])

# %% Tests 
test_index = 3 # test_index can be 0, 1, 2, 3

if test_index == 0:
    concrete_bool = np.copy(concrete_bool_sample_0)
    index_0 = 3
    index_1 = 4
       
    bughole_axis_0_lower = 2
    bughole_axis_0_upper = 5
    bughole_axis_1_lower = 3
    bughole_axis_1_upper = 5
    
    expected_answer = np.array(
         [[False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False,  True,  True,  True, False],
          [False, False, False, False, False, False,  True,  True,  True, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False,  True,  True,  True,  True,  True,  True],
          [False, False, False, False,  True,  True,  True,  True,  True,  True],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False]])

elif test_index == 1:
    concrete_bool = np.copy(concrete_bool_sample_0)
    index_0 = 4
    index_1 = 7
       
    bughole_axis_0_lower = 4
    bughole_axis_0_upper = 6
    bughole_axis_1_lower = 6
    bughole_axis_1_upper = 9
    
    expected_answer = np.array(
         [[False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False,  True,  True, False, False, False, False, False],
          [False, False, False,  True,  True, False, False, False, False, False],
          [False, False, False,  True,  True, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False,  True,  True,  True,  True,  True,  True],
          [False, False, False, False,  True,  True,  True,  True,  True,  True],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False, False, False, False]])
    
elif test_index == 2:
    concrete_bool = np.copy(concrete_bool_sample_1)
       
    bughole_axis_0_lower = 0
    bughole_axis_0_upper = 5
    bughole_axis_1_lower = 0
    bughole_axis_1_upper = 4     

    expected_answer = np.array(
    [[False, False, False, False, False, False, False, False, False, False, False, False],
     [False, False, False, False, False, False, False, False, False, False, False, False],
     [False, False, False, False, False, False, False, False, False,  True,  True,  True],
     [False, False, False, False, False, False, False, False, False,  True,  True,  True],
     [False, False, False, False, False, False, False, False, False,  True,  True,  True],
     [False, False, False, False, False, False, False, False, False,  True,  True,  True],
     [False, False, False, False, False, False, False, False, False, False, False, False],
     [False, False, False, False,  True,  True,  True,  True,  True, False, False, False],
     [False, False, False, False,  True,  True,  True,  True,  True, False, False, False],
     [False, False, False, False, False, False, False, False, False, False, False, False]])    

elif test_index == 3:
    concrete_bool = np.copy(concrete_bool_sample_1)
        
    bughole_axis_0_lower = 2
    bughole_axis_0_upper = 6
    bughole_axis_1_lower = 9
    bughole_axis_1_upper = 12 

    expected_answer = np.array(
    [[ True,  True,  True,  True, False, False, False, False, False, False, False, False],
     [ True,  True,  True,  True, False, False, False, False, False, False, False, False],
     [ True,  True,  True,  True, False, False, False, False, False, False, False, False],
     [ True,  True,  True,  True, False, False, False, False, False, False, False, False],
     [ True,  True,  True,  True, False, False, False, False, False, False, False, False],
     [False, False, False, False, False, False, False, False, False, False, False, False],
     [False, False, False, False, False, False, False, False, False, False, False, False],
     [False, False, False, False,  True,  True,  True,  True,  True, False, False, False],
     [False, False, False, False,  True,  True,  True,  True,  True, False, False, False],
     [False, False, False, False, False, False, False, False, False, False, False, False]])
    
# Make a copy of the given concrete_bool for plotting
concrete_bool_given = np.copy(concrete_bool)


# %% Run the function and check the answers
# Call the function remove_a_bughole() and store the answer in your_answer
your_answer = remove.remove_a_bughole(concrete_bool, 
                        bughole_axis_0_lower, bughole_axis_0_upper, 
                        bughole_axis_1_lower, bughole_axis_1_upper)

# Do some basic checks before making a comparison 
# These basic checks are: Is it a numpy array? Is dtype bool?
#                         Does it have the correct shape?
# If all these types are correct, then compare the entries 
if type(your_answer) is np.ndarray:
    # your answer is a numpy array
    if your_answer.dtype.name == 'bool':
        # your_answer is a numpy array of bool dtype
        if your_answer.shape == expected_answer.shape:
            # your_answer has the right type and shape
            if np.all(your_answer == expected_answer):
                # All entries are correct
                print('Your answer is correct')
            else: 
                # Not all entries are correct 
                print('Some elements in your answers are incorrect')
                
            # Plot the given concrete_bool 
            plt.figure()
            plt.imshow(concrete_bool_given, cmap = 'gray_r', vmin = 0, vmax = 1)
            # The following 8 lines of code are used to draw a grid at
            # the pixel boundary 
            x_min = -0.5
            x_max = concrete_bool.shape[1]-0.5
            y_min = -0.5
            y_max = concrete_bool.shape[0]-0.5
            x_for_vlines = np.arange(x_min,x_max+0.5)
            y_for_hlines = np.arange(y_min,y_max+0.5)
            plt.hlines(y_for_hlines,x_min,x_max,'b')
            plt.vlines(x_for_vlines,y_min,y_max,'b')
            plt.colorbar()
            plt.title(f'test_index = {test_index}. The given concrete_bool')
            plt.show()

            # Plot your answer
            plt.figure()
            plt.imshow(your_answer, cmap = 'gray_r', vmin = 0, vmax = 1)
            # The following 8 lines of code are used to draw a grid at
            # the pixel boundary 
            x_min = -0.5
            x_max = your_answer.shape[1]-0.5
            y_min = -0.5
            y_max = your_answer.shape[0]-0.5
            x_for_vlines = np.arange(x_min,x_max+0.5)
            y_for_hlines = np.arange(y_min,y_max+0.5)
            plt.hlines(y_for_hlines,x_min,x_max,'b')
            plt.vlines(x_for_vlines,y_min,y_max,'b')
            plt.title(f'test_index = {test_index}. Your answer')
            plt.show()
            
            # Plot the expected answer
            plt.figure()
            plt.imshow(expected_answer, cmap = 'gray_r', vmin = 0, vmax = 1)
            # The following 8 lines of code are used to draw a grid at
            # the pixel boundary 
            x_min = -0.5
            x_max = expected_answer.shape[1]-0.5
            y_min = -0.5
            y_max = expected_answer.shape[0]-0.5
            x_for_vlines = np.arange(x_min,x_max+0.5)
            y_for_hlines = np.arange(y_min,y_max+0.5)
            plt.hlines(y_for_hlines,x_min,x_max,'b')
            plt.vlines(x_for_vlines,y_min,y_max,'b')
            plt.title(f'test_index = {test_index}. Expected answer')            
            plt.show()
            
        else:
            print('Your answer has a shape of:',your_answer.shape)
            print('The expected answer has a shape of:',expected_answer.shape)
    else:
        print('Your function output did not return a numpy array of bool type')  
else:
    print('Your function output did not return a numpy array')    
