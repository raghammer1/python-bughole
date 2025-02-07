#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 2 (22T3) 

You can use this file to test your find_bugholes().

This file containing 3 test cases which you can choose by
adjusting the variable test_index in Line 20. 

You can use this file to come out with additional tests. 
"""

# %% import 
import find_bugholes as bugholes # For the function to be tested 
import numpy as np 
import matplotlib.pyplot as plt # For plotting the image

# %% Tests 
test_index = 2 # test_index can be 0, 1, 2

if test_index == 0:
    # The concrete image 
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
        
    expected_num_bugholes = 3
    
    expected_bugholes_locations = [[0, 5, 0, 4],
                                   [7, 9, 4, 9],
                                   [2, 6, 9, 12]]

elif test_index == 1: 
    concrete_image = np.array(
                [[ 14,  12,  19,  36, 212, 140, 161,  13,   7,  28, 181],
                 [  9,  26,   5,  20, 160, 184, 233,  36,   8,  26, 221],
                 [ 31,  17,   9,  32, 203, 200, 141,  24,  20,  30, 244],
                 [250, 237, 169, 246, 164, 202, 147,  17,  32,  22, 188],
                 [177, 160, 234, 189, 161, 218, 168,  39,  31,  32, 245],
                 [158, 203, 177, 196, 196, 211, 177, 186, 173, 253, 141],
                 [225, 214, 247, 240, 239, 231, 156, 220, 172, 156, 254],
                 [158, 215, 195, 236, 235, 153,  23,  24,  33, 201, 173],
                 [192, 253, 254, 142, 168, 176,  21,  26,  15, 188, 199],
                 [214, 194, 252, 240, 231, 253,  28,  11,  17, 244, 179],
                 [169, 172, 188, 149, 173, 251, 200, 228, 195, 151, 224],
                 [150, 252, 220, 216, 208, 184, 184, 159, 156, 238, 179],
                 [190, 205, 175, 185, 254, 192, 141,   7,  13,  31, 227],
                 [239, 160, 202, 221, 162, 232, 247,   4,  30,  13, 183],
                 [172, 232, 200, 156, 167, 193, 247, 148, 160, 148, 164]])
    
    threshold = 45
    
    expected_num_bugholes = 4
    expected_bugholes_locations = [[ 0,  3, 0,  4],
                                   [ 0,  5, 7, 10],
                                   [ 7, 10, 6,  9],
                                   [12, 14, 7, 10]]

    
elif test_index == 2: 
    concrete_image = np.array(
                [[186, 195, 209, 141, 244, 227, 212, 190, 149],
                 [198, 243, 249, 234, 195, 195, 197, 244, 176],
                 [190, 184,  32,  25, 192, 143,  28,  23, 161],
                 [161, 213,  25,   5, 196, 206,   6,  19, 148],
                 [189, 206, 198, 227, 172, 180,  15,  29, 173],
                 [172, 249, 168, 143, 254, 219, 238, 235, 197],
                 [190, 157, 252, 221, 229, 213, 199, 188, 216],
                 [163, 254, 234, 162, 207, 202,  29,  22, 163],
                 [196,  15,  25,  21, 249, 246,  33,   8, 222],
                 [195,  12,  24,  15, 234, 219,   6,   8, 199],
                 [247, 191, 148, 177, 212, 199, 194, 243, 236],
                 [170, 144, 194, 215, 148, 240, 171, 180, 157],
                 [218, 149, 193,  12, 202, 254, 199,  27, 144],
                 [179, 194, 210,  14, 236, 207, 247,  28, 162],
                 [248, 246, 157, 167, 237, 200, 183, 226, 155],
                 [153, 140, 150, 244, 147, 203, 242, 219, 244]])
    
    threshold = 41
    
    expected_num_bugholes = 6
    expected_bugholes_locations = [[ 2,  4, 2, 4],
                                   [ 2,  5, 6, 8],
                                   [ 7, 10, 6, 8],
                                   [12, 14, 7, 8],
                                   [ 8, 10, 1, 4],
                                   [12, 14, 3, 4]]
     
# %% Plot the concrete image
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
plt.title('The given concrete_image')
plt.show()

# %% Run the function and check the answers

# Call the function find_concrete_crack_bool() and store the answer in your_answer
your_num_bugholes, your_bugholes_locations = \
    bugholes.find_bugholes(concrete_image, threshold)

# Check the number of bugholes
print('For the number of bugholes:')
print('\tYour function returns',your_num_bugholes)
print('\tThe expected answer is',expected_num_bugholes)

try:       
    if your_num_bugholes == expected_num_bugholes:
        print('Your num_bugholes is correct')
    else:
        print('Your num_bugholes is NOT correct')          
except:
    print('\tYour num_bugholes is NOT correct.')
    print('\tPossibly because your answer is not an integer.')

# Check the locations of the bugholes
print('')
print('For the locations of the bugholes:')
print('\tYour function returns',your_bugholes_locations)
print('\tThe expected answer is',expected_bugholes_locations)

try:
    num_correct_locations = 0
    locations_found = []
    locations_not_found = []
    
    for location in expected_bugholes_locations:
        if location in your_bugholes_locations:
            num_correct_locations += 1
            locations_found.append(location)
        else: 
            locations_not_found.append(location)
            
    if num_correct_locations == expected_num_bugholes:
        print('\tYour bugholes_locations is correct')
    else:
        print('\tYour bugholes_locations is NOT correct') 
        print('\tThese locations are missing',locations_not_found)    
        print('\tThese locations are found',locations_found)   
except:
    print('\tYour num_bugholes is NOT correct.')
    print('\tPlease compare the bugholes_locations returned by your function')
    print('\against the expected answer')

