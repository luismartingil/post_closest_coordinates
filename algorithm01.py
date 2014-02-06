#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
algorithm01.py

First solution to the closest coordinates puzzle.

@author:  Luis Martin Gil
@contact: martingil.luis@gmail.com
@website: www.luismartingil.com
@github: https://github.com/luismartingil
'''

from utils import calculate_dist, MIN, MAX

def algorithm01(array, iterations=None):
    """ Receives a list of integers pairs in the range [-65000, 65000]
    returns the two closest pairs.
    PRE. len(array) > 1
    PRE. for all items in array | items are (x,y) | x
    @TODO. Raise exception when PREs not apply
    """
    elem1, elem2 = None, None
    dist_min = calculate_dist((MIN, MIN),(MAX, MAX))
    for item in array:
        for item_tmp in array:
            if item_tmp is not item:
                dist_tmp = calculate_dist(item, item_tmp)
                if dist_tmp <= dist_min:
                    elem1, elem2 = item, item_tmp
                    dist_min = dist_tmp
        # end for
    # end for
    return [elem1, elem2]
