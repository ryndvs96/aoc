
lines = []
n = input()
while n != 'done':
    lines.append(n)
    n = input()
    
groups = []
curr = []
for i in range(len(lines)):
    l = lines[i]
    if l == '':
        groups.append(curr)
        curr = []
    elif i == len(lines) - 1:
        curr.append(l)
        groups.append(curr)
    else:
        curr.append(l)
        

sets = []        
for g in groups:
    s = None
    for l in g:
        ss = set(l)
        if s is None:
            s = ss
        else:
            s = s.intersection(ss)
    sets.append(s)
    print(g)
    print(len(s))

print(sum([len(x) for x in sets]))