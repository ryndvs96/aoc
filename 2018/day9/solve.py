
# 424 players; last marble is worth 71482 points
ps = 424
ls = 7148200

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

circ = Node(0)
circ.next = Node(1)
circ.next.next = circ
circ.prev = circ.next
circ.next.prev = circ
scores = [0 for i in range(0, ps + 1)]
p = 1
curr = circ.next

def printcirc():
    stop = circ.data
    curr = circ.next
    while curr.data != stop:
        print(curr.data, curr.next, curr.prev)
        curr = curr.next

for i in range(2, ls + 1):
    # print("i", i)
    if i % 100000 == 0:
        print("i", i)
    p += 1
    if p == ps + 1:
        p = 1
    if i % 23 == 0:
        # go back 7
        for j in range(0, 7):
            curr = curr.prev
        val = curr.data
        pr = curr.prev
        ne = curr.next
        pr.next = ne
        ne.prev = pr
        curr = ne
        scores[p] += val + i
    else:
        one = curr.next
        # printcirc()
        two = curr.next.next
        one.next = Node(i)
        one.next.next = two
        one.next.prev = one
        two.prev = one.next
        curr = one.next
    

print(max(scores))


