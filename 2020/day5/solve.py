
import re
def extract_line(s):
    pattern = re.compile(r"(?P<name>.*)", re.VERBOSE)
    match = pattern.match(s)

    name = match.group("name")
    n1 = float(match.group("n1"))
    n2 = float(match.group("n2"))

    return (name, n1, n2)

lines = []
n = input()
while n != 'done':
    lines.append(n)
    n = input()

def conv(n):
    t = 0
    for i in range(len(n)):
        k = len(n) - i - 1
        if n[k] == 'B' or n[k] == 'R':
            t += (2**i)
    return t


grid = [[0 for i in range(8)] for j in range(128)]
seats = []
for l in lines:
    rowss = l[0:7]

    row = conv(rowss)
    
    colss = l[7:11]

    col = conv(colss)
    grid[row][col] = 1
    seats.append((row * 8) + col)
    
for i in range(128):
    for j in range(8):
        if grid[i][j] != 1:
            print(i, j, (i * 8) + j)

    
print(max(seats))

# 78*247*68*69*33

    


