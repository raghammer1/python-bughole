#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 22T3 Assignment 2 

Template file for remove_a_bughole()

TimeLine:
1. Coding started and finished on 16 Nov 2022
2. Final editing and commenting done on 18 Nov 2022

@author: Raghav Agarwal
zId: z5394767

This is a very simple code in which I am basically selecting
the part of the 2d array according to the given parameters
and then assigning that part of the array as false and hence
removing the bughole that was present in that part of the 2d
array. 
"""
import numpy as np


def remove_a_bughole(
    concrete_bool,
    bughole_axis_0_lower,
    bughole_axis_0_upper,
    bughole_axis_1_lower,
    bughole_axis_1_upper,
):
    concrete_bool[
        bughole_axis_0_lower:bughole_axis_0_upper,
        bughole_axis_1_lower:bughole_axis_1_upper,
    ] = False
    return concrete_bool

    # for i in range(bughole_axis_0_lower, bughole_axis_0_upper):
    #     for j in range(bughole_axis_1_lower, bughole_axis_1_upper):
    #         concrete_bool[i, j] = False
    # return concrete_bool
