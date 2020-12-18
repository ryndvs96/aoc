# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None
#         self.prev = None
import re
linere = re.compile('[a-z]+')
# m = linere.match(l)
# if m:
#   m.group(0)

lines = []
n = input()
while n != 'done':
    lines.append(n)
    n = input()
    
preamblelen = 25
i = 0
nums = []
for l in lines:
    nums.append(int(l))
    
# for i in range(preamblelen, len(nums)):
#     issum = False
#     for j in range(i - preamblelen - 1, i):
#         for k in range(j + 1, i):
#             if nums[j] + nums[k] == nums[i]:
#                 print(nums[i], '=', nums[j], '+', nums[k])
#                 issum = True
#     if not issum:
#         print(nums[i])
#         break

t = 556543474
for i in range(len(nums)):
    tot = 0
    j = i
    while tot < t:
        tot += nums[j]
        j += 1
    if tot > t:
        continue
    if tot == t:
        vals = [nums[k] for k in range(i, j)]
        print(i, j, max(vals) + min(vals))
        

