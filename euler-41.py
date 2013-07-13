"""
Author:Ashwini Chaudhary
Link:http://projecteuler.net/problem=41
lang:python
"""
def primes(n):
    if n<=2:
        yield []
    sieve=[True for _ in range(n+1)]
    for x in range(3,int(n**0.5)+1,2):
        for y in range(3,(n//x)+1,2):
            sieve[(x*y)]=False
         
    for i in range(n-1,3,-2):
        if sieve[i]:yield i
              
for x in primes(987645203):
    x=str(x)
    if len(x)==len(set(x)):
        print (x)
        break
