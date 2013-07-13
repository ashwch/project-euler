lis=range(10)
from itertools import permutations, islice
lis=(int("".join(map(str,x))) for x in permutations(lis,10))
print list(sorted(islice(lis,999998,999999)))
