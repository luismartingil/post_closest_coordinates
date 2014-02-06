#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
algorithm02.py

Another solution to the closest coordinates puzzle.

@author:  Luis Martin Gil
@contact: martingil.luis@gmail.com
@website: www.luismartingil.com
@github: https://github.com/luismartingil
'''

from utils import calculate_dist, MIN, MAX

class CoordKey(object):
    """ Stores a given coordinates key """
    elem1, elem2 = None, None
    def __init__(self, elem1, elem2):
        self.elem1 = elem1
        self.elem2 = elem2
    def unpack(self):
        return self.elem1, self.elem2

def algorithm02(array, iterations=None):
    """ Receives a list of integers pairs in the range [-65000, 65000]
    returns the two closest pairs.
    PRE. len(array) > 1
    PRE. for all items in array | items are (x,y) | x
    @TODO. Raise exception when PREs not apply
    """
    def encode_key(item, item_tmp):
        tmp = sorted([tmp1, tmp2])
        ret = '%s;%s' % (tmp[0], tmp[1])
        return ret
    def decode_key(key):
        tmp1, tmp2 = key.split(';')
        return tmp1, tmp2
    hist_dict = {}
    for item in array:
        for item_tmp in array:
            key = CoordKey(item, item_tmp)
            if not hist_dict.has_key(key):
                hist_dict[key] = calculate_dist(item, item_tmp)
        # end for
    # end for
    dist_min = min(hist_dict.values())
    for key, value in hist_dict.iteritems():
        if value <= dist_min:
            elem1, elem2 = key.unpack()
    # end for
    return [elem1, elem2]
