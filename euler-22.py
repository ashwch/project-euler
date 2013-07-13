"""
Author:Ashwini Chaudhary
Link:http://projecteuler.net/problem=22
lang:python
"""
from itertools import imap
from string import ascii_uppercase as au
dic={x:i for i,x in enumerate(au,1)}
with open("names.txt") as f:
    line=imap(lambda x:x.strip('"'),f.read().split(','))
    line=sorted(line)
    score=0
    print line[937]
    for i,name in enumerate(line,1):
        score+=i*sum(dic[x] for x in name)
print score
