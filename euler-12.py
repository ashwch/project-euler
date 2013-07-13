"""
Author:Ashwini Chaudhary
Link:http://projecteuler.net/problem=12
lang:python
"""
import sys
s=2
while True:
    num=sum(xrange(1,s))
    count=0
    sqrt=num**0.5
    for i in xrange(2,int(sqrt)):
        if count>500:
            print num
            sys.exit(0)
        if num%i==0:
            count+=2
    if sqrt ==int(sqrt):
        count+=2
    if count>500:
        print num
        sys.exit(0)
    s+=2
