
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

def printp(x=0,y=500):
    print(mini, maxi)
    grid[x][y] = 'X'
    for k in range(0, x + 50):
        print('|' + ''.join(grid[k][(y - 100):(y + 100)]) + '|')
    # exit()

def fill(i1,j1,i2,j2):
    if False:
        return
    for i in range(i1,i2+1):
        for j in range(j1,j2+1):
            grid[i][j] = '~'

ct = 0
# ip = 6
def flow(ip = 6, jp = 500):
    global ct
    print("Flowing", ip, jp)
    if (ip,jp) == (27,511):
        ct += 1
        if ct == 3:
            printp(27,511)
    
    i,j = ip,jp
    if grid[i][j] == '~':
        return
    
    i = flowdown(i,j)
    # we've reached the bottom
    if i is None:
        print("hit max")
        fill(ip,jp,maxi,j)
        return
    i -= 1
        
    # Find barriers
    lb, rb = j, j
    while grid[i+1][lb] != ' ' and grid[i][lb] != '#':
        lb -= 1
    while grid[i+1][rb] != ' ' and grid[i][rb] != '#':
        rb += 1
        
    print(i,j,lb,rb)
    # Determine which case we're in, cup, or slab
    if grid[i+1][rb] != '#' and grid[i+1][lb] != '#' and grid[i][rb] != '#' and grid[i][lb] != '#' and grid[i+1][j] == '#':
        print("Hit slab", i,j)
        # slab with rb and lb being the overflow points
        # slab handles itself
        # fill in slab section
        fill(i,lb+1,i,rb-1)
        # flow left barrier and right barrier
        print("Flowing left border")
        flow(i,lb)
        print("Flowing right border")
        flow(i,rb) # if wwe've filled up left/right current slab, repeat this fill
    elif grid[i+1][lb] == '#' and grid[i+1][rb] != '#' and grid[i][rb] == ' ' and grid[i][lb] != ' ':
        print("right droopy slab")
        fill(i,lb+1,i,rb-1)
        print("Flowing right border")
        flow(i,rb) # if wwe've filled up left/right current slab, repeat this fill
    elif grid[i+1][rb] == '#' and grid[i+1][lb] != '#' and grid[i][lb] == ' ' and grid[i][rb] != ' ':
        print("left droopy slab")
        fill(i,lb+1,i,rb-1)
        print("Flowing left border")
        flow(i,lb)
    elif grid[i+1][rb] != ' ' and grid[i+1][lb] != ' ' and grid[i][rb] != ' ' and grid[i][lb] != ' ':
        print("Hit cup", i,j)
        # cup with rb and lb being boundaries
        # cup, we need to know how the interior fills up
        # fnd top of cup
        ltop, rtop = walltop(i,lb), walltop(i,rb)
        # fill left to right until we reach top of cup
        fill(i,lb+1,i,rb-1)
        i -= 1
        while i > max(ltop, rtop):
            print("Filling level", i)
            ly,ry = flowleft(i,j), flowright(i,j)
            print("left right walls", i,ly,ry)
            if ly > lb:
                # move left boundary in
                lb, ltop = ly, walltop(i,ly)
            if rb > ry:
                # move right boundary in
                rb, rtop = ry, walltop(i,ry)
            fill(i,lb+1,i,rb-1)
            i -= 1
        if i == rtop and i == ltop:
            # overflow both
            print("Overfloww both")
            flow(i,rb+1)
            flow(i,lb-1)
            fill(i,lb,i,rb)
        elif i == rtop:
            # overflow right
            flow(i,rb+1)
            fill(i,lb+1,i,rb)
        elif i == ltop:
            # overflow left
            flow(i,lb-1)
            fill(i,lb,i,rb-1)
            
    # Check if we've totally filled
    lb, rb = jp, jp
    while grid[i][lb] == '~':
        lb -= 1
    while grid[i][rb] == '~':
        rb += 1
    if grid[i][lb] == '#' and grid[i][rb] == '#':
        # not filled, repeat
        flow(ip,jp)
    fill(ip,jp,i,jp)
            
def walltop(i,j):
    top = i 
    while grid[top][j] == '#':
        top -= 1
    return top   

def flowleft(i, j):
    # go left until we hit a wall
    lb = j
    while grid[i][lb] != '#':
        lb -= 1
    return lb
    
def flowright(i, j):
    # go right until we hit a wall
    rb = j
    while grid[i][rb] != '#':
        rb += 1
    return rb
    
def flowdown(i, j):
    # go down until we hit a wall
    bb = i
    while grid[bb][j] == ' ' and bb <= maxi:
        bb += 1
    if bb > maxi:
        return None
    return bb

flow() # 38364
printp(1900,500)
tot = 0
for i in range(0, len(grid)):
    j = 0
    while j < len(grid[i]):
        if grid[i][j] == '~':
            # Check if we've totally filled
            lb, rb = j, j
            while grid[i][lb] == '~':
                lb -= 1
            while grid[i][rb] == '~':
                rb += 1
            if grid[i][lb] == '#' and grid[i][rb] == '#':
                tot += (rb - lb) - 1
            j = rb
        else:
            j += 1
print(tot, mini, maxi)

