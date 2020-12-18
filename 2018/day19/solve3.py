
r1 = 10551300 # <-- n
r0 = 0
r5 = 1
while r5 <= r1:
    print(r5, r1, r0)
    r4 = 1
    while r4 <= r1:
        if (r4 * r5) == r1:
            r0 += r5
        r4 += 1
    r5 += 1    
print(r0)












