from parse import compile
from copy import copy, deepcopy
from collections import defaultdict, Counter, deque
from blist import *
import itertools
import math

def find(arr, num):
    n = len(arr) - 2
    while n > -1:
        if arr[n] == num:
            return n
        n -= 1
    return -1

def default():
    return -1

most_recent = defaultdict(default)
second_most_recent = defaultdict(default)
nums = [0]
# nums = [0,14,1,3,7,9]
# for i, n in enumerate(nums[0:-1]):
#     most_recent[n] = i
# # 
# print(most_recent)
# 
# # while len(nums) < 30000000:
# while len(nums) < 50:
#     n = len(nums)
#     if n % 100000 == 0:
#         print(n)
#     last = nums[-1]
#     age = most_recent[last]
#     if n < 20:
#         print(most_recent)
#         print(last, age)
#     if age >= 0:
#         num = n - age - 1
#         most_recent[last] = n - 1
#         nums.append(num)
#     else:
#         most_recent[last] = n - 1
#         nums.append(0)
    
# A181391 = [0]
# A181391 = [0,3,6]
A181391 = [0,14,1,3,7,9]
total = 30000000
last_pos = {}
for i, value in enumerate(A181391[:-1]):
    last_pos[value] = i
for i in range(len(A181391) - 1, total - 1):
    if i % 100000 == 0:
        print(i)
    new_value = i - last_pos.get(A181391[i], i)
    A181391.append(new_value)
    if new_value == 16:
        print(len(A181391), 16)
        break
    last_pos[A181391[i]] = i
print(A181391[-1])
    
# print(nums)
i = 0
# for k in most_recent:
#     i += 1
#     if i > 20:
#         break
#     print(k, most_recent[k])
# print(nums[0:20])
# print(nums[-20:-1])
# print(nums[-1])
# print(nums)