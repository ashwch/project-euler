"""
Author:Ashwini Chaudhary
Link:http://projecteuler.net/problem=56
lang:python
"""
maxx=0
for a in xrange(1,101):
    for b in xrange(1,101):
        strs=str(a**b)
        maxx=max(maxx,sum(int(x) for x in strs))
print maxx        
