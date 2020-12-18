
from copy import copy, deepcopy
from collections import defaultdict, deque, Counter
from blist import *
from parse import compile

reg = compile("pos=<{},{},{}>, r={}")
s = input()
lines = []
while s != 'done':
    x,y,z,r = map(int, reg.parse(s))
    lines.append((x,y,z,r))
    s = input()
    
def run(lines):
    maxr = 0
    pts = []
    for (x,y,z,r) in lines:
        pts.append((x,y,z))
        for (a,b,c,d) in lines:
            if (a,b,c,d) == (x,y,z,r):
                continue
            pts.extend(inter(a,b,c,d,x,y,z,r))
            pts.extend(inter(x,y,z,r,a,b,c,d))
    minp = None
    mind = 100000000000
    maxi = 0
    print("Collect {} points".format(len(pts)))
    for (a,b,c) in pts:
        # print("Trying point", a, b, c)
        i = 0
        for (x,y,z,r) in lines:
            if dist(a,b,c,x,y,z) <= r:
                i += 1
        d = dist(0,0,0,a,b,c)
        if i > maxi or (i == maxi and d < mind):
            maxi = i
            mind = d
            minp = (a,b,c)
            print("Max Score", maxi, "for", minp, "at", mind)
    print("Final Max Score", maxi, "for", minp, "at", mind)
                
def inter(a,b,c,d,x,y,z,r):
    altps = [
        (a,b,c),
        (a+d,b,c),
        (a-d,b,c),
        (a,b+d,c),
        (a,b-d,c),
        (a,b,c+d),
        (a,b,c-d)
    ]
    ints = []
    for (e,f,g) in altps:
        if dist(e,f,g,x,y,z) <= r:
            ints.append((e,f,g))
    return ints
                
def dist(a,b,c,x,y,z):
    return abs(a-x) + abs(b-y) + abs(c-z)
        
run(lines)
