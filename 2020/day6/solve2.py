
lines = []
n = input()
i = -1
while n != 'done':
    x,y = map(int, n.split(", "))

    lines.append((i, x,y))
    i -= 1
    n = input()

grid = [[1 for i in range(0, 400)] for j in range(0, 400)]

count = 0
for i in range(0, 400):
    print("row", i)
    for j in range(0, 400):
        s = 0
        for k,x,y in lines:
            s += abs(x - i) + abs(y - j)
        grid[i][j] = s
        if s < 10000:
            count += 1

for g in grid[:50]:
    print(" ".join(map(str, g[:50])))
print(count)

