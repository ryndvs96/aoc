from copy import copy, deepcopy
from collections import defaultdict, deque, Counter
from blist import *
from parse import compile
import sys
# sys.setrecursionlimit(10000)

# regx = compile("x={}, y={}..{}")
# regy = compile("y={}, x={}..{}")

s = input()
lines = []
while s != 'done':
    lines.append(s.replace(' ', ''))
    s = input()
    
def eval(expr):
    if len(expr) == 1:
        tot = expr[0]
        # print('evaluating {} = {}'.format(expr, tot))
        return tot
    
    tot = None
    for i, c in enumerate(expr):
        if c == '*':
            tot = eval(expr[0:i]) * eval(expr[i+1:])
            
    if tot is None:
        for i, c in enumerate(expr):
            if c == '+':
                tot = eval(expr[0:i]) + eval(expr[i+1:])
    
    print('evaluating {} = {}'.format(expr, tot))
    return tot
    
def resolve(line):
    expr = []
    curr = ''
    in_paren = 0
    for c in line:
        if c == '(':
            if in_paren >= 1:
                curr += c
            in_paren += 1
            
            # do stuff
        elif c == ')':
            in_paren -= 1
            if in_paren >= 1:
                curr += c
            if in_paren == 0:
                expr.append(resolve(curr))
                curr = ''
        else:
            if in_paren > 0:
                curr += c
            else:
                if c == '*' or c == '+':
                    expr.append(c)
                else:
                    expr.append(int(c))
    return eval(expr)

tot = 0
for l in lines:
    tot += resolve(l)
print(tot)
    
    
# 10 participants, kev 1 on 10 days, ryd 2 on 10 days
# kev = 10*2*10 = 200
# ryd =  9*2*10 = 180
# reduce to 2 participants
# kev = 2*2*10 = 40
# ryd = 1*2*10 = 20
    
    
    
    
    
    
    
    
    
    
    
    # hello