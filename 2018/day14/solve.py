
from copy import copy, deepcopy
from collections import defaultdict, Counter, deque
from blist import *

s = 327901
l = "327901"
b = blist([3,7])
b[0] = 3
b[1] = 7

i = 0
j = 1
base = 0
n = 2
while True:
    if n % 100000 == 0:
        print(n)
    new = b[i - base] + b[j - base]
    if new >= 10:
        b.append(1)
        n += 1
    b.append(new % 10)
    n += 1
    
    pi = (i + b[i - base] + 1) % n
    pj = (j + b[j - base] + 1) % n
    # print('piiii',b[i-base], base, pi,pj,i,j)
    i,j = pi,pj
    if n < 50:
        nb = 0
    else:
        nb = min(i,j)
    # b = b[(nb-base):]
    base = 0
    # print(n, i, j, base, b)
    bx = ''.join([str(b[i - base]) for i in range(n - 6, n)])
    bxp = ''.join([str(b[i - base]) for i in range(n - 7, n - 1)])
    # print(n, bx, bxp, l)
    # print(l, bx, bxp)
    # print(b)
    if l == bx:
        print("found bx", n - len(l))
        print(l, bx, bxp)
        c = 0
        break
    if l == bxp:
        print("found bxp", n - len(l))
        print(l, bx)
        c = 0
        break
        
        
        
    
    
    


    

    