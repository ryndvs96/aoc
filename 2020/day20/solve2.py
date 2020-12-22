from parse import compile
from copy import copy, deepcopy
from collections import defaultdict, Counter, deque
from blist import *
import itertools
import math
import sys
# sys.setrecursionlimit(10000)

s = input()
GRID = []
while s != 'done':
    GRID.append(list(s))
    s = input()
    
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
        [str(i*len(GRID[i]) + j) for j in range(len(GRID[i]))] 
        for i in range(len(GRID))
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

monster = [
list('                  # '),
list('#    ##    ##    ###'),
list(' #  #  #  #  #  #   ')]

monster_cells = []
for i, row in enumerate(monster):
    for j, c in enumerate(row):
        if c == '#':
            monster_cells.append((i,j))
print(monster_cells)

def valid(i, j, grid):
    if i >= 0 and i < len(grid):
        if j >= 0 and j < len(grid[i]):
            return True
    return False

def find_monster(i, j, grid):
    total = set()
    for (ioff,joff) in monster_cells:
        if not valid(i + ioff, j + joff, grid):
            return None

        if grid[i + ioff][j + joff] != '#':
            return None
        else:
            total.add((i + ioff, j + joff))
    print('returning total')
    return total
    
def count_non(grid, ignore):
    newgrid = deepcopy(grid)
    for (i,j) in ignore:
        newgrid[i][j] = '.'
        
    ct = 0
    for _, row in enumerate(newgrid):
        for _, c in enumerate(row):
            if c == '#':
                ct += 1
    return ct
    
for ((op1,f1),(op2,f2)) in op_pairs:
    newgrid = f1(f2(GRID))
    totals = set()
    for i, row in enumerate(newgrid):
        for j, c in enumerate(row):
            total = find_monster(i,j,newgrid)
            if total:
                totals = totals.union(total)
    if len(totals) > 0:
        c = count_non(newgrid, totals)
        print(c)
            
    
    

                
            



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # hello