
tic = 0
def inc():
    global tic,r0,r1,r2,ip,r4,r5
    tic += 1
    ip += 1
    if tic % 100000 == 0:
        print(tic, r0,r1,r2,ip,r4,r5)
    
    

ip = 0
r0,r1,r2,ip,r4,r5 = (1,0,0,0,0,0)
# START
# op 0
ip = 16
inc()
# op 17
r1 += 2
inc()
# op 18
r1 = r1 * r1
inc()
# op 19
r1 = r1 * ip
inc()
# op 20
r1 = r1 * 11
inc()
# op 21
r2 = r2 + 2
inc()
# op 22
r2 = ip * r2
inc()
# op 23
r2 = r2 + 20
inc()
# op 24
r1 = r2 + r1
inc()
# op 25
ip = r0 + ip
inc()
# op 27
r2 = ip
inc()
# op 28
r2 = ip * r2
inc()
# op 29
r2 = ip + r2
inc()
# op 30
r2 = ip * r2
inc()
# op 31
r2 = r2 * 14
inc()
# op 32
r2 = ip * r2
inc()
# op 33
r1 = r2 + r1
inc()
# op 34
r0 = 0
inc()
# op 35
ip = 0
inc()
# op 1
r5 = 1
inc()
# op 2 (loop start)
while True:
    r4 = 1
    inc()
    # op 3 (loop start)
    while True:
        r2 = r4 * r5
        inc()
        # op 4
        r2 = 1 if r1 == r2 else 0
        inc()
        # op 5
        ip = ip + r2
        inc()
        if r2 == 0:
            # op 6
            ip = ip + 1
            inc()
        elif r2 == 1:
            # op 7
            r0 = r5 + r0
            inc()
        # op 8
        r4 = r4 + 1
        inc()
        # op 9
        r2 = 1 if r4 > r1 else 0
        inc()
        # op 10
        ip = ip + r2
        inc()
        if r2 == 0:
            # op 11
            ip = 2
            inc()
            # op 3 (loop)
        else:
            inc()
            break
    # op 12
    r5 = r5 + 1
    inc()
    # op 13
    r2 = 1 if r5 > r1 else 0
    inc()
    # op 14
    ip = ip + r2
    inc()
    if r2 == 0:
        # op 15
        ip = 1
        inc()
        # op 2 (loop)
    else:
        inc()
        break
    
print(r0)












