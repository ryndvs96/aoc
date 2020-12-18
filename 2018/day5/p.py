
line = input()

def rec(s):
    lj = 1
    while True:
        if s == '':
            return s
        n = len(s)
        print(n)
        rem = None
        for j in range(lj, n):
            i = j - 1
            if s[i] != s[j] and s[i].lower() == s[j].lower():
                rem = i
                break
        if rem == None:
            for j in range(1, lj):
                i = j - 1
                if s[i] != s[j] and s[i].lower() == s[j].lower():
                    rem = i
                    break
        lj = j
        if rem == None:
            return s
        s = s[:rem] + s[rem+2:]

s = rec(line)
chars = set([c for c in s.lower()])
m = len(s)
print(m)
for c in chars:
    sp = [k for k in s if k.lower() != c]
    spp = rec(sp)
    print("removing: ", c, ' got', len(spp))

    if len(spp) < m:
        m = len(spp)

print(m)



