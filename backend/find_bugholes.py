#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 22T3 Assignment 2

Template file for find_bugholes()

TimeLine:
1. Coding started and finished on 16 Nov 2022
2. Final editing and commenting done on 18 Nov 2022

@author: Raghav Agarwal
zId: z5394767

So in this function we are first calling the calc_concrete_bool 
file to make the given concrete_image array into the boolean array
which is being called as the concrete_bool array in this function.
Then we are going through this concrete_bool array and looking 
for the first time that a true value occurs. If a true value occurs
then that means we have found a bughole. Then we are calling 
find_bughole_extent file and finding the exact coordinates of the 
bughole. then we are adding these coordinates to the location_bugholes
array and also we are calling remove_a_bughole function file to clear
this bughole. We are also adding one value to the num_bugholes variable
so that at the end we also have the total amount of bugholes that we 
present in the given concrete_image. Finally, we are returning the 
variable num_bugholes and the newly created array location_bugholes.
"""

from calc_concrete_bool import calc_concrete_bool as calc
from find_bughole_extent import find_bughole_extent as extent
from remove_a_bughole import remove_a_bughole as remove


def find_bugholes(concrete_image, threshold):
    # creating the boolean array with the given image and threshold
    concrete_bool = calc(concrete_image, threshold)

    # defining the number of bugholes finder variable and the
    # location of bugholes array
    num_bugholes = 0
    location_bugholes = []

    # Starting the loop to find the bugholes
    i = 0
    while i < len(concrete_bool):
        j = 0
        while j < len(concrete_bool[i]):

            # If we find any value as true then we go in here
            if concrete_bool[i][j] == True:

                # We first call the find_bughole_extent func
                # to find the 4 coordinates of the bughole
                [
                    bughole_axis_0_lower,
                    bughole_axis_0_upper,
                    bughole_axis_1_lower,
                    bughole_axis_1_upper,
                ] = extent(concrete_bool, i, j)

                # As we have found the coordinates of the
                # bughole we now proceed on removing them
                concrete_bool = remove(
                    concrete_bool,
                    bughole_axis_0_lower,
                    bughole_axis_0_upper,
                    bughole_axis_1_lower,
                    bughole_axis_1_upper,
                )

                # We also append the 4 coordinates of the
                # bughole in our location_bugholes array
                location_bugholes.append(
                    [
                        bughole_axis_0_lower,
                        bughole_axis_0_upper,
                        bughole_axis_1_lower,
                        bughole_axis_1_upper,
                    ]
                )

                # Finally we add 1 to the count of the bugholes
                num_bugholes += 1

            j += 1
        i += 1

    return [num_bugholes, location_bugholes]

    # concrete_bool = calc(concrete_image, threshold)
    # bughole =  0
    # coord_bugholes = []
    # for i in range(0, len(concrete_bool)):
    #     for j in range(0, len(concrete_bool[i])):
    #         if concrete_bool[i][j] == True:
    #             bughole += 1
    #             [coord_1, coord_2, coord_3, coord_4] = extent(concrete_bool, i, j)
    #             coord_bugholes.append([coord_1, coord_2, coord_3, coord_4])
    #             concrete_bool = remove(concrete_bool, coord_1, coord_2, coord_3, coord_4)

    # return [bughole, coord_bugholes]