
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

# work on all with no dependencies
q = []
for a in p:
    if len(p[a]) == 0:
        q.append((a,0))
q.sort()
window = []

cost = {}
i = 0
while len(q) > 0:
    i += 1
    # fill window
    while len(q) > 0 and len(window) < 5:
        window.append(q.pop(0))
    window.sort()

    # complete tasks in window
    for (w,s) in window:
        c = ord(w) - 4
        cost[w] = c + s
        print("window", i, w, cost[w])

        for a in p:
            # delete task from others' dependencies
            if w in p[a]:
                p[a].remove(w)
                # if that was the last dependency, add a to queue
                if len(p[a]) == 0:
                    # last one
                    q.append((a, cost[w]))
    window = []

    x = set(q)
    q = list(x)
    q.sort()
