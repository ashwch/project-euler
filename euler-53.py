"""
Author:Ashwini Chaudhary
Link:http://projecteuler.net/problem=53
lang:python
"""
from math import factorial as fc
def calc(n,r):
    return fc(n)/(fc(r)*fc(n-r))
count=0
for n in xrange(23,101):
    for r in xrange(0,n+1):
        if calc(n,r)>10**6:
            count+=1
print count
