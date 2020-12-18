
from parse import compile

# position=< -9982, -30288> velocity=< 1,  3>
reg = compile("position=<{}, {}> velocity=<{}, {}>")
s = input()
xs = []
ys = []
vxs = []
vys = []
while s != 'done':
    y,x,vy,vx = map(lambda x: int(x.strip()), reg.parse(s))
    xs.append(x)
    ys.append(y)
    vxs.append(vx)    
    vys.append(vy)
    s = input()

# max box
prev_mb = 10000000000000
mb = (max(xs) - min(xs)) * (max(ys) - min(xs))

j = 0
while mb < prev_mb:
    print(j, mb)
    # update locs
    for i in range(0, len(xs)):
        xs[i] += vxs[i]
        ys[i] += vys[i]
    
    j += 1
    prev_mb = mb
    mb = (max(xs) - min(xs)) * (max(ys) - min(xs))
    
for i in range(0, len(xs)):
    xs[i] -= vxs[i]
    ys[i] -= vys[i]
    
minx, maxx = min(xs), max(xs)
miny, maxy = min(ys), max(ys)
totx = maxx - minx + 1
toty = maxy - miny + 1

grid = [[' ' for i in range(0, toty)] for j in range(0, totx)]
for x,y in zip(xs,ys):
    grid[x - minx][y - miny] = '0'
for g in grid:
    print(''.join(g))

    
    
    
    
    
    
    
    
    
    
    # ex
    