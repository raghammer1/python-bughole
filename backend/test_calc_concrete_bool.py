#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 2 (22T3) 

You can use this file to test your calc_concrete_bool().

This file containing 3 test cases which you can choose by
adjusting the variable test_index in Line 20. 

You can use this file to come out with additional tests. 
"""

# %% import 
import calc_concrete_bool as calc # For the function to be tested 
import numpy as np 
import matplotlib.pyplot as plt # For plotting the image

# %% Tests 
test_index = 2 # test_index can be 0, 1, 2

if test_index == 0:
    # The concrete image 
    concrete_image = np.array(
      [[200,  25,  25, 200, 200],
       [200,  25,  25, 200, 200],
       [200,  25,  25, 200, 200],
       [200, 200, 200, 200, 200]])
    
    threshold = 60
        
    expected_answer = np.array(
      [[False,  True,  True, False, False],
       [False,  True,  True, False, False],
       [False,  True,  True, False, False],
       [False, False, False, False, False]])

elif test_index == 1: 
    concrete_image = np.array(
          [[177, 247, 152, 212, 149, 215, 145, 219, 204, 156],
           [141, 216, 211, 249, 146, 165, 190, 160, 241, 158],
           [224, 151, 246,  16,  12, 154, 190, 208, 227, 227],
           [245, 253, 234,  22,  21, 153, 245, 149, 147, 203],
           [201, 162, 197,  17,  23, 200,  23,  20,  27, 153],
           [187, 246, 212, 170, 211, 143,  17,  20,  10, 197],
           [143, 208, 164, 253, 183, 216, 166, 192, 220, 249],
           [181, 222, 155, 204,  18,  21,  22,  21,  14,  17],
           [166, 165, 244, 162,  17,  23,  14,  26,  28,  10],
           [177, 197, 223, 178, 148, 172, 174, 150, 163, 155],
           [251, 227, 165, 211, 232, 214, 202, 186, 172, 228],
           [163, 195, 205, 253, 217, 143, 140, 217, 146, 192]])
    
    threshold = 40
    
    expected_answer = np.array(
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

    
elif test_index == 2: 
    concrete_image = np.array(
          [[ 20,  15,  27,  25, 162, 183, 222, 215, 244, 147, 174, 189],
           [ 23,  17,  21,  25, 203, 171, 230, 160, 177, 179, 207, 242],
           [ 29,  27,  14,  10, 243, 178, 246, 173, 198,  19,  21,  24],
           [ 18,  14,  21,  24, 223, 171, 206, 220, 192,  24,  10,  26],
           [ 28,  19,  17,  27, 189, 179, 186, 148, 190,  21,  12,  20],
           [249, 148, 157, 162, 213, 197, 245, 250, 230,  27,  29,  29],
           [183, 172, 166, 254, 148, 216, 150, 180, 174, 200, 149, 241],
           [210, 226, 210, 159,  28,  11,  25,  24,  10, 221, 201, 210],
           [241, 237, 158, 224,  17,  27,  18,  22,  24, 241, 214, 212],
           [230, 239, 231, 236, 156, 195, 161, 183, 233, 220, 180, 210]])
    
    threshold = 65
    
    expected_answer = np.array(
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
     

# %% Run the function and check the answers

# Call the function find_concrete_crack_bool() and store the answer in your_answer
your_answer = calc.calc_concrete_bool(concrete_image,threshold)

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
                
            # Plot the given concrete image 
            plt.figure()
            plt.imshow(concrete_image, cmap = 'gray', vmin = 0, vmax = 255)
            # The following 8 lines of code are used to draw a grid at
            # the pixel boundary 
            x_min = -0.5
            x_max = concrete_image.shape[1]-0.5
            y_min = -0.5
            y_max = concrete_image.shape[0]-0.5
            x_for_vlines = np.arange(x_min,x_max+0.5)
            y_for_hlines = np.arange(y_min,y_max+0.5)
            plt.hlines(y_for_hlines,x_min,x_max,'b')
            plt.vlines(x_for_vlines,y_min,y_max,'b')
            plt.colorbar()
            plt.title('The given image')
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
            plt.title('Your answer. White: False. Black: True')
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
            plt.title('Expected answer. White: False. Black: True')            
            plt.show()
            
        else:
            print('Your answer has a shape of:',your_answer.shape)
            print('The expected answer has a shape of:',expected_answer.shape)
    else:
        print('Your function output did not return a numpy array of bool type')  
else:
    print('Your function output did not return a numpy array')    
