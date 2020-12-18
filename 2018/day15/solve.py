
from copy import copy, deepcopy
from collections import defaultdict, deque, Counter
from blist import *
from parse import compile

# s = input()
# 
# reg = compile("{} => {}")
# f,v = reg.parse(s)

s = input()
grid = []
hp = []
while s != 'done':
    row = list(s)
    hp.append([(200 if r in ['G', 'E'] else 0) for r in row])
    grid.append(row)
    s = input()
    
def run():
    done = 1
    r = 0
    while done > 0 and r < 8:
        print(" ROROROROROROR", r)
        ens = []
        for x in range(0, len(grid)):
            for y in range(0, len(grid[x])):
                if grid[x][y] in ['G', 'E']:
                    ens.append((x,y)) 
        ens.sort()
        print(ens)
        done = 0
        cc = False # from round 7 to 8, unit 10 moves down in mine, left in correct
        for (x,y) in ens:
            print("PROCESSING", x,y, "round", r, "of", ens)
            for k in range(0, len(grid)):
                print(''.join(grid[k]) + ' : ' + ','.join([str(x) for x in hp[k] if x != 0]))
            c = Counter()
            for xp in range(0, len(grid)):
                for yp in range(0, len(grid[xp])):
                    if grid[xp][yp] in ['G', 'E']:
                         c[grid[xp][yp]] += 1
            if len(c) == 1:
                cc = True
                break
            
            # for h in hp:
            #     print(','.join([str(x) for x in h]))
            done += turn(x,y)
            # print(r, "done", done)
            # break
        if cc:
            break
        print("adding r")
        r += 1
        # return 1
    hh = sum([sum(h) for h in hp])
    for g in grid:
        print(''.join(g))
    for h in hp:
        print(','.join([str(x) for x in h]))
    print(hh)
    print(r)
    return hh * r
    
    
def turn(i,j):
    if grid[i][j] == 'E':
        enemy = 'G'
    elif grid[i][j] == 'G':
        enemy = 'E'
    else:
        # killed earlier in return
        return 0
    print("me", i,j, enemy)
        
    ens = []
    for x in range(0, len(grid)):
        for y in range(0, len(grid[x])):
            if grid[x][y] == enemy:
                ens.append((x,y)) 
    if len(ens) == 0:
        return 0
    print("ens", ens)
    inr = []
    for (ip,jp) in ens:
        for x in range(ip-1, ip+2):
            for y in range(jp-1, jp+2):
                if x >= 0 and x < len(grid):
                    if y >= 0 and y < len(grid[x]):
                        # if (x,y) == (2,5):
                        #     print("IM TWO FIVEEE")
                        if abs(x - ip) + abs(y - jp) == 2:
                            # if (x,y) == (2,5):
                            #     print("IM TWO FIVEEE, not counted")
                            continue
                        if grid[x][y] == '.':
                            # if (x,y) == (2,5):
                            #     print("IM TWO FIVEEE, dot")
                            inr.append((x,y,ip,jp))
                        if (x,y) == (i,j):
                            # if (x,y) == (2,5):?
                            #     print("IM TWO FIVEEE, me")
                            inr.append((i,j,ip,jp))
    if len(inr) == 0:
        return 0
    # print("inrange", inr)
        
    # check if already inr?
    xx = [(x,y) for (x,y,_,_) in inr]
    # print(xx)
    if (i,j) not in [(x,y) for (x,y,_,_) in inr]:
        # print("NOT IN R")
        ss = shortest(i,j,inr)
        if ss is None:
            return 0
        
        sx,sy = ss
        if grid[sx][sy] == '.':
            print("moving", sx,sy)
            grid[sx][sy] = grid[i][j]
            grid[i][j] = '.'
            hp[sx][sy] = hp[i][j]
            hp[i][j] = 0
            i,j = sx,sy
        
    adj = []
    # for x in range(i-1, i+2):
    #     for y in range(j-1, j+2):
    #         if x >= 0 and x < len(grid):
    #             if y >= 0 and y < len(grid[x]):
    #                 if abs(x - ip) + abs(y - jp) == 2:
    #                     continue
    #                 if grid[x][y] == enemy:
    #                     adj.append((hp[x][y], x,y))
    adj = adjf(i,j,enemy)
    print(i,j, "adj", adj)
    if len(adj) == 0:
        return 1
    adj.sort()
    _,tx,ty = adj[0]
    print("attacking", tx,ty)
    
    # attack
    hpt = hp[tx][ty]
    if hpt - 3 <= 0:
        # remove
        grid[tx][ty] = '.'
        hp[tx][ty] = 0
    else:
        hp[tx][ty] = hpt - 3
    return 1

