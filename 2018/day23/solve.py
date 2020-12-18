
from copy import copy, deepcopy
from collections import defaultdict, deque, Counter
from blist import *
from parse import compile
from z3 import *

reg = compile("pos=<{},{},{}>, r={}")
s = input()
lines = []
while s != 'done':
    x,y,z,r = map(int, reg.parse(s))
    lines.append(((x,y,z),r))
    s = input()
    
def run(lines):
    x,y,z = (Int('x'), Int('y'), Int('z'))
    orig = (x,y,z)
    cost = 0
    for p,r in lines:
        cost += If(z3_dist(orig, p) <= r, 1, 0)
    opt = Optimize()
    opt.maximize(cost)
    opt.minimize(z3_dist((0,0,0), orig))
    opt.check()
    model = opt.model()
    x,y,z = model[x].as_long(), model[y].as_long(), model[z].as_long()
    print(model)
    print(x,y,z, dist((0,0,0), (x,y,z)))
    cost = 0
    orig = (x,y,z)
    for p,r in lines:
        if dist(orig, p) <= r:
            cost += 1
    print("Total:", cost)
    
def dist(p1, p2):
    (a,b,c), (x,y,z) = p1, p2
    return abs(a-x) + abs(b-y) + abs(c-z)
    
def z3_abs(x):
    return If(x >= 0, x, -x)
                
def z3_dist(p1, p2):
    (a,b,c), (x,y,z) = p1, p2
    return z3_abs(a-x) + z3_abs(b-y) + z3_abs(c-z)

        
run(lines)
