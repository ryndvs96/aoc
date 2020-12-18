
from copy import copy, deepcopy

s = input()
grid = []
carts = []
while s != 'done':
    row = list(s)
    grid.append(row)
    s = input()
    
# fix grid, remove carts add lines
for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        if grid[i][j] in ['>', '<']:
            carts.append((i,j,grid[i][j],0))
            grid[i][j] = '-'
        if grid[i][j] in ['^', 'v']:
            carts.append((i,j,grid[i][j],0))
            grid[i][j] = '|'

def orientation(i, j, dir, turn):
    # directions regarding [\, straight, /] in that order
    # output is (updated i, updated j, [order (above)], default for turning)
    if dir == '^':
        dirs = ['<', '^', '>']
        return (i-1, j, dirs, dirs[turn])
    elif dir == '<':
        dirs = ['^', '<', 'v']
        return (i, j-1, dirs, dirs[2 - turn])
    elif dir == 'v':
        dirs = ['>', 'v', '<']
        return (i+1, j, dirs, dirs[turn])
    elif dir == '>':
        dirs = ['v', '>', '^']
        return (i, j+1, dirs, dirs[2 - turn])

def step(carts):
    carts.sort()
    locs = [(i,j) for (i,j,v,t) in carts]
    newcarts = []
    hit = set()
    while len(carts) > 0:
        (i,j,v,t) = carts.pop(0)
        locs.pop(0)
        
        if (i,j) in hit:
            # this cart has been hit
            continue
        
        (ip,jp,dirs,inter) = orientation(i,j,v,t)
        if (ip,jp) in locs:
            # this cart hit another cart
            print(tick, "Collision at {},{}".format(jp,ip))
            hit.add((ip,jp))
            continue
        
        # update location if no hits    
        for (j,b) in enumerate([['\\'], ['|', '-'], ['/']]):
            if grid[ip][jp] in b:
                newcarts.append((ip,jp,dirs[j],t))
                break
        # intersection
        if grid[ip][jp] == '+':
            newcarts.append((ip,jp,inter,(t+1)%3))
        
        # add new location
        locs.append((ip,jp))

    newcarts = [(i,j,v,t) for (i,j,v,t) in newcarts if (i,j) not in hit]
    return newcarts
            
# def printlocs(carts):
#     g = deepcopy(grid)
#     for (i,j,v,_) in carts:
#         g[i][j] = v
#     for gs in g:
#         print(''.join(gs))

# step
tick = 0
while len(carts) > 1:
    # print("Time", tick)
    # printlocs(carts)
    carts = step(carts)
    tick += 1

cart = carts.pop()
print(tick, "Last Cart: {},{}".format(cart[1], cart[0]))