def adjf(ip,jp,m = '.'):
    desc = []
    if ip - 1 >= 0:
        x,y = ip - 1, jp
        if grid[x][y] == m:
            desc.append((hp[x][y],x,y))
    if jp - 1 >= 0:
        x,y = ip, jp - 1
        if grid[x][y] == m:
            desc.append((hp[x][y],x,y))
    if ip + 1 < len(grid):
        x,y = ip + 1, jp
        if grid[x][y] == m:
            desc.append((hp[x][y],x,y))
    if jp + 1 < len(grid[0]):
        x,y = ip, jp + 1
        if grid[x][y] == m:
            desc.append((hp[x][y],x,y))  
    return desc      

def shortest(i,j,inr):
    print("shortest from ", i, j)
    
    dist = {}
    q = [(0,i,j,None,None)]
    par = {}
    while len(q) > 0:
        q.sort()
        (d,ip,jp,pi,pj) = q.pop(0)
        if (ip,jp) in dist:
            continue
        # print("processing", ip, jp, "at dist", d)
        # print(q)
        dist[(ip,jp)] = d
        par[(ip,jp)] = (pi,pj)
        #adj
        desc = []
        if ip - 1 >= 0:
            x,y = ip - 1, jp
            if grid[x][y] == '.':
                desc.append((x,y))
        if jp - 1 >= 0:
            x,y = ip, jp - 1
            if grid[x][y] == '.':
                desc.append((x,y))
        if ip + 1 < len(grid):
            x,y = ip + 1, jp
            if grid[x][y] == '.':
                desc.append((x,y))
        if jp + 1 < len(grid[0]):
            x,y = ip, jp + 1
            if grid[x][y] == '.':
                desc.append((x,y))
            
        # print("desc of ",ip,jp, "is", desc)
        for (x,y) in desc:
            if (x,y) not in dist:
                q.append((d + 1, x,y,ip,jp))
    mind = 10000000
    # print("inr", inr)
    # print(dist)
    for (x,y,_,_) in inr:
        # desc = []
        # if ip - 1 >= 0:
        #     x,y = ip - 1, jp
        #     if grid[x][y] == '.':
        #         desc.append((x,y))
        # if jp - 1 >= 0:
        #     x,y = ip, jp - 1
        #     if grid[x][y] == '.':
        #         desc.append((x,y))
        # if ip + 1 < len(grid):
        #     x,y = ip + 1, jp
        #     if grid[x][y] == '.':
        #         desc.append((x,y))
        # if jp + 1 < len(grid[0]):
        #     x,y = ip, jp + 1
        #     if grid[x][y] == '.':
        #         desc.append((x,y))
        # 
        if (x,y) not in dist:
            continue
            # unreachable
        d = dist[(x,y)]
        # print("dist to ", x, y, "is", d)
        if d < mind:
            mind = d
    
    if mind ==10000000:
        return None
    upr = [(x,y) for (x,y,_,_) in inr if (x,y) in dist and dist[(x,y)] == mind]
    upr.sort()
    x,y = upr[0]
    path = [(x,y)]
    px,py = par[(x,y)]
    while px is not None:
        path.append((px,py))
        px,py = par[(px,py)]
    print("path", path)
    return path[-2]

    
print(run())
    
