from parse import compile
from blist import blist
from copy import deepcopy

pre = compile("It's {}, I love it!")
# a,c = pre.parse(line)

lines = []
n = input()
while n != 'done':
    lines.append(n)
    n = input()


grid = []
for l in lines:
    row = []
    for c in l:
        row.append(c)
    grid.append(row)
    
def count(grid, i, j):
    ct = 0
    if i > 0:
        c = '.'
        ip = i 
        jp = j
        while c == '.':
            ip -= 1
            if ip < 0 or ip >= len(grid) or jp < 0 or jp >= len(grid[i]):
                break
            c = grid[ip][jp]
        if c == '#':        
            ct += 1
        if j > 0:
            c = '.'
            ip = i 
            jp = j
            while c == '.':
                ip -= 1
                jp -= 1
                if ip < 0 or ip >= len(grid) or jp < 0 or jp >= len(grid[i]):
                    break
                c = grid[ip][jp]
            if c == '#':
                ct += 1
        if j < len(grid[i]) - 1:
            c = '.'
            ip = i 
            jp = j
            while c == '.':
                ip -= 1
                jp += 1
                if ip < 0 or ip >= len(grid) or jp < 0 or jp >= len(grid[i]):
                    break
                c = grid[ip][jp]
            if c == '#':
                ct += 1
    if i < len(grid) - 1:
        c = '.'
        ip = i 
        jp = j
        while c == '.':
            ip += 1
            if ip < 0 or ip >= len(grid) or jp < 0 or jp >= len(grid[i]):
                break
            c = grid[ip][jp]
        if c == '#':
            ct += 1
        if j > 0:
            c = '.'
            ip = i 
            jp = j
            while c == '.':
                ip += 1
                jp -= 1
                if ip < 0 or ip >= len(grid) or jp < 0 or jp >= len(grid[i]):
                    break
                c = grid[ip][jp]
            if c == '#':
                ct += 1
        if j < len(grid[i]) - 1:
            c = '.'
            ip = i 
            jp = j
            while c == '.':
                ip += 1
                jp += 1
                if ip < 0 or ip >= len(grid) or jp < 0 or jp >= len(grid[i]):
                    break
                c = grid[ip][jp]
            if c == '#':
                ct += 1
    if j > 0:
        c = '.'
        ip = i 
        jp = j
        while c == '.':
            jp -= 1
            if ip < 0 or ip >= len(grid) or jp < 0 or jp >= len(grid[i]):
                break
            c = grid[ip][jp]
        if c == '#':
            ct += 1
    if j < len(grid[i]) - 1:
        c = '.'
        ip = i 
        jp = j
        while c == '.':
            jp += 1
            if ip < 0 or ip >= len(grid) or jp < 0 or jp >= len(grid[i]):
                break
            c = grid[ip][jp]
        if c == '#':
            ct += 1
    return ct
    
def printg(grid):
    for g in grid:
        print(''.join(g))
    
change = 1
iters = 0
while change > 0:
    iters += 1
    print('iter', iters)
    printg(grid)
    change = 0
    newgrid = deepcopy(grid)
    for i, _ in enumerate(grid):
        for j, c in enumerate(grid[i]):
            ct = count(grid, i, j)
            if c == 'L' and ct == 0:
                change += 1
                newgrid[i][j] = '#'
            elif c == '#' and ct >= 5:
                change += 1
                newgrid[i][j] = 'L'
            else:
                newgrid[i][j] = c
    grid = deepcopy(newgrid)
    
print('final')
printg(grid)

ct = 0
for i, _ in enumerate(grid):
    for j, c in enumerate(grid[i]):
        if c == '#':
            ct += 1
    
print('iters', iters)        
print(ct)

    




