#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 22T3 Assignment 2

Template file for find_edge_after()

TimeLine:
1. Coding started and finished on 16 Nov 2022
2. Final editing and commenting done on 18 Nov 2022

@author: Raghav Agarwal
zId: z5394767

So this function is basically being used to find the
upper index or the last index for when the true or the
given bughole ends. We are finding the index of the false
that occurs for the first time after the last true. 
We are using try and except blocks as if the last false 
is also the last value that occurs in the given array then
there is no last false, hence we are returning the length 
of the array.
"""

import numpy as np

def find_edge_after(array_bool, start_index):
    # try block runs if there is a false present at the end of the last
    # true in the given bughole
    try:
        # This is basically giving the index of the first false that occurs
        # after the start index which is the index of one of the trues
        # in the bughole
        return array_bool.tolist().index(False, start_index)

    # else ValueError is thrown meaning no false present at the end of the
    # given array hence length of the array is returned meaning the bughole
    # might be on the bottom of right edge depending the situation.
    except ValueError:
        return len(array_bool.tolist())

    # try:
    #     index_arr = np.where(np.logical_or(array_bool == True, array_bool == False))
    #     index_arr = index_arr[0].tolist()[start_index:]
    #     new_arr = array_bool[start_index:].tolist()
    #     return index_arr[new_arr.index(False)]
    # except ValueError:
    #     return len(array_bool)