# /Users/ryan/Code/competitive/advent2019/day12

from parse import compile
from blist import blist
from copy import deepcopy

s = input()
lines = []
while s != 'done':
    lines.append(s)
    s = input()

faces = {}
faces[0] = 'E'
faces[90] = 'N'
faces[180] = 'W'
faces[270] = 'S'

facing = 0
actions = []
for l in lines:
    dir = l[0]
    num = l[1:]
    actions.append((dir, int(num)))

def moven(x,y,dir,c):
    if dir == 'N':
        y += c
    elif dir == 'S':
        y -= c
    elif dir == 'E':
        x += c
    elif dir == 'W':
        x -= c
    return (x,y)
    
def move(x,y,cx,cy,multiplier):
    # print(x,y,cx,cy,multiplier)
    nx = x + cx * multiplier
    ny = y + cy * multiplier
    return (nx,ny)


def rotate(face, degrees, dir, x, y):
    # (10, 4)
    
    #L90 -> (-4, 10) L90 -> (-10, -4)
    #R90
    # (4, -10)
    if dir == 'L':
        while degrees > 0:
            (x,y) = (0 - y, x)
            degrees -= 90
        return (x,y)
    elif dir == 'R':
        while degrees > 0:
            (x,y) = (y, 0 - x)
            degrees -= 90
        return (x,y)
    else:
        return None
        

wx,wy = 10, 1
x,y = 0, 0
for (dir, c) in actions:
    print(dir,c)
    if dir == 'L' or dir == 'R':
        wx,wy = rotate(facing, c, dir,wx,wy)
    elif dir == 'F':
        x,y = move(x,y,wx,wy,c)
    else:
        wx,wy = moven(wx,wy,dir,c)
    print('loc', x,y, 'diff', wx, wy)

print(x,y)
print(abs(x) + abs(y))
        
        
