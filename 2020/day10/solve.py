
from parse import compile
from blist import blist

lines = []
n = input()
while n != 'done':
    lines.append(n)
    n = input()

jolts = blist([int(l) for l in lines])
jolts.append(0)
m = max(jolts)
jolts.append(m + 3)
jolts.sort()
print(jolts)

diff1 = 0
diff2 = 0
diff3 = 0
dels = 0

cand = []

for i, jolt in enumerate(jolts):
    if i == len(jolts) - 3:
        diffa = jolts[i+1] - jolt
        diffb = jolts[i+2] - jolts[i+1]
        diffc = 0
    elif i == len(jolts) - 2:
        diffa = jolts[i+1] - jolt
        diffb = 0
        diffc = 0
    elif i == len(jolts) - 1:
        diffa = 0
        diffb = 0
        diffc = 0
    else:
        diffa = jolts[i+1] - jolt
        diffb = jolts[i+2] - jolts[i+1]
        diffc = jolts[i+3] - jolts[i+2]
            
    a = i+1
    b = i+2
    # print('at {}, diffs are {}, {}, {}'.format(i, diffa, diffb, diffc))
    
    dells = []
    if diffa == 3:
        continue
    # if diffa == 2 and diffb == 1:
    #     dels += 1
    if diffa == 1:
        if diffb == 1:
            dels += 1
            cand.append(a)
        # if diffb == 1 and diffc == 1:
        #     dells.append((a,b))
    
# print(cand)

runs3p = 0
n = len(cand)
for i, c in enumerate(cand):
    consec = 1
    diff = 0
    for j, cj in enumerate(cand, i):
        if j == n - 1:
            break
        diff += cand[j + 1] - cand[j] 
        if diff > 3:
            break
        consec += 1
    # print('starting at {} we have consec {}'.format(i, consec))
    if consec >= 3:
        runs3p += (consec - 2)
        
        
        
# diff3 += 1
# print(dels, runs3p)
# print((2**dels) - runs3p)

def can_remove(i, js, offset=0):
    if i == 0:
        return False
    if i + 1 + offset >= len(js):
        return False
    if js[i + 1 + offset] - js[i - 1] <= 3:
        return True
    else: False

tots = [0 for i in range(len(jolts) + 1)]
currs = [0 for i in range(len(jolts) + 1)]
for i, jolt in enumerate(jolts, 1):
    curr = 0
    for j in range(0, 3):
        if can_remove(i, jolts, j):
            curr += 1
    # print('curr at {} is {}'.format(i, curr))
    currs[i] = curr
    for j in range(0, i - 3):
        curr += currs[j]
    if i > 2 and can_remove(i - 2, jolts):
        curr += 1
    tots[i] = curr + tots[i - 1]
            
# print(currs)
# print(tots)

cand = []
for i, j in enumerate(jolts):
    if can_remove(i, jolts):
        cand.append(1)
    else:
        cand.append(0)
        
tots = [0 for i in range(len(jolts))]
tots[0] = 1
tots[1] = can_remove(1, jolts) + 1
for i in range(2, len(jolts)):
    tots[i] = tots[i-1]
    if can_remove(i, jolts):
        tots[i] += tots[i-2]
    if can_remove(i - 1, jolts, 1):
        if i > 3:
            tots[i] += tots[i-3]
        else:
            tots[i] += 1
print(tots[-1])


    

    















    
    
    
    
    
    
    
    
    
    
    # ex
    