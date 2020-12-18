
from copy import copy, deepcopy
from collections import defaultdict, deque, Counter
from blist import *
from parse import compile
import sys
sys.setrecursionlimit(10000)

regx = compile("x={}, y={}..{}")
regy = compile("y={}, x={}..{}")
# x=732, y=143..151
# y=438, x=555..569

s = input()
lines = []
mini = 100000000
maxi = -1
grid = [[' ' for j in range(0, 1000)] for i in range(0, 2000)]
while s != 'done':
    if s[0] == 'x':
        j,i1,i2 = map(int, regx.parse(s))
        for i in range(i1, i2 + 1):
            mini = min(i, mini)
            maxi = max(i, maxi)
            grid[i][j] = '#'
    else:
        i,j1,j2 = map(int, regy.parse(s))
        for j in range(j1, j2 + 1):
            grid[i][j] = '#'
    s = input()

def printp(x,y):
    print(mini, maxi)
    grid[x][y] = 'X'
    for k in range(0, x + 50):
        print('|' + ''.join(grid[k][(y - 100):(y + 100)]) + '|')
    exit()

def fill(i1,j1,i2,j2):
    if False:
        return
    for i in range(i1,i2+1):
        for j in range(j1,j2+1):
            grid[i][j] = '~'

def flow(ip = 0, jp = 500):
    i,j = ip,jp
    if grid[i][j] == '~':
        return 0
    
    # xx,yy = 22,508
    # if (i,j) == (xx,yy):
    #     printp(xx,yy)
    
    print("Flowing", i, j)
    x = flowdown(i,j)
    
    # we've reached the bottom
    if x is None:
        fill(i,j,maxi,j)
        return (maxi - i + 1)
    print("Flow down", x - i)
        
    # flow down
    total = (x - i)
    
    
    # fill up
    x -= 1
    
    # find left barier, find right barier
    lb, rb = j, j
    while grid[x+1][lb] == '#' and grid[x][lb] != '#':
        lb -= 1
    while grid[x+1][rb] == '#' and grid[x][rb] != '#':
        rb += 1
    if grid[x+1][rb] == ' ':
        return flow(x,rb)
    if grid[x+1][lb] == ' ':
        return flow(x,lb)
        
    
    ly, ry = flowleft(x, j, -1), flowright(x, j, 999)
    if ly is not None:
        lb = ly
    if ry is not None:
        rb = ry
    while ly is not None and ry is not None and not (ly < lb or ry > rb):
        lb, rb = ly, ry
        total += (j - ly) - 1
        total += (ry - j) - 1
        fill(x,ly+1,x,ry-1)
        x -= 1
        ly, ry = flowleft(x, j, lb), flowright(x, j, rb)
        # boundary is larger than us
        
    # overflow both
    print(ly,ry,lb,rb)
    if (ly,ry) == (None, None):
        total += (rb - lb) - 1
        fill(x,lb,x,rb)
        total += flow(x, lb - 1)
        total += flow(x, rb + 1)
        
    # overflow left
    elif ly is None and ry <= rb:
        total += (ry - lb) - 2
        fill(x,lb,x,ry-1)
        total += flow(x, lb - 1)
        
    # overflow right
    elif ry is None and ly >= lb:
        total += (rb - ly) - 2
        fill(x,ly+1,x,rb)
        total += flow(x, rb + 1)
    
    # overflow both
    elif ly < lb and ry > rb:
        total += (rb - lb) - 1
        fill(x,lb,x,rb)
        total += flow(x, lb - 1)
        total += flow(x, rb + 1)
        
    # overflow left
    elif ly < lb:
        total += (ry - lb) - 2
        fill(x,lb,x,ry-1)
        total += flow(x, lb - 1)
        
    # overflow right
    elif ry > rb:
        total += (rb - ly) - 2
        fill(x,ly+1,x,rb)
        total += flow(x, rb + 1)
    
    # flow down
    while grid[ip][jp] == ' ':
        grid[ip][jp] = '~'
        ip += 1
        
    # fill(i,j,x-1,j)
    return total

def flowleft(i, j, k):
    # go left until we hit a wall
    if j < k:
        return None
    if grid[i][j] == '#':
        return j
    else:
        return flowleft(i,j-1,k)
    
def flowright(i, j, k):
    # go right until we hit a wall
    if j > k:
        return None
    if grid[i][j] == '#':
        return j
    else:
        return flowright(i,j+1,k)

def flowdown(i, j):
    # go down until we hit a wall
    if i > maxi:
        return None
    if grid[i][j] == '#':
        return i
    else:
        return flowdown(i+1,j)
        
print(flow())
printp(0,500)

