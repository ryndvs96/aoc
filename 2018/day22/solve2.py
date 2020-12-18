
from blist import *
import sys
sys.path.append('/Users/ryan/Code/competitive/algorithms')
import shortestpath as sp


### Setup Input
depth = 3879
# depth = 510
dx, dy = depth, depth
# depth_x, depth_y = 200, 1500
x, y = 8, 713
# x,y, = 10,10

# map from erosion level to tools
# 0, 1, 2 are rocky, wet, narrow
# 0, 1, 2 are torch, climb, none
tools = {
    0 : [0, 1],
    1 : [1, 2],
    2 : [0, 2] 
} 

def run():
    grid = build_grid()
    
    dist = {}
    q = [(0,0,0,0)]
    while len(q) > 0:
        (d,i,j,tool) = heapq.heappop(q)
        if (i,j,tool) in dist:
            continue
        print("Processing node {},{} at distance {}.".format(i,j,d))
        if (i,j,tool) == (x,y,0):
            print("Found {},{} at distance {}.".format(x,y,d))
            exit()
        dist[(i,j,tool)] = d
            
        # Add adjacent nodes
        for (time,ip,jp,toolp) in adj(i,j,tool,grid):
            if (ip,jp,toolp) in dist:
                continue
            heapq.heappush(q, (time + d, ip, jp, toolp))
    
def adj(i,j,tool,grid):
    global dx, dy
    desc = []
    if i > 0 and tool in tools[grid[i-1][j]]:
        desc.append((1,i-1,j,tool))
    if i < dx and tool in tools[grid[i+1][j]]:
        desc.append((1,i+1,j,tool))
    if j > 0 and tool in tools[grid[i][j-1]]:
        desc.append((1,i,j-1,tool))
    if j < dy and tool in tools[grid[i][j+1]]:
        desc.append((1,i,j+1,tool))
    for t in tools[grid[i][j]]:
        if t != tool:
            desc.append((7,i,j,t))
    return desc

def build_grid():
    global dx, dy, x, y
    grid = [[0 for i in range(0, dy + 1)] for j in range(0, dx + 1)]
    for i in range(0, dx + 1):
        print("Creating row {} of {}".format(i, dx))
        for j in range(0, dy + 1):
            if (i,j) == (0,0) or (i,j) == (x,y):
                grid[i][j] = 0
            elif i == 0:
                grid[i][j] = 48271 * j
            elif j == 0:
                grid[i][j] = 16807 * i
            else:
                grid[i][j] = e_level(grid[i-1][j]) * e_level(grid[i][j-1])

    for i in range(0, dx + 1):
        for j in range(0, dy + 1):
            grid[i][j] = e_level(grid[i][j]) % 3
    return grid
    
def e_level(geo):
    global depth
    return (geo + depth) % 20183
    
run()












