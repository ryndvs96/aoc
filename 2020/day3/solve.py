
lines = []
n = input()
while n != 'done':
    lines.append(n)
    n = input()

grid = []
for l in lines:
    row = [0 if x == '.' else 1 for x in l]
    grid.append(row)
    
trees = 0
i,j = (0, 0)
width = len(grid[0])
while i < len(grid):
    trees += grid[i][j]
    i += 2
    j += 1
    j = j % width
print(trees)

# 78*247*68*69*33

    


