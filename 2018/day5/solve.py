
line = input()

def rec(s):
    while True:
        if s == '':
            return s
        n = len(s)
        print(n)
        rem = None
        for j in range(1, n):
            i = j - 1
            if s[i] != s[j] and s[i].lower() == s[j].lower():
                rem = i
       
        if rem == None:
            return s
        s = s[:rem] + s[rem+2:]

print(rec(line))
