
from copy import copy, deepcopy
from collections import defaultdict, deque, Counter
from blist import *
from parse import compile
import sys
# sys.setrecursionlimit(10000)

# regx = compile("x={}, y={}..{}")
# regy = compile("y={}, x={}..{}")

s = input()
grid = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: '.'))))
x = 0
actives = set()
while s != 'done':
    ys = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: '.')))
    y = 0
    for w in list(s):
        zs = defaultdict(lambda: defaultdict(lambda: '.'))
        ws = defaultdict(lambda: '.')
        ws[0] = w
        zs[0] = ws
        if w == '#':
            actives.add((x,y,0,0))
        ys[y] = zs
        y += 1
    grid[x] = ys
    x += 1
    s = input()
    
def neighbors(grid, x, y, z, w):
    n = []
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                for l in range(w - 1, w + 2):
                    if x == i and y == j and z == k and l == w:
                        continue
                    else:
                        n.append((i,j,k,l))
    return n
    
def is_active(grid, x, y, z, w):
    return grid[x][y][z][w] == '#'

def is_actives(grid, n):
    tot = 0
    for (x,y,z,w) in n:
        if is_active(grid, x, y, z,w):
            tot += 1
    return tot

for i in range(6):
    new_state = deepcopy(grid)
    possibles = set()
    new_actives = deepcopy(actives)
    for (x,y,z,w) in actives:
        ns = neighbors(grid, x,y,z,w)
        for n in ns:
            possibles.add(n)
        ct = is_actives(grid, ns)
        if ct == 2 or ct == 3:
            continue
        else:
            new_state[x][y][z][w] = '.'
            new_actives.remove((x,y,z,w))
            
    for (x,y,z,w) in possibles:
        if not is_active(grid, x, y, z,w):
            ns = neighbors(grid, x,y,z,w)
            ct = is_actives(grid, ns)
            if ct == 3:
                new_state[x][y][z][w] = '#'
                new_actives.add((x,y,z,w))
    actives = new_actives
    grid = new_state
    
print(len(actives))
    












# for l in lines:
    
