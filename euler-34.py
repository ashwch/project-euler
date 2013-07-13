"""
Author:Ashwini Chaudhary
Link:http://projecteuler.net/problem=34
lang:python
"""
from math import factorial as fc
summ=0
for x in xrange(11,999999):
    st=str(x)
    if x==sum(fc(int(i)) for i in st):
        summ+=x
print summ
