from parse import compile
from copy import copy, deepcopy
from collections import defaultdict, Counter, deque
from blist import *
import itertools
import math

s = input()
time = int(s)
buses = input()
buses = buses.split(',')

# 67 * c = 7 * d - 1 = 59 * e - 2 = 61 * f - 3 = X
# X = 67 * c
# X = 7 * d - 1
# X = 59 * e - 2
# X = 61 * f - 3
# 4X = (67 * c) + (7 * d - 1) + (59 * e - 2) + (61 * f - 3)
# 4X + 6 = 67c + 7d + 59e + 61f



def lcm(a):
    lcm = a[0]
    for i in a[1:]:
      lcm = lcm * i // math.gcd(lcm, i)
    return lcm

busdiff = []
busd = []
diff = 0
coefs = []
times = []
for b in buses:
    busdiff.append(diff)
    if b == 'x':
        busd.append(1)
    else:
        busd.append(int(b))
        times.append((int(b), diff))
    
    diff += 1
buses = busd

# 67
# 67 * 7 = 469, 469 - 1 = 468 
# 67 * 7 = 469
# 0, 67, 134, 201, 268, 335(336)
#335 + 469 

start = 0
add = times[0][0]
for k, (t, t_offset) in enumerate(times[1:], 1):
    while ((start + t_offset) % t) != 0:
        start += add
    add *= t
print(start)















# hello