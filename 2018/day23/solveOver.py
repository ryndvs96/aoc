
from parse import compile
import random as r
import math

reg = compile("pos=<{},{},{}>, r={}")
s = input()
lines = []
while s != 'done':
    x,y,z,r = map(int, reg.parse(s))
    lines.append(((x,y,z),r))
    s = input()
    
def run(n_lines):
    sep = 20
    a,b,c = (0, 0, 0)
    # a,b,c = (450, 280, 490)
    # a,b,c = (4540, 2660, 5120)
    # a,b,c = (45580, 26520, 51230)
    # a,b,c = (455900, 265260, 512380)
    # a,b,c = (4559110, 2652590, 5123900)
    # a,b,c = (45591140, 26525960, 51239060)
    div = 10000000
    while div > 0:
        best_cell = (0,0,0)
        best_total = 0
        lines = scale(n_lines, div)
        print("Div =", div, "Anchor =", a, b, c)
        for x in range(-sep, sep):
            print("At x =", x)
            print("Best Cell", best_cell, "with total", best_total)
            for y in range(-sep, sep):
                for z in range(-sep, sep):
                    total = 0
                    for (p,r) in lines:
                        if dist(p, (a+x,b+y,c+z)) <= r:
                            total += 1
                    if total > best_total:
                        best_total = total
                        best_cell = (x+a,y+b,z+c)
        a,b,c = best_cell[0] * 10, best_cell[1] * 10, best_cell[2] * 10
        div = int(div / 10)
        print("Best Cell", best_cell, "with total", best_total, "and dist", dist(best_cell, (0,0,0)))
    
def dist(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) + abs(p1[2]-p2[2])

def scale(lines, div):
    # minx, maxx = -157807669, 256719117
    # miny, maxy =  -75904576, 172605678
    # minz, maxz = -105515361, 205521402
    # smallestx =       12899
    # smallesty =      190161
    # smallestz =          57
    
    # example radius 90808192
    new_lines = []
    for ((x,y,z), r) in lines:
        a = int(x / div)
        b = int(y / div)
        c = int(z / div)
        d = int(math.ceil(r / div)) # + 1
        new_lines.append(((a,b,c),d))
    return new_lines
        
run(lines)
