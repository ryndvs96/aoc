
lines = []
n = input()
while n != 'done':
    lines.append(n)
    n = input()

def find2020(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[k] + nums[i] + nums[j] == 2020:
                    print(nums[i] * nums[j] * nums[k])

nums = [int(x) for x in lines]
find2020(nums)

