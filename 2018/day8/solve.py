
nums = list(map(int,input().split(" ")))

child = {}  # child[i] is indices of children (in nums) for node i
meta = {}   # meta[i] is the value of metadata entries for node i
def parse(i):
    cs = nums[i]     # number of children
    ms = nums[i+1]   # number of metadata entries
    start = i + 2   # start index of child nodes
    child[i] = []
    meta[i] = []

    # process child nodes
    for c in range(0, cs):
        child[i].append(start)
        start = parse(start)  # update where next child node starts

    # process metadata
    for m in range(start, start + ms):
        meta[i].append(nums[m])

    # return the index where this node's data ends (1 after technically)
    return (start + ms)

# solution to 1
def solve1():
    return sum([sum(meta[k]) for k in meta])

# solution to 2, recursive
def solve2(i):
    if len(child[i]) == 0:
        return sum(meta[i])
    else:
        return sum([solve2(child[i][m - 1]) for m in meta[i] if m <= len(child[i])])

parse(0)
print(solve1(), solve2(0))


















#extend
