
lines = []
n = input()
while n != 'done':
    lines.append(n)
    n = input()

aa = list(map(int, lines[0].split(',')))

for j in range(0, 100):
    for k in range(0, 100):
        a = list(aa)
        a[1], a[2] = j, k
        i = 0
        while True:
            v = a[i]
            if v == 99:
                break
            b, c, d = a[i + 1], a[i + 2], a[i + 3]
            if v == 1:
                a[d] = a[b] + a[c]
            elif v == 2:
                a[d] = a[b] * a[c]
            else:
                # print("err", j, k)
                break
            i += 4
        if a[0] == 19690720:
            print("done", j, k)
            break
    
print(a[0])

