#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 2 (22T3) 

You can use this file to test your find_bughole_extent().

This file containing 6 test cases which you can choose by
adjusting the variable test_index in Line 48. 

You can use this file to come out with additional tests. 
"""

# %% import 
import find_bughole_extent as extent # For the function to be tested 
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
     [False, False, False, False,  True,  True,  True,  True,  True, False, False, False]])
concrete_bool_sample_3 = np.array(
    [[True,True,True],[True,True,True],[True,True,True]])

# %% Tests 
test_index = 6 # test_index can be 0, 1, 2, 3, 4 or 5 

if test_index == 0:
    concrete_bool = np.copy(concrete_bool_sample_0)
    index_0 = 3
    index_1 = 4
       
    expected_bughole_axis_0_lower = 2
    expected_bughole_axis_0_upper = 5
    expected_bughole_axis_1_lower = 3
    expected_bughole_axis_1_upper = 5

elif test_index == 6:
    concrete_bool = np.copy(concrete_bool_sample_3)
    index_0 = 1
    index_1 = 1
       
    expected_bughole_axis_0_lower = 0
    expected_bughole_axis_0_upper = 3
    expected_bughole_axis_1_lower = 0
    expected_bughole_axis_1_upper = 3

elif test_index == 1:
    concrete_bool = np.copy(concrete_bool_sample_0)
    index_0 = 4
    index_1 = 7
       
    expected_bughole_axis_0_lower = 4
    expected_bughole_axis_0_upper = 6
    expected_bughole_axis_1_lower = 6
    expected_bughole_axis_1_upper = 9

elif test_index == 2:
    concrete_bool = np.copy(concrete_bool_sample_0)
    index_0 = 8
    index_1 = 7
       
    expected_bughole_axis_0_lower = 7
    expected_bughole_axis_0_upper = 9
    expected_bughole_axis_1_lower = 4
    expected_bughole_axis_1_upper = 10 
    
elif test_index == 3:
    concrete_bool = np.copy(concrete_bool_sample_1)
    index_0 = 2
    index_1 = 3
       
    expected_bughole_axis_0_lower = 0
    expected_bughole_axis_0_upper = 5
    expected_bughole_axis_1_lower = 0
    expected_bughole_axis_1_upper = 4     

elif test_index == 4:
    concrete_bool = np.copy(concrete_bool_sample_1)
    index_0 = 3
    index_1 = 10
       
    expected_bughole_axis_0_lower = 2
    expected_bughole_axis_0_upper = 6
    expected_bughole_axis_1_lower = 9
    expected_bughole_axis_1_upper = 12 

elif test_index == 5:
    concrete_bool = np.copy(concrete_bool_sample_1)
    index_0 = 7
    index_1 = 4
       
    expected_bughole_axis_0_lower = 7
    expected_bughole_axis_0_upper = 10
    expected_bughole_axis_1_lower = 4
    expected_bughole_axis_1_upper = 9
    
# %% Plot 
import matplotlib.patches as patches

# Plot the Boolean array and the position of the pixel at (index_0,index_1)
# so that you have a visual picture of the test case
# Plot the expected answer
plt.figure()
plt.imshow(concrete_bool, cmap = 'gray_r', vmin = 0, vmax = 1)
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
ax = plt.gca()
rect = patches.Rectangle((index_1-0.5,index_0-0.5),1,1,linewidth=2,
                         edgecolor='r',facecolor='r')
ax.add_patch(rect)
plt.title('concrete_bool. White: False. Black: True. Red: starting pixel.')            
plt.show()

# %% Run the function and check the answers
# Call the function find_bughole_extent() and store the answer in your_answer
your_bughole_axis_0_lower, your_bughole_axis_0_upper, \
your_bughole_axis_1_lower, your_bughole_axis_1_upper = \
    extent.find_bughole_extent(concrete_bool, index_0, index_1)



# Create lists to do the comparisons
expected_answer = \
    [expected_bughole_axis_0_lower, expected_bughole_axis_0_upper, 
     expected_bughole_axis_1_lower, expected_bughole_axis_1_upper]
your_answer = \
    [your_bughole_axis_0_lower, your_bughole_axis_0_upper, 
     your_bughole_axis_1_lower, your_bughole_axis_1_upper]
var_names = \
    ['bughole_axis_0_lower', 'bughole_axis_0_upper', \
     'bughole_axis_1_lower', 'bughole_axis_1_upper']

for k in range(len(var_names)):
    # Print the purpose and answers  
    print('For the computation of:',var_names[k])
    print('\tYour function returns',your_answer[k])
    print('\tThe expected answer is',expected_answer[k])
    
    if type(your_answer[k]) in [int, np.int64, np.int32]:
        if your_answer[k] == expected_answer[k]:
            print('\tYour',var_names[k],'is correct')
        else:
            print('\tYour',var_names[k],'is NOT correct') 
    else:
        print('\tYour',var_names[k],'does not have the correct type') 

    print('')