
from copy import copy, deepcopy
from collections import defaultdict, deque, Counter
from blist import *
from parse import compile

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
    
total = 0
def flow(ip = 0, jp = 500):
    global total
    # if total >= 200000:
    #     printp(500,500)
    
    i,j = ip,jp
    # go down while we can
    while can_go_down(i,j):
        i += 1
    if i == maxi:
        return
    grid[i][j] = '~'
    total += 1
        
    # bfs left and right
    q = adj(i,j)
    if len(q) == 0:
        # gotta go back up
        while grid[i][j-1] == '#' and grid[i][j+1] == '#':
            i -= 1
        if grid[i][j-1] == ' ':
            q.append((i,j-1))
        if grid[i][j+1] == ' ':
            q.append((i,j+1))
    
    while len(q) > 0:
        x,y = q.pop(0)
        if can_go_down(x,y):
            flow(x,y)
            continue
        grid[x][y] = '~'
        total += 1
        q.extend(adj(x,y))
        
    while can_go_down(ip,jp):
        grid[ip][jp] = '~'
        ip += 1
    
def can_go_down(i,j):
    return grid[i+1][j] == ' ' and i < maxi
    
def adj(i,j):
    if can_go_down(i,j):
        return None
        
    desc = []
    # go left 
    if grid[i][j-1] == ' ':
        desc.append((i,j-1))
    # go right
    if grid[i][j+1] == ' ':
        desc.append((i,j+1))
    # go up in not left or right
    if len(desc) == 0 and grid[i-1][j] == ' ':
        desc.append((i-1,j))
    return desc
    
    
flow()
print(total)
printp(0,500)
    
    
    
    
    
    
    
    
    
    
    