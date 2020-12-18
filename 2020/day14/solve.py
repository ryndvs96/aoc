
from parse import compile
from copy import copy, deepcopy
from collections import defaultdict, Counter, deque
from blist import *
import itertools
import math

maskreg = compile("mask = {}")
memreg = compile("mem[{}] = {}")
# read in each line as value
s = input()
lines = []
while s != 'done':
    if s.startswith('mask'):
        mask = s.split(" ")[2]
    else:
        loc, val = memreg.parse(s)
        lines.append((str(mask), int(loc), int(val)))
    s = input()

def maskstr(mask, val):
    xmask = mask.replace('0', '0').replace('1', '0').replace('X', '1')
    nmask = mask.replace('X', '0')
    return (int(xmask, 2) & val) | int(nmask, 2)
    
# 
# def maskstr(mask, val):
#     res = ''
#     offset = len(mask) - len(val)
#     for i in range(len(mask)):
#         if i < offset:
#             if mask[i] == 'X':
#                 res += 'X'
#             elif mask[i] == '1':
#                 res += mask[i]
#             else:
#                 res += '0'
#         else:
#             m = mask[i]
#             if m == 'X':
#                 res += 'X' 
#             elif m == '1':
#                 res += '1'
#             else:
#                 res += val[i - offset]
#     return res
            
def iterx(val):
    vals = []
    ct = 0
    for v in val:
        if v == 'X':
            ct += 1
    
    #XX
    #0, 1, 2, 3
    if ct == 0:
        return [int(val, 2)]
    for b in range(0, 2**ct): 
        bins = "{0:b}".format(b)
        bi = 0
        offset = ct - len(bins)
        cp = ''
        for v in val:
                
            if v == 'X':
                if bi < offset:
                    cp += '0'
                else:
                    cp += bins[offset - bi]
                bi += 1
            else:
                cp += v
        vals.append(int(cp, 2))
    return vals

    
mem = {}
for (mask, loc, val) in lines:
    # v = "{0:b}".format(loc)
    fixed = maskstr(mask, val)
    # vals = iterx(fixed)
    mem[loc] = fixed
    # for v in vals:
    #     mem[v] = val

tot = 0
for k in mem:
    tot += mem[k]
    

print(tot)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # hello