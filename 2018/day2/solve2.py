
lines = []
n = input()
while n != 'done':
    lines.append(n)
    n = input()

for n in lines:
    for m in lines:
        if n == m:
            continue

        same = 0
        for i in range(0, len(n)):
            same += 1 if n[i] == m[i] else 0

        
        if same == len(n) - 1:
            kk = ''
            for i in range(0, len(n)):
                if n[i] == m[i]:
                    kk += n[i]

            print(kk)
            break




