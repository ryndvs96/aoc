
lines = []
n = input()
while n != 'done':
    lines.append(n)
    n = input()

valid = 0
for l in lines:
    sp = l.split(' ')
    pol = sp[0]
    pol1 = pol.split('-')
    pol = (int(pol1[0]) - 1, int(pol1[1]) - 1)
    
    let = sp[1][0]
    
    pwd = sp[2]

    ct = 0
    if pwd[pol[0]] == let:
        ct += 1
    if pwd[pol[1]] == let:
        ct += 1
    
    if ct == 1:
        valid += 1

print(valid)
    


