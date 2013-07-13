primes=[2,3]
num=600851475143
import math
for x in range(4,int(math.sqrt(num)+1)):
    for y in primes:
        if x%y==0:
            break
    else:
        primes.append(x)

factors=[x for x in range(2,int(math.sqrt(num))+1) if num%x==0]
for x in reversed(factors):
    if x in primes:
        print x
        break
