#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
utils.py

Common funs for the algorithms solving the closest coordinates puzzle.

@author:  Luis Martin Gil
@contact: martingil.luis@gmail.com
@website: www.luismartingil.com
@github: https://github.com/luismartingil
'''

MIN = -65000
MAX = 65000

def calculate_dist ((x0,y0),(x1,y1)):
    """ Helper function to calculate the 
    distance between two coordinates"""
    ret = (abs(x0-x1)**2 + abs(y0-y1)**2)**(0.5)
    return ret
