"""
Author:Ashwini Chaudhary
Link:http://projecteuler.net/problem=30
lang:python
"""
summ=0
for x in xrange(2,6*(9**5)):
    st=str(x)
    if sum(int(i)**5 for i in st)==x:
        summ+=x
print summ
