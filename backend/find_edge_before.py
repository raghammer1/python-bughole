#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 22T3 Assignment 2

Template file for find_edge_before()

TimeLine:
1. Coding started and finished on 16 Nov 2022
2. Final editing and commenting done on 18 Nov 2022

@author: Raghav Agarwal
zId: z5394767

So in this function first we have used numpy.where which is giving us
as index array which is equivalent in length to the array_bool.
We are given a start index which is telling us the location of one
true in the array_bool we have to find out where the true array starts.
Hence to find this I have first created the index_arr then I have spliced
the index_arr and the array_bool into a smaller array which only goes up
and until the start_index. Then I find the first time a false value occurs
in the newly created array_bool_spl_arr and use that index in the index_arr
which finally gives me the index of the false that occurs before the true in
the given array, then I add 1 to that so that it gives me the index of the
first true.
I have also created a try and except block as there could be a situation when
there is no false value in the array_bool_spl_arr because trues start at the
beginning of the array and hence a ValueError can be thrown which then gives
the return value of 0.
"""

from asyncio.format_helpers import _format_callback_source
import numpy as np


def find_edge_before(array_bool, start_index):

    # If there is atleast one false before the true value start then this will be run
    try:
        # creating the index_array
        index_arr = np.where(np.logical_or(array_bool == True, array_bool == False))
        index_arr = index_arr[0].tolist()

        # only taking the part of index_arr from starting to index of the true given
        # also flipping it
        index_arr = np.flipud(index_arr[:start_index])
        index_arr = index_arr.tolist()

        # only taking the part of array_bool from starting to index of the true given
        # also flipping it
        array_bool_spl_arr = np.flipud(array_bool[:start_index])
        array_bool_spl_arr = array_bool_spl_arr.tolist()

        # finding index of first false in the flipped array_bool_spl_arr then
        # putting that index in flipped index_arr to find the actual index of the
        # false before first true and finally adding 1 to give the index of that true
        return index_arr[array_bool_spl_arr.index(False)] + 1

    # if there is no false before the first true then this block is run
    except ValueError:
        return 0

    # if array_bool[start_index] != False:
    #     return find_edge_before(array_bool, start_index-1)
    # else:
    #     return start_index + 1