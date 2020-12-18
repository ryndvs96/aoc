
s = input()
ords = s.split(",")

def run(ords):
    nw,n,ne = 0,0,0
    for o in ords:
        if o == 'n':
            n += 1
        elif o == 'ne':
            ne += 1
        elif o == 'se':
            nw -= 1
        elif o == 's':
            n -= 1
        elif o == 'sw':
            ne -= 1
        elif o == 'nw':
            nw += 1
    
    l = [abs(nw), abs(n), abs(ne)]
    return sum(l) - min(l)

m = 0
for i in range(1, len(ords) + 1):
    m = max(m, run(ords[:i]))
    print(m)
    


            
