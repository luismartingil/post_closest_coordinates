#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
closest_coordinates.py

closest coordinates puzzle.

@author:  Luis Martin Gil
@contact: martingil.luis@gmail.com
@website: www.luismartingil.com
@github: https://github.com/luismartingil
'''

import unittest
import random
import timeit
import pprint

from algorithm01 import algorithm01
from algorithm02 import algorithm02
from utils import MIN, MAX

# Some time-measurements params
accuracy = 100
#array_sizes = [2, 50, 100, 150, 200]
array_sizes = [500]
algs = [algorithm01, algorithm02]

# Lets work on some unittests
tests = [
    ([(MIN,MIN), (MAX,MAX)], [(MIN,MIN), (MAX,MAX)]),
    ([(MAX,MAX), (MIN,MIN)], [(MIN,MIN), (MAX,MAX)]),
    ([(15,15), (2,3)], [(15,15), (2,3)]),
    ([(2,3), (5,5)], [(5,5), (2,3)]),
    ([(0,0), (1,1), (7,8), (12, 12), (2,3), (5,5)], [(0,0), (1,1)]),
    ([(21,13), (2,3), (51,5), (4,8)], [(2,3), (4,8)]),
    ([(14,13), (2,3), (5,6), (33, 12), (44, 2)], [(5,6), (2,3)]),
    ([(0, 0), (1, 20), (5, 2)], [(0, 0), (5, 2)]),
    ([(-10, 10), (1, 5), (4, 3)], [(1, 5), (4, 3)]),
    ]

class Test_Apply(unittest.TestCase):
    pass

def test_Function(t, expected, algorithm):
    def test(self):
        self.assertEquals(set(algorithm(t)),
                          set(expected))
    return test

def attach(where, fun, l, algorithm):
    """ Attaches tests. DRY function helper. """
    for a, b in [("test-%s-%.6i" % (algorithm.__name__, 
                                    l.index(x)), 
                  fun(x[0], x[1], algorithm)) for x in l]:
        setattr(where, a, b)

def suite():
    test_suite = unittest.TestSuite()
    for algorithm in algs:
        attach(Test_Apply,
               test_Function,            
               tests,
               algorithm)
    test_suite.addTest(unittest.makeSuite(Test_Apply))
    return test_suite
    
if __name__ == '__main__':

    test = True
    bench = True

    if test:
        mySuit=suite()
        runner=unittest.TextTestRunner(verbosity=2)
        runner.run(mySuit)
        print 'Should be %i tests' % (len(tests))
        print '~' * 60

    if bench:
        result_dict = {}
        for size in array_sizes:
            array = [(random.randint(MIN, MAX),
                      random.randint(MIN, MAX)) \
                         for _ in range(0, size)]
            for algorithm in algs:
                algorithm_name = algorithm.__name__
                t = timeit.timeit(algorithm_name + '(%s)' % array,
                                  setup="from __main__ import %s" % algorithm_name,
                                  number=accuracy)
                if not result_dict.has_key(size):
                    result_dict[size] = {}
                result_dict[size][algorithm_name] = t
        # end for
        pprint.pprint(result_dict)


# test-algorithm01-000000 (__main__.Test_Apply) ... ok
# test-algorithm01-000001 (__main__.Test_Apply) ... ok
# test-algorithm01-000002 (__main__.Test_Apply) ... ok
# test-algorithm01-000003 (__main__.Test_Apply) ... ok
# test-algorithm01-000004 (__main__.Test_Apply) ... ok
# test-algorithm01-000005 (__main__.Test_Apply) ... ok
# test-algorithm01-000006 (__main__.Test_Apply) ... ok
# test-algorithm01-000007 (__main__.Test_Apply) ... ok
# test-algorithm01-000008 (__main__.Test_Apply) ... ok
# test-algorithm02-000000 (__main__.Test_Apply) ... FAIL
# test-algorithm02-000001 (__main__.Test_Apply) ... FAIL
# test-algorithm02-000002 (__main__.Test_Apply) ... FAIL
# test-algorithm02-000003 (__main__.Test_Apply) ... FAIL
# test-algorithm02-000004 (__main__.Test_Apply) ... FAIL
# test-algorithm02-000005 (__main__.Test_Apply) ... FAIL
# test-algorithm02-000006 (__main__.Test_Apply) ... FAIL
# test-algorithm02-000007 (__main__.Test_Apply) ... FAIL
# test-algorithm02-000008 (__main__.Test_Apply) ... FAIL
