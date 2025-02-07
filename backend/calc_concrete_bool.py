#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 22T3 Assignment 2

Template file for calc_concrete_bool()

TimeLine:
1. Coding started and finished on 16 Nov 2022
2. Final editing and commenting done on 18 Nov 2022

@author: Raghav Agarwal
zId: z5394767

This function is basically modifing an already given
array which is the concrete_image which is a numbers
array and we are checking every value in this array
with the threshhold and if the value is less than the
threshhold then we are setting it to true else false,
hence creating a new array of bools which is called as
concrete_bool and returning it.
"""

import numpy as np


def calc_concrete_bool(concrete_image, threshold):
    return np.array(concrete_image < threshold)
    # return np.where(concrete_image < threshold, True, False)
