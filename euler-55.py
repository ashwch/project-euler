"""
Author:Ashwini Chaudhary
Link:http://projecteuler.net/problem=55
lang:python
"""
def lych(x):
    x=str(int(x)+int(x[::-1]))
    for _ in xrange(51):
        if x==x[::-1]:
            return False
        x=str(int(x)+int(x[::-1]))
    if x==x[::-1]:
        return False
    return True

print sum(lych(str(x)) for x in xrange(1,10001))

