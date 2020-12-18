
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

print(rec(line))
