
freqs = []
n = input()
while n != 'd':
    freqs.append(int(n))
    n = input()

f = 0
s = set([0])
found = False
while not found:
    for n in freqs:
        f += n
        if f in s:
            print(f)
            found = True
            break
        s.add(f)
