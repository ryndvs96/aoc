
lines = []
n = input()
i = 0
while n != 'done':
    s1,s2 = n.split(" must be finished before step ")
    s1 = s1[-1]
    s2 = s2[0]
    # [Step I] must be finished before step [U can begin.]
    lines.append((s1,s2))
    i += 1
    n = input()

g = {}
g['super'] = []
for (a,b) in lines:
    g['super'].append(a)
    g['super'].append(b)
    if a in g:
        g[a].append(b)
    else:
        g[a] = [b]

    if b not in g:
        g[b] = []


def solve1(g):
    #q = (d, n, odd)
    q = []
    q.append((0, 'super', 1))
    dist = [{}, {}]
    visit = [set(), set(['super'])]

    while len(q) > 0:
        # print(q)
        (d, n, odd) = q.pop(0)

        visit[odd].add(n)
        dist[odd][n] = d
        for m in g[n]:
            if m in visit[(odd + 1) % 2]:
                continue
            q.append((d + 1, m, (odd + 1) % 2))
        q.sort()
    return dist


def main(g):
    dist = solve1(g)
    for k in dist[0]:
        print("Dist odd to {} is {}".format(k, dist[0][k]))

main(g)

















# extend
