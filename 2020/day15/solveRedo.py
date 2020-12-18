
from collections import defaultdict, deque, Counter
from blist import *

s = input()
grid = []
# units are (i,j,HP,Type,Alive)
units = []
elf_count = 0
while s != 'done':
    row = list(s)
    grid.append(['#' for r in row])
    for i,r in enumerate(row):
        if r in ['G', 'E']:
            if r == 'E':
                elf_count += 1
            units.append((len(grid) - 1, i, 200, r, True))
        if r != '#':
            grid[len(grid) - 1][i] = r
    s = input()
n,m = len(grid), len(grid[0])
num_units = len(units)
elf_attack = 3

def run(attack):
    global elf_attack
    elf_attack = attack
    done = 1
    r = 0
    while done > 0:
        print("Starting Round", r)
        units.sort()
        
        won = False
        done = 0
        # printgrid()
        for i in range(0, num_units):
            
            ect = sum([1 for (_,_,_,t,a) in units if t == 'E' and a])
            gct = sum([1 for (_,_,_,t,a) in units if t == 'G' and a])
            
            # if only one team is alive
            if ect == 0 or gct == 0:
                dead = True
                for k in range(i, num_units):
                    (_,_,_,_,alive) = units[k]
                    if alive:
                        dead = False
                if dead:
                    # round is over, everyone else is dead
                    r += 1
                print("All Dead")
                won = True
                break
            
            # do a turn
            done += turn(i)
        if won:
            break
        r += 1
    printgrid()
    total_hp = sum([hp for (_,_,hp,_,a) in units if a])
    print("Total HP", total_hp)
    print("Total Rounds", r)
    print("Total Score", r * total_hp)
    print("Elf Attack", elf_attack)
    print("Elves Left", sum([1 for (_,_,_,t,a) in units if t == 'E' and a]), "out of", elf_count)
    return
    
def turn(unit_i):
    (i,j,hp,type,alive) = units[unit_i]
    # print("Initiating Turn of", i,j,hp,type,alive)
    
    # Return if not alive
    if not alive:
        return 0
    
    # Identify enemy type
    enemy = 'G' if type == 'E' else 'E'
    
    ### MOVE TIME ###    
    # Identify all alive enemies
    enemies = []
    for k,(_,_,_,t,a) in enumerate(units):
        if a and t == enemy:
            enemies.append(k)
    
    # If no enemies, return
    if len(enemies) == 0:
        return 0
    
    # Find if we're adjacent to an enemy
    adj = []
    for k,(x,y,hpt,t,a) in enumerate(units):
        if not a or t != enemy:
            continue
        if (x,y) in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
            adj.append((hpt,x,y,t,k))
    
    # If no adjacent, then move
    if len(adj) == 0:
        
        # Identify in range of enemie
        in_range = []
        for k in enemies:
            (x,y,_,t,a) = units[k]
            in_range.extend(adjf(x,y,'.'))
        
        # Check if we're already in range
        if len(in_range) == 0 or (i,j) not in in_range:
            # If not, consider moving
            cs = shortest(i,j,in_range)
            if cs is not None:
                cx,cy = cs
                move = shortest(cx,cy,adjf(i,j))
                
                # No points in range are reachable
                if move is None:
                    return 0
                
                x,y = move
                grid[x][y] = grid[i][j]
                grid[i][j] = '.'
                units[unit_i] = (x,y,hp,type,alive)
                i,j = x,y
        
    ### ATTACK TIME ###
    # Find adjacent enemies
    adj = []
    for k,(x,y,hp,t,a) in enumerate(units):
        if not a or t != enemy:
            continue
        if (x,y) in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
            adj.append((hp,x,y,t,k))
    
    # If no adjacent, end turn
    if len(adj) == 0:
        return 1
        
    # Find first adjacent, via smallest hp
    adj.sort()
    hpt,tx,ty,t,k = adj[0]
    
    # Initiate attack
    if type == 'E':
        if hpt - elf_attack <= 0:
            # Dead
            units[k] = (tx,ty,0,t,False)
            grid[tx][ty] = '.'
        else:
            # Injured
            units[k] = (tx,ty,hpt - elf_attack,t,True)
    else:
        if hpt - 3 <= 0:
            # Dead
            units[k] = (tx,ty,0,t,False)
            grid[tx][ty] = '.'
        else:
            # Injured
            units[k] = (tx,ty,hpt - 3,t,True)
    return 1

def shortest(i,j, inr):
    # distance and parent maps
    dist, par = {}, {}
    # priority queue, entries as (dist, i, j, parent_i, parent_j)
    q = [(0,i,j,None,None)]
    
    # Dijkstras
    while len(q) > 0:
        # if (10,9) == (i,j) and k == 9:
        #     print(q)
        q.sort()
        (d,ip,jp,pi,pj) = q.pop(0)
        if (ip,jp) in dist:
            continue
        
        dist[(ip,jp)] = d
        par[(ip,jp)] = (pi,pj)
        desc = adjf(ip,jp)
        
        for (x,y) in desc:
            if (x,y) not in dist:
                q.append((d + 1,x,y,ip,jp))
    
    # Find min distance points
    mind = 10000000
    for (x,y) in inr:
        # We can't reach this point
        if (x,y) not in dist:
            continue
        
        d = dist[(x,y)]
        if d < mind:
            mind = d
    
    # No points rechable
    if mind == 10000000:
        return None
    
    # Get all points with min distance
    upr = [(x,y) for (x,y) in inr if (x,y) in dist and dist[(x,y)] == mind]
    
    # Find first in "reading order"
    upr.sort()
    x,y = upr[0]
    return (x,y)

### HELPERS
def adjf(ip,jp,match = '.'):
    desc = []
    if ip - 1 >= 0:
        x,y = ip - 1, jp
        if grid[x][y] == match:
            desc.append((x,y))
    if jp - 1 >= 0:
        x,y = ip, jp - 1
        if grid[x][y] == match:
            desc.append((x,y))
    if ip + 1 < n:
        x,y = ip + 1, jp
        if grid[x][y] == match:
            desc.append((x,y))
    if jp + 1 < m:
        x,y = ip, jp + 1
        if grid[x][y] == match:
            desc.append((x,y))
    desc.sort()
    return desc   

def printgrid():
    g = grid
    
    hps = defaultdict(list)
    for (x,y,hp,t,a) in units:
        if not a:
            continue
        g[x][y] = t
        hps[x].append(hp)
    t = []
    b = []
    for i in range(0, m):
        if i < 10:
            t.append(' ')
        else:
            t.append(str(int(i / 10)))
        b.append(str(i % 10))
    print(''.join(t))
    print(''.join(b))
    for i,gs in enumerate(g):
        print(''.join(gs), str(i).zfill(2), ':', ','.join([str(x).rjust(3) for x in hps[i]]))

# Part 1
run(3)
# Part 2
# run(16)
    
