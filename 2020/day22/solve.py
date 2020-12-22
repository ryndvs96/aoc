from parse import compile
from copy import copy, deepcopy
from collections import defaultdict, Counter, deque
from blist import *
import itertools
import math
import sys
# sys.setrecursionlimit(10000)

s = input()
s = input()
p1 = []
while s != '':
    p1.append(int(s))
    s = input()

s = input()
s = input()
p2 = []
while s != 'done':
    p2.append(int(s))
    s = input()

p1,p2 = blist(p1), blist(p2)
op1,op2 = deepcopy(p1), deepcopy(p2)

def key(p1,p2):
    s1 = ','.join([str(p) for p in p1])
    s2 = ','.join([str(p) for p in p2])
    return hash(s1 + ':' + s2)

rounds = set()
print(rounds)

games = {}
def roundl(p1,p2,depth=0):
    gk = key(p1,p2)
    if gk in games:
        return games[gk]
    
    while len(p1) > 0 and len(p2) > 0:
        k = key(p1,p2)
        if k in rounds:
            games[gk] = (1, p1, p2)
            print('{}player {} won game {}'.format('  '*depth,1,len(games)))
            return (1, p1, p2)
        else:
            rounds.add(k)
        t1 = p1.pop(0)
        t2 = p2.pop(0)
        # print('player 1 deck {}\nplayer 2 deck {}'.format(p1,p2))
        # print('player 1 plays {}\nplayer 2 plays {}'.format(t1,t2))
        
        if t1 <= len(p1) and t2 <= len(p2):
            cp1 = deepcopy(p1)
            cp2 = deepcopy(p2)
            # print('starting subgame')
            (w,cp1,cp2) = roundl(cp1,cp2,depth+1)
            c1,c2 = t1,t2
            if w == 1:
                p1.append(c1)
                p1.append(c2)
            elif w == 2:
                p2.append(c2)
                p2.append(c1)    
        else:
            c1,c2 = t1,t2
            if c1 > c2:
                p1.append(c1)
                p1.append(c2)
            elif c2 > c1:
                p2.append(c2)
                p2.append(c1)
        
    if len(p1) > 0:
        p = 1
        dp = p1
    else:
        p = 2  
        dp = p2  
    games[gk] = (p,p1,p2)
    # if len(games) % 1000 == 0:
    print('{}player {} won game {}'.format('  '*depth,p,len(games)))
    return (p,p1,p2)
    
(w,p1,p2) = roundl(p1,p2)

def score(p):
    n = len(p)
    tot = 0
    for i in range(len(p)):
        c = i + 1
        tot += c * p[n-i-1]
    return tot

if w == 1:
    print(score(p1))
else:
    print(score(p2))
    
    


    
 

                
            



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # hello