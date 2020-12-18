
lines = []
n = input()
i = 0
while n != 'done':
    s1,s2 = n.split(" must be finished before step ")
    s1 = s1[-1]
    s2 = s2[0]
    # [Step I] must be finished before step [U can begin.]
    lines.append((s2,s1))
    i += 1
    n = input()

g = {}
p = {}
for (a,b) in lines:
    if a in g:
        g[a].append(b)
    else:
        g[a] = [b]

    if b not in g:
        g[b] = []
p = g
# p is parent graph
# strip nodes with no children
q = []
for a in p:
    if len(p[a]) == 0:
        q.append(a)
q.sort()
o = []
while len(q) > 0:
    print("queue =", q)
    root = q.pop(0)

    o.append(root)
    p.pop(root)
    for a in p:
        if root in p[a]:
            p[a].remove(root)
    for a in p:
        if len(p[a]) == 0:
            q.append(a)
    x = set(q)
    q = list(x)
    q.sort()
print("order", "".join(o))
