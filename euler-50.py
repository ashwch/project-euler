"""
Author:Ashwini Chaudhary
Link:http://projecteuler.net/problem=50
lang:python
"""
def primes(n):
    if n<=2:
        return []
    sieve=[True]*(n+1)
    for x in range(3,int(n**0.5)+1,2):
        for y in range(3,(n//x)+1,2):
            sieve[(x*y)]=False
         
    return [2]+[i for i in range(3,n,2) if sieve[i]]
maxx=0
p=primes(1000000)
ps=set(p)
for i,x in enumerate(p):
    summ=x
    j=i+1
    prev=summ
    while summ<=1000000 and j<len(p):
        nex=p[j]
        summ+=nex
        if summ in ps:
            if j-i+1 > maxx:
                maxx=j-i+1
                num=summ
        j+=1       
print num
