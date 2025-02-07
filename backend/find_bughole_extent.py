#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 22T3 Assignment 2

Template file for find_bughole_extend()

TimeLine:
1. Coding started and finished on 16 Nov 2022
2. Final editing and commenting done on 18 Nov 2022

@author: Raghav Agarwal
zId: z5394767

In this file we are finding the location of the bugholes
and so we are just calling the functions created in the
find_edge_before and find_edge_after files.
to find bughole_axis_0_lower we are calling the find_edge_before
function and giving it the reversed row so that it can find
the first true from the back and then for bughole_axis_0_upper I
have called the find_edge_after function with a reversed column
then for bughole_axis_1_lower I am calling the find_edge_before
with straight row and then find_edge_after with straight column
again for bughole_axis_1_upper.
I have also provided a commented pseudocode for better understanding.
"""

from find_edge_before import find_edge_before as before
from find_edge_after import find_edge_after as after


def find_bughole_extent(concrete_bool, index_0, index_1):
    return [
        before(concrete_bool[:, index_1], index_0),
        after(concrete_bool[:, index_1], index_0),
        before(concrete_bool[index_0], index_1),
        after(concrete_bool[index_0], index_1),
    ]

    #  PSEUDOCODE FOR ALL THE FUNCTIONS ABOVE
    # print(len(concrete_bool[0]), len(concrete_bool))
    # for i in range(index_0, -3, -1):
    #     if i < 0:
    #         bughole_axis_0_lower = 0
    #         break
    #     if concrete_bool[i, index_1] == False:
    #         bughole_axis_0_lower = i + 1
    #         break
    # for j in range(index_1, -3, -1):
    #     if j < 0:
    #         bughole_axis_1_lower = 0
    #         break
    #     if concrete_bool[index_0, j] == False:
    #         bughole_axis_1_lower = j + 1
    #         break
    # for i in range(index_0, len(concrete_bool) + 1):
    #     if i == len(concrete_bool):
    #         bughole_axis_0_upper = i
    #         break
    #     if concrete_bool[i, index_1] == False:
    #         bughole_axis_0_upper = i
    #         break
    # for j in range(index_1, len(concrete_bool[0]) + 1):
    #     if j == len(concrete_bool[0]):
    #         bughole_axis_1_upper = j
    #         break
    #     if concrete_bool[index_0, j] == False:
    #         bughole_axis_1_upper = j
    #         break
