from parse import compile
from copy import copy, deepcopy
from collections import defaultdict, Counter, deque
from blist import *
import itertools
import math
import sys
# sys.setrecursionlimit(10000)

s = input()
lines = []
while s != 'done':
    lines.append(s)
    s = input()

allergens = {}
foods = []
for l in lines:
    ingredsstr = l.split(' ')
    ingreds = set()
    allers = set()
    inallergs = False
    for i in ingredsstr:
        if inallergs:
            aller = i.strip(')').strip(',')
            allers.add(aller)
        else:
            if i == '(contains':
                inallergs = True
            else:
                ingreds.add(i)
    foods.append((ingreds, allers))
    for a in allers:
        if a in allergens:
            allergens[a] = allergens[a] & ingreds
        else:
            allergens[a] = ingreds
            
all_poss = set()
for a in allergens:
    all_poss = all_poss | allergens[a]
    
tot = 0
for (ins, als) in foods:
    for ing in ins:
        if ing not in all_poss:
            tot += 1
print(tot)

final_alls = {}
left = set()
for a in allergens:
    left.add(a)

while len(left) > 0:
    print(left)
    to_remove = set()
    for a in left:
        if len(allergens[a]) == 1:
            t = allergens[a].pop()
            final_alls[a] = t
            to_remove.add(a)
            for k in allergens:
                if t in allergens[k]:
                    allergens[k].remove(t)
    for a in to_remove:
        left.remove(a)
                    
finals = [k for k in final_alls]
finals.sort()
str = []
for k in finals:
    str.append(final_alls[k])
    
print(','.join(str))


    
 

                
            



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # hello