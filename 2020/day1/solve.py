
lines = []
n = input()
while n != 'done':
    lines.append(n)
    n = input()

def func(x):
    if x <= 0:
        return 0
    y = int(x / 3) - 2
    return y

tot = [func(int(x)) for x in lines]

print(sum(tot))

