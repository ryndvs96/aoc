from parse import compile
from copy import copy, deepcopy
from collections import defaultdict, Counter, deque
from blist import *
import itertools
import math
import sys
# sys.setrecursionlimit(10000)

s = ''
tiles = {}
while s != 'done':
    s = input()
    tile = int(s.strip(':').split(' ')[1])
    s = input()
    grid = []
    while s != '' and s != 'done':
        grid.append(list(s))
        s = input()
    tiles[tile] = grid
    
def rotate1(grid, times=1):
    if times > 1:
        grid = rotate1(grid, times - 1)
    n,m = len(grid), len(grid[0])
    newgrid = deepcopy(grid)
    for i in range(n):
        for j in range(m):
            newi = j
            newj = m - i - 1
            newgrid[newi][newj] = grid[i][j] 
    return newgrid
    
def rotate2(grid):
    return rotate1(grid, 2)
    
def rotate3(grid):
    return rotate1(grid, 3)
    
def flip_vert(grid):
    n,m = len(grid), len(grid[0])
    newgrid = deepcopy(grid)
    for i in range(n):
        for j in range(m):
            newi = n - i - 1
            newj = j
            newgrid[newi][newj] = grid[i][j]
    return newgrid
            
def flip_hor(grid):
    n,m = len(grid), len(grid[0])
    newgrid = deepcopy(grid)
    for i in range(n):
        for j in range(m):
            c = grid[i][j]
            newi = i
            newj = m - j - 1
            newgrid[newi][newj] = c 
    return newgrid
    
def flip_both(grid):
    return flip_hor(flip_vert(grid))
    
rots = [
    ('rot_none', lambda x: x),
    ('rot1', rotate1),
    ('rot2', rotate2),
    ('rot3', rotate3)
]
    
flips = [
    ('flip_none', lambda x: x), 
    ('fliph', flip_hor), 
    ('flipv', flip_vert), 
    ('flip_both', flip_both)
]

def unique_op_pairs():
    op_results = {}
    # determine which pairs of ops result in the same value
    test_grid = [
        [str(i*len(grid[i]) + j) for j in range(len(grid[i]))] 
        for i in range(len(grid))
    ]
    for (r,rf) in rots:
        for (f,ff) in flips:
            res = rf(ff(test_grid))
            s = ''
            for i in res:
                s += ','.join(i)
            if s not in op_results:
                op_results[s] = ((r,rf), (f,ff))
    return set([op_results[k] for k in op_results])

op_pairs = unique_op_pairs()
    
def right_edge(grid):
    str = ''
    n,m = len(grid), len(grid[0])
    for i in range(n):
        str += grid[i][m-1]
    return str
    
def left_edge(grid):
    str = ''
    n,m = len(grid), len(grid[0])
    for i in range(n):
        str += grid[i][0]
    return str
    
def top_edge(grid):
    return ''.join(grid[0])
    
def bottom_edge(grid):
    return ''.join(grid[len(grid)-1])
    
edges = [('right', right_edge, left_edge), 
('left', left_edge, right_edge), ('top', top_edge, bottom_edge),
('bottom', bottom_edge, top_edge)]

def match_edge(g1, g2):
    # determine which edges of g1, g2 matches to
    matches = []
    for (e, f1, f2) in edges:
        if f1(g1) == f2(g2):
            matches.append(e)
    return matches

# in is 12x12
premade_grids = {}
adj = defaultdict(list)
for kk, t1 in enumerate(tiles):
    g1 = tiles[t1]
    print('Checking tile {}: {} of {}'.format(t1, kk + 1, len(tiles)))
    for t2 in tiles:
        if t2 == t1:
            continue
        g2 = tiles[t2]
        for ((r1, r1func),(f1,f1func)) in op_pairs:
            g1op = '{},{}'.format(r1,f1)
            if (t1, g1op) in premade_grids:
                newg1 = premade_grids[(t1, g1op)]
            else:
                newg1 = r1func(f1func(g1))
                premade_grids[(t1, g1op)] = newg1
            for ((r, rfunc), (f, ffunc)) in op_pairs:
                g2op = '{},{}'.format(r,f)
                if (t2, g2op) in premade_grids:
                    newg2 = premade_grids[(t2, g2op)]
                else:
                    newg2 = rfunc(ffunc(g2))
                    premade_grids[(t2, g2op)] = newg2
                matches = match_edge(newg1, newg2)
                for m in matches:
                    adj[(t1, g1op)].append(((t2, g2op), m))
    
def side_move(i, j, side):
    if side == 'top':
        return (i -1, j)
    if side == 'bottom':
        return (i+1, j)
    if side == 'right':
        return (i, j + 1)
    if side == 'left':
        return (i, j - 1)
    print('somethings wrong')
    exit()
    
def valid(i, j, grid):
    if i >= 0 and i < len(grid):
        if j >= 0 and j < len(grid[i]):
            return True
    return False
    
def fits(t, op, i, j, grid):
    if grid[i][j] is not None:
        return False
    sides = ['bottom', 'top', 'left', 'right']
    for side in sides:
        i2,j2 = side_move(i, j, side)
        if valid(i2,j2,grid):
            if grid[i2][j2] is not None:
                t2,op2 = grid[i2][j2]
                if ((t2,op2), side) not in adj[(t,op)]:
                    return False
    return True

SIDES = int(math.sqrt(len(tiles)))
GRID = [[None for i in range(SIDES)] for j in range(SIDES)]

def solve(t, op, i=0, j=0, unused=set([t for t in tiles])):
    if not fits(t, op, i, j, GRID):
        return None
    depth = SIDES * i + j + 1
    if depth % SIDES == 0:
        rleft = SIDES * SIDES - depth
        print('.'*depth + ' '*rleft + '|')
        
    GRID[i][j] = (t, op)
    unused.remove(t)
    if len(unused) == 0:
        return GRID
    for k in adj:
        (t2,op2) = k
        if t2 not in unused:
            continue
        newj = (j + 1) % SIDES
        newi = i if newj > 0 else i + 1
        ret = solve(t2,op2,newi,newj,unused)
        if ret is not None:
            return ret

    GRID[i][j] = None
    unused.add(t)
    return None
    
def four_corners(grid):
    n,m = len(grid), len(grid[0])
    a,b,c,d = grid[0][0][0], grid[0][m-1][0], grid[n-1][m-1][0], grid[n-1][0][0]
    return (a*b*c*d, [a,b,c,d])
    
def print_grid(metagrid):
    for k in premade_grids:
        n,m = len(premade_grids[k]), len(premade_grids[k][0])
        break
    for row in metagrid:
        for i in range(1,n-1):
            fullrow = ''
            for k in row:
                grid = premade_grids[k]
                fullrow += ''.join(grid[i][1:m-1])
            print(fullrow)    
    
for k in adj:
    t,op = k
    ret = solve(t,op)
    if ret is not None:
        print('grid is {}'.format(ret))
        print('four corners: {}'.format(four_corners(GRID)))
        print_grid(GRID)
        exit()
                
            



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # hello