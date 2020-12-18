
def power(x,y):
    serial = 2018 # 7803
    rank = x + 10
    pow = (rank * y + serial) * rank
    pow = int(pow / 100) % 10
    return pow - 5

N = 300

# compute powers
g = [[0 for i in range(0, N)] for j in range(0, N)]
for x in range(0, N):
    for y in range(0, N):
        g[x][y] = power(x+1,y+1)

# part 1
maxp, maxx, maxy = 0,None,None
for x in range(0, N - 3):
    for y in range(0, N - 3):
        p = 0
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                p += g[i][j]
        if p > maxp:
            maxp,maxx,maxy = p,x+1,y+1
print("Part1: {},{}".format(maxx,maxy))

# part 2
# prefix sums from top left corner to [i,j]
pre = [[0 for i in range(0, N)] for j in range(0, N)]
pre[0][0] = g[1][1]
for i in range(0, N):
    pre[i][0] = pre[i-1][0] + g[i][0]
    for j in range(1, N):
        pre[i][j] = pre[i-1][j] + pre[i][j-1] - pre[i-1][j-1] + g[i][j]

def prep(x,y):
    if x < 0 or y < 0:
        return 0
    return pre[x][y]
    
# compute max
maxp, maxx, maxy, maxsize = 0, None, None, None
for x in range(0, N):
    for y in range(0, N):
        p, size = 0, None
        for w in range(0, N - max(x,y)):
            v = prep(x+w, y+w) - prep(x-1,y+w) - prep(x+w,y-1) + prep(x-1,y-1)
            if v > p:
                p,size = v,w+1
        if p > maxp:
            maxp,maxx,maxy,maxsize = p,x+1,y+1,size
print("Part2: ({},{}) with width {} and total size {}".format(maxx,maxy,maxsize,maxp))
            