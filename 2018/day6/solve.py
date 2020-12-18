
lines = []
n = input()
i = -1
while n != 'done':
    x,y = map(int, n.split(", "))

    lines.append((i, x,y))
    i -= 1
    n = input()

grid = [[0 for i in range(0, 400)] for j in range(0, 400)]

loc = {}
for k,x,y in lines:
    grid[x][y] = k
    loc[abs(k)] = (x,y)
    print(k, x, y)
    for i in range(0, 400):
        for j in range(0, 400):
            if str(grid[i][j])[0] == '.':
                dist = int(str(grid[i][j])[1:])
                if abs(x - i) + abs(y - j) < dist:
                    grid[i][j] = abs(k)
                continue
            if grid[i][j] == 0:
                grid[i][j] = abs(k)
            if grid[i][j] < 0:
                continue
            if grid[i][j] > 0:
                vx,vy = loc[grid[i][j]]
                if abs(vx - i) + abs(vy - j) > abs(x - i) + abs(y - j):
                    grid[i][j] = abs(k)
                elif abs(vx - i) + abs(vy - j) == abs(x - i) + abs(y - j):
                    if abs(grid[i][j]) != abs(k):
                        grid[i][j] = '.' + str((abs(x - i) + abs(y - j)))

for i in range(0, 400):
    for j in range(0, 400):
        if str(grid[i][j])[0] == '.':
            grid[i][j] = '.'
for g in grid[:50]:
    print(" ".join(map(str, g[:50])))

cannot_be = set()
for i in range(0, 400):
    if grid[i][0] != '.':
        cannot_be.add(abs(grid[i][0]))
    if grid[i][399] != '.':
        cannot_be.add(abs(grid[i][399]))
    if grid[0][i] != '.':
        cannot_be.add(abs(grid[0][i]))
    if grid[399][i] != '.':
        cannot_be.add(abs(grid[399][i]))


n = len(lines)
count = {}
for k in range(0, n):
    if k in cannot_be:
        continue
    count[k] = 0
    for i in range(0, 400):
        for j in range(0, 400):
            if grid[i][j] == '.':
                continue
            if abs(grid[i][j]) == k:
                count[k] += 1

ma = 0
for k in count:
    ma = max(ma, count[k])

print(ma)
