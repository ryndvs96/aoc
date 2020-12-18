
import numpy as np
import random as r

reg = compile("pos=<{},{},{}>, r={}")
s = input()
lines = []
while s != 'done':
    x,y,z,r = map(int, reg.parse(s))
    lines.append(np.asarray([x,y,z]),r)
    s = input()
    
def run(lines):
    gd(lines)
    
def gd(lines):
    w = init()
    # for (p,r) in lines:
    
def init():
    w = [0,0,0]
    w[0] = r.random(minx, maxx)
    w[1] = r.random(miny, maxy)
    w[2] = r.random(minz, maxz)
    return np.asarray(w)
    
def dist(p1, p2):
    (a,b,c), (x,y,z) = p1, p2
    return abs(a-x) + abs(b-y) + abs(c-z)
        
minx, maxx = 0, 0
miny, maxy = 0, 0
minz, maxz = 0, 0
for (arr,r) in lines:
    x,y,z = arr
    minx, maxx = min(x,minx), max(x,maxx)
    miny, maxy = min(y,miny), max(y,maxy)
    minz, maxz = min(z,minz), max(z,maxz)
print(minx, maxx)
print(miny, maxy)
print(minz, maxz)
        
# run(lines)
