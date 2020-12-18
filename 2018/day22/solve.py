
from copy import copy, deepcopy
from collections import defaultdict, deque, Counter
# from blist import *
from parse import compile

d = 3879
x,y = 8,713
def run():
    grid = [[0 for i in range(0, y+1)] for j in range(0, x+1)]
    e = [[0 for i in range(0, y+1)] for j in range(0, x+1)]
    for i in range(0, x+1):
        for j in range(0, y+1):
            print(i,j)
            if (i,j) == (0,0):
                grid[i][j] = 0
                e[i][j] = ee(grid[i][j])
            elif (i,j) == (x,y):
                grid[i][j] = 0
                e[i][j] = ee(grid[i][j])
            elif j == 0:
                grid[i][j] = ((i) * (16807)) 
                e[i][j] = ee(grid[i][j])
            elif i == 0:
                grid[i][j] = ((j) * (48271)) 
                e[i][j] = ee(grid[i][j])
            else:
                grid[i][j] = ee(grid[i-1][j]) * ee(grid[i][j-1])
                e[i][j] = ee(grid[i][j])
    t = 0
    for i in range(0, x+1):
        for j in range(0, y+1):
            t += e[i][j] % 3
    print(t)


def erosion(v):
    return (v + 3879) % 20183

        
run()
