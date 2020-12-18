
lines = []
n = input()
while n != 'done':
    # [1518-10-16 00:02] Guard #1601 begins shift
    # [1518-06-17 00:30] wakes up
    s = n.split(" ")
    date = s[0][1:]
    time = s[1][:-1]
    hour, minute = map(int, time.split(":"))
    wake = None
    num = None
    if s[2] == "wakes":
        wake = True
    elif s[2] == "falls":
        wake = False
    else:
        num = s[3][1:]

    lines.append((date, hour, minute, wake, num))
    n = input()

lines.sort()

ps = {}
p = None
for i in range(0, len(lines)):
    print(lines[i])
    (date, hour, minute, wake, num) = lines[i]
    if num is not None:
        p = num
        continue

    if not wake:
        (date, hour, done, wake, num) = lines[i+1]
        print("Player {} falls asleep at {}, wakes up at {}".format(p, minute, done))
        if p in ps:
            for j in range(minute, done):
                ps[p][j] += 1
        else:
            ps[p] = [0 for i in range(0, 60)]
            for j in range(minute, done):
                ps[p][j] += 1
m = 0
mi = None
for p in ps:
    s = sum(ps[p])
    print("Player {} slept {} time: {}".format(p, s, ps[p]))
    if sum(ps[p]) > m or mi == None:
        m = sum(ps[p])
        mi = p

print(mi, ps[mi])
for i in rang
print(int(mi) * max(ps[mi]))

