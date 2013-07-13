"""
Author:Ashwini Chaudhary
Link:http://projecteuler.net/problem=29
lang:python
"""
import time
t_0 = time.clock()
print len(set(i**j for i in xrange(2,101) for j in xrange(2,101)))
t_1 = time.clock()
print("This took {0:0.3f}s to compute.".format(t_1-t_0))

