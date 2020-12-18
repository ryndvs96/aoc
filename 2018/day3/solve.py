
lines = []
n = input()
while n != 'done':
    s = n.split(" ")
    a,b,c = s[0], s[2], s[3]
    left,top = map(int, b[:-1].split(","))
    width,height = map(int, c.split("x"))
    lines.append((a,left,top,width,height))
    n = input()

grid = [[set() for i in range(0, 1100)] for j in range(0, 1100)]

tot = 0
for s in lines:
    (a, l, t, w, h) = s
    for i in range(t, t + h):
        for j in range(l, l + w):
            grid[i][j].add(a)

single = set()
cannot_be = set()
for i in range(0, 1100):
    for j in range(0, 1100):
        if len(grid[i][j]) == 1:
            single |= grid[i][j]
        else:
            cannot_be |= grid[i][j]

print(single - cannot_be)




