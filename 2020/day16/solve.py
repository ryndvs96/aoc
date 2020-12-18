
from parse import compile
from copy import copy, deepcopy
from collections import defaultdict, Counter, deque
from blist import *
import random
import itertools
import math

# s = input()
# 
reg = compile("{}: {}-{} or {}-{}")
# f,v = reg.parse(s)

def in_range(m, c, val):
    x0, x1, x2, x3 = m[c]
    if val >= x0 and val <= x1:
        return True
    if val >= x2 and val <= x3:
        return True
    return False
    
def in_ranger(m, c, val):
    x0, x1, x2, x3 = m[c]
    if val >= x0 and val <= x1:
        return '{} <= {} <= {}'.format(x0, val, x1)
    if val >= x2 and val <= x3:
        return '{} <= {} <= {}'.format(x2, val, x3)
    return None
    
def valid_at_all(m, val):
    for k in m:
        if in_range(m, k, val):
            return k
    return None
    
def all_valid(m, vals, excluding=[]):
    for k in m:
        if k in excluding:
            continue
        valid = True
        for v in vals:
            valid = valid and in_range(m, k, v)
        if valid:
            return k
    return None
    
validfork = {}
def valid_for_k(m, k, vals, i):
    if k in validfork:
        if i in validfork[k]:
            return validfork[k][i]
    valid = True
    for v in vals:
        valid = valid and in_range(m, k, v)
    if k in validfork:
        validfork[k][i] = valid
    else:
        validfork[k] = {}
        validfork[k][i] = valid
    return valid

s = input()
rules = {}
lines = []
while s != '':
    c, x0, x1, x2, x3 = reg.parse(s)
    x0, x1, x2, x3 = map(int, (x0, x1, x2, x3))
    rules[c] = (x0, x1, x2, x3)
    lines.append(s)
    s = input()
    
s = input()
my_ticket = list(map(int, input().split(",")))
    
s = input()
s = input()
s = input()
nearby_tickets = []
while s != 'done':
    nearby_tickets.append(list(map(int, s.split(","))))
    s = input()

tot = 0
valid_ticks = []
for n in nearby_tickets:
    valid = True
    for v in n:
        ks = valid_at_all(rules, v)
        if ks is None:
            print('{} is not a valid ticket because {} does not fit anywhere'.format(n, v))
            valid = False
            break
    if not valid:
        continue
    valid_ticks.append(n)
valid_ticks.append(my_ticket)

validforcol = {}
cols = {}
for i in range(len(valid_ticks[0])):
    col = []
    for n in valid_ticks:
        col.append(n[i])
    cols[i] = col
    valids = {}
    for k in rules:
        valids[k] = valid_for_k(rules, k, col, i)
    
    validforcol[i] = valids

dont_repeat = defaultdict(set)
avail = set([k for k in rules])

def solve(rules, used, ticks, i=0):
    if i == len(ticks[0]):
        return used
    
    col = cols[i]

    poss = [k for k in avail]
    random.shuffle(poss)
    for k in poss:
        if used[k] == -1 and k not in dont_repeat[i]:
            if not validforcol[i][k]:
                dont_repeat[i].add(k)
                continue
            else: #1065457657417 #1310022201749
                print(' '*(i+1), k, 'for', i)
                used[k] = i
                avail.remove(k)
                v = solve(rules, used, ticks, i + 1)
                if v is None:
                    used[k] = -1
                    avail.add(k)
                    continue
                else:
                    return v
    return None

used = {}
for k in rules:
    used[k] = -1
    
v = solve(rules, used, valid_ticks)

for k in v:
    i = v[k]
    valid = True
    print(k, rules[k])
    for n in valid_ticks:
        s = in_ranger(rules, k, n[i])
        valid = valid and (s is not None)
        if not valid:
            print(k, 'at', i, 'is not valid for', n[i],';', n)
        else:
            print(k, 'at', i, 'is valid for', s,';', n)
    if valid:
        print(k, 'at', i, 'is valid for all rows')
print(rules)
print(v)
tot = 1
for k in v:
    if k.startswith('departure'):
        tot *= my_ticket[v[k]]
    
print(tot)
        
    # 0: 79,
    # 1: 149,
    # 2: 97,
    # 3: 163,
    # 4: 59,
    # 5: 151,
    # 6: 101,
    # 7: 89,
    # 8: 173,
    # 9: 139,
    # 10: 167,
    # 11: 61,
    # 12: 73,
    # 13: 71,
    # 14: 137,
    # 15: 53,
    # 16: 83,
    # 17: 157,
    # 18: 131,
    # 19: 67
    
    # 2092162605341
    # 2397587803201
    # 1359142130477
    # 680273730571
    # 692559507931
    
    
    
    
    
    
    
    
    # do something