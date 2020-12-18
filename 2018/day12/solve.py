
from parse import compile

s = input()
init = s[15:]
rules = {}

reg = compile("{} => {}")
s = input()
while s != 'done':
    f,v = reg.parse(s)
    # rule format: ###.. => .
    rules[f] = v
    s = input()

N = 500
pots = list(init + '.'*N)
# print(init)
for iter in range(0, 20):
    # print(''.join(pots[-10:]) + ''.join(pots[:125]))
    nxt = list('.' * len(pots))
    for i in range(0, len(pots)):
        pot = pots[i-2] + pots[i-1] + pots[i] + pots[(i+1)%len(pots)] + pots[(i+2)%len(pots)]
        nxt[i] = rules[pot] if pot in rules else '.'
    pots = nxt

pos = [i for i in range(-10, len(pots) - 10) if pots[i] == '#']
total = sum(pos)
print('Part 1:', total)

### Part 2
pots = list(init + '.'*N)
for iter in range(0, 200):
    nxt = list('.' * (len(init) + N))
    # pos = [i for i in range(0, len(pots)) if pots[i] == '#']
    # first,last = pos[0], pos[-1]
    # print('start index is', first, ''.join(pots[first:(last + 1)]))
    for i in range(0, len(pots)):
        pot = pots[i-2] + pots[i-1] + pots[i] + pots[(i+1)%len(pots)] + pots[(i+2)%len(pots)]
        nxt[i] = rules[pot]
    pots = nxt

pos = [i for i in range(0, len(pots)) if pots[i] == '#']
first,last = pos[0], pos[-1]

iter = 200
dist = first - 200 + 50000000000
pos = list(map(lambda x: x - first, pos))

print('Part 2:', sum(pos) + len(pos) * dist)

