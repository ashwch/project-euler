"""
Author:Ashwini Chaudhary
Link:http://projecteuler.net/problem=11
lang:python
"""
from operator import mul
lis=[map(int,raw_input().split()) for _ in xrange(20)]
dic={'hor1':((1,0),(2,0),(3,0)),
     'ver1':((0,1),(0,2),(0,3)),
     'hor2':((-1,0),(-2,0),(-3,0)),
     'ver1':((0,-1),(0,-2),(0,-3)),
     'diag1':((1,1,),(2,2),(3,3)),
     'diag2':((1,-1),(2,-2),(3,-3)),
     'diag3':((-1,-1,),(-2,-2),(-3,-3)),
     'diag4':((-1,1),(-2,2),(-3,3))}

maxx=0
for i,x in enumerate(lis):
    for j,y in enumerate(x):
        for z in dic.values():
            if all(0<=i+a<20 and 0<=j+b<20 for a,b in z):
                maxx=max(maxx,y*reduce(mul,(lis[i+a][j+b] for a,b in z)))
print maxx
