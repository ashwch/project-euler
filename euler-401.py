"""
Author:Ashwini Chaudhary
Link:http://projecteuler.net/problem=401
lang:python
"""
ans=0
for i in range(4,(10**4)+1):
    #print (i,end=" ")
    summ=1
    if i%2==0:
        skip=1
        summ+=4
    else:
        skip=2
    for div in range(3,(i//2)+1,skip):
        if i%div==0:
            summ+=div**2
    summ+=i**2
    #print (summ)
    ans+=summ
print ((ans+1+5+10)%10**9)
