
lines = []
n = input()
while n != 'done':
    lines.append(n)
    n = input()

twos = 0
threes = 0
for s in lines:
    counts = {}
    for k in s:
        if k in counts:
            counts[k] += 1
        else:
            counts[k] = 1
    for k in counts:
        if counts[k] == 2:
            twos += 1
            break
    for k in counts:
        if counts[k] == 3:
            threes += 1
            break

print(twos * threes)

