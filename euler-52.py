"""
Author:Ashwini Chaudhary
Link:http://projecteuler.net/problem=52
lang:python
"""
from collections import Counter as c
i=1
while True:
    s=c(str(i))
    if s.most_common(2):
        lis=[c(str(j*i)) for j in xrange(2,7)]
        if all(x==s for x in lis):
            print i
            break
    i+=1
