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

def rotate3(grid):
    return rotate1(grid, 3)
    
def rotate2(grid):
    return rotate1(grid, 2)
    
def rotate1(cgrid, times=1):
    if times > 1:
        grid = rotate1(cgrid, times - 1)
    else:
        grid = cgrid
    n,m = len(grid), len(grid[0])
    newgrid = deepcopy(grid)
    for i in range(n):
        if i > 0 and i < n-1:
            iters = [0, m-1]
        else:
            iters = range(m)
        for j in iters:
            c = grid[i][j]
            newi = j
            newj = m - i - 1
            newgrid[newi][newj] = c 
    return newgrid
    
def flip_vert(grid):
    n,m = len(grid), len(grid[0])
    newgrid = deepcopy(grid)
    for i in range(n):
        if i > 0 and i < n-1:
            iters = [0, m-1]
        else:
            iters = range(m)
        for j in iters:
            c = grid[i][j]
            newi = n - i - 1
            newj = j
            newgrid[newi][newj] = c 
    return newgrid
            
def flip_hor(grid):
    n,m = len(grid), len(grid[0])
    newgrid = deepcopy(grid)
    for i in range(n):
        if i > 0 and i < n-1:
            iters = [0, m-1]
        else:
            iters = range(m)
        for j in iters:
            c = grid[i][j]
            newi = i
            newj = m - j - 1
            newgrid[newi][newj] = c 
    return newgrid
    
def flip_both(grid):
    return flip_hor(flip_vert(grid))
    
rots = [
    ('rot1', rotate1),
    ('rot2', rotate2),
    ('rot3', rotate3),
    ('rot_none', lambda x: x)]
    
flips = [('fliph', flip_hor), ('flipv', flip_vert), ('flipb', flip_both),
('flip_none', lambda x: x)]
    
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
    str = ''
    n,m = len(grid), len(grid[0])
    for j in range(m):
        str += grid[0][j]
    return str
    
def bottom_edge(grid):
    str = ''
    n,m = len(grid), len(grid[0])
    for j in range(m):
        str += grid[n - 1][j]
    return str
    
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
        for (r1, r1func) in rots:
            for (f1, f1func) in flips:
                g1op = '{},{}'.format(r1,f1)
                if (t1, g1op) in premade_grids:
                    newg1 = premade_grids[(t1, g1op)]
                else:
                    newg1 = r1func(f1func(g1))
                    premade_grids[(t1, g1op)] = newg1
                for (r, rfunc) in rots:
                    for (f, ffunc) in flips:
                        g2op = '{},{}'.format(r,f)
                        if (t2, g2op) in premade_grids:
                            newg2 = premade_grids[(t2, g2op)]
                        else:
                            newg2 = rfunc(ffunc(g2))
                            premade_grids[(t2, g2op)] = newg2
                        matches = match_edge(newg1, newg2)
                        for m in matches:
                            adj[(t1, g1op)].append(
                                ((t2, g2op), m)
                            )

tile_matches = defaultdict(lambda: 0)
for t in tiles:
    for k in adj:
        (t1, op) = k
        if t == t1 and len(adj[k]) > 0:
            tile_matches[t] += 1 
                

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
    
def fits(t, op, i, j, grid, adj):
    sides = ['bottom', 'top', 'left', 'right']
    for side in sides:
        i2,j2 = side_move(i, j, side)
        if valid(i2,j2,grid):
            if grid[i2][j2] is not None:
                t2,op2 = grid[i2][j2]
                if ((t2,op2), side) not in adj[(t,op)]:
                    return False
    return True
    
def filled_in(grid):
    for row in grid:
        for c in row:
            if c is None:
                return False
    return True
    
def in_grid(t, grid):
    for row in grid:
        for c in row:
            if c is not None and t == c[0]:
                return True
    return False

def solve(t1, op1, i1, j1, grid, adj, depth=1, used=set()):
    print('${}checking {} {} at {},{}'.format(' '*(depth-2), t1,op1,i1,j1))
    if (t1,op1) in used:
        print('{}already used!'.format(' '*(depth-1)))
        return None
    if not fits(t1,op1,i1,j1,grid,adj):
        print('{}not fits! \n{}'.format(' '*(depth-1),grid))
        return None
    # else:
    #     print('{}fits!'.format(' '*(depth-1)))

    grid[i1][j1] = (t1, op1)
    used.add(t1)
    if depth -1 >= len(grid) * len(grid[0]):
        print('{}depth {} >= {}'.format(' '*(depth-1),depth, len(grid) * len(grid[0])))
        # if filled_in(grid):
        return grid
        # else:
        #     used.remove(t1)
        #     grid[i1][j1] = None
        #     return None
        
    edges = adj[(t1, op1)]
    for ((t2, op2), side) in edges:
        if t1 == 3079 and op1 == 'rot_none,flip_none':
            print(t2,op2,side)
        if in_grid(t2,grid):
            if t1 == 3079 and op1 == 'rot_none,flip_none':
                print('was used')
                for g in grid:
                    print(g)
            continue
        i2,j2 = side_move(i1,j1,side)
        if valid(i2,j2,grid):
            if t1 == 3079 and op1 == 'rot_none,flip_none':
                print('invalid move to', i2,j2)
            ret = solve(t2,op2,i2,j2,grid,adj,depth+1,used)
            if ret is not None:
                return ret

    used.remove(t1)
    grid[i1][j1] = None
    return None
    
start_t = None
for k in tiles:
    start_t = k
    break

sidess = int(math.sqrt(len(tiles)))
meta_grid = [[None for i in range(sidess)] for j in range(sidess)]
t1_ops = []
for k in adj:
    t,op = k
    if t == start_t:
        t1_ops.append(op)
    
def four_corners(grid):
    n,m = len(grid), len(grid[0])
    a,b,c,d = grid[0][0][0], grid[0][m-1][0], grid[n-1][m-1][0], grid[n-1][0][0]
    return (a*b*c*d, [a,b,c,d])
    
for i in range(sidess):
    for j in range(sidess):
        for op in t1_ops:
            m = deepcopy(meta_grid)
            ret = solve(start_t, op, i, j, m, adj)
            if ret is None:
                continue
            else:
                print(ret)
                print(four_corners(ret))
                exit()

                
            



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # hello