
from copy import copy, deepcopy
from collections import defaultdict, deque, Counter
from blist import *
from parse import compile
# import sys
# sys.setrecursionlimit(10000)

reg = compile("x={}, y={}..{}")

s = input()
grid = []
while s != 'done':
    row = list(s)
    grid.append(row)
    s = input()

def main():
    global grid
    for k in range(0, 10000):
        print("Minute", k + 1, score(grid))
        # for gs in grid:
        #     print(''.join(gs)) # 851, 823, 795, 28 period start, 514 with 207240
        print('---------------------------------------------')
        g = deepcopy(grid)
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                a = adj(i,j,grid)
                pts = [grid[ip][jp] for (ip,jp) in a]
                if grid[i][j] == '.':
                    l = len([1 for p in pts if p == '|'])
                    if l >= 3:
                        g[i][j] = '|'
                elif grid[i][j] == '|':
                    l = len([1 for p in pts if p == '#'])
                    if l >= 3:
                        g[i][j] = '#'
                else:
                    l = len([1 for p in pts if p == '#'])
                    d = len([1 for p in pts if p == '|'])
                    if l >= 1 and d >= 1:
                        g[i][j] = '#'
                    else:
                        g[i][j] = '.'
        grid = g
    for gs in grid:
        print(''.join(gs))
    print('---------------------------------------------')
    print(score(grid))
    return 0
    
def score(grid):
    o, f, t = 0,0,0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == '|':
                t += 1
            elif grid[i][j] == '#':
                f += 1
            else:
                o += 1
    return (f*t)
    
def adj(i,j,grid):
    desc = []
    if j - 1 >= 0:
        desc.append((i, j - 1))
    if j + 1 < len(grid):
        desc.append((i, j + 1))
    if i - 1 >= 0:
        desc.append((i - 1,j))
        if j - 1 >= 0:
            desc.append((i - 1,j-1))
        if j + 1 < len(grid[0]):
            desc.append((i - 1,j+1))
        
    if i + 1< len(grid):
        desc.append((i + 1, j))
        if j - 1 >= 0:
            desc.append((i + 1, j - 1))
        if j + 1< len(grid[0]):
            desc.append((i + 1, j + 1))
    return desc

main()




