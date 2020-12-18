
from copy import copy, deepcopy
from collections import defaultdict, deque, Counter
# from blist import *
from parse import compile


def run():
    s = input()
    nodes = parse_group(s)
    visited = set()
    adj = defaultdict(set)
    for n in nodes:
        run_grid(0,0,n,adj,visited)
    
    print_graph(adj)
        
    sps = sp(adj)
    m = 0
    for (i,j) in sps:
        if sps[(i,j)] >= 1000:
            m += 1
    print(m)
    
def print_graph(adj):
    mini, minj = 0,0
    maxi, maxj = 0,0
    for (i,j) in adj:
        mini,minj = min(mini, i), min(minj, j)
        maxi,maxj = max(maxi, i), max(maxj, j)
        for (l,m) in adj[(i,j)]:
            mini,minj = min(mini, l), min(minj,m)
            maxi,maxj = max(maxi, l), max(maxj, m)
    n = maxi - mini + 1
    m = maxj - minj + 1
    graph = Graph(n,m, 0 -mini, 0 - minj)
    for (i,j) in adj:
        for (l,m) in adj[(i,j)]:
            graph.connect(i - mini,j - minj,l - mini,m - minj)
    graph.print_me()
    
class Graph:
    def __init__(self, n, m, x,y):
        self.x = x
        self.y = y
        self.height = 2*n + 1
        self.width = 2*m + 1
        # +-+-+-+
        # | | | |
        # +-+-+-+
        # | | | |  3x3 example
        # +-+-+-+
        # | | | |
        # +-+-+-+
        self.grid = []
        for i in range(0, self.height):
            row = []
            if i % 2 == 0:
                for j in range(0, self.width):
                    if j % 2 == 0:
                        row.append('+')
                    else:
                        row.append('-')
            else:
                for j in range(0, self.width):
                    if j % 2 == 0:
                        row.append('|')
                    else:
                        row.append(' ')
            self.grid.append(row)
    
    def print_me(self):
        self.grid[self.x][self.y] = 'X'
        for g in self.grid:
            print(''.join(g))
        
    
    def connect(self,i,j,ip,jp):
        # map to our coords (0,0) -> (1,1), (1,2) -> (3,5)
        i,j,ip,jp = map(lambda x: x*2 + 1, (i,j,ip,jp))
        # break down wall
        # print(i,j,ip,jp)
        if i < ip:
            self.grid[i+1][j] = ' '
        elif i > ip:
            self.grid[ip+1][j] = ' '
        elif j > jp:
            self.grid[i][jp+1] = ' '
        elif j < jp:
            self.grid[i][j+1] = ' '
    
def sp(adj):
    dist = {}
    queue = [(0,0,0)]
    while len(queue) != 0:
        queue.sort()
        (d,i,j) = queue.pop()
        if (i,j) in dist:
            continue
        dist[(i,j)] = d
        for (l,m) in adj[(i,j)]:
            if (l,m) in dist:
                continue
            else:
                queue.append((d+1,l,m))
    return dist

def run_grid(i,j,node, adj,visited):
    if (i,j,node) in visited:
        return
    visited.add((i,j,node))
    for dir in node.dirs:
        if dir == 'N':
            adj[(i,j)].add((i-1,j))
            i -= 1
        if dir == 'S':
            adj[(i,j)].add((i+1,j))
            i += 1
        if dir == 'E':
            adj[(i,j)].add((i,j+1))
            j += 1
        if dir == 'W':
            adj[(i,j)].add((i,j-1))
            j -= 1
    for n in node.children:
        run_grid(i,j,n,adj,visited)
        
class Node:
    def __init__(self, dirs=None):
        self.dirs = dirs
        self.children = []
        self.count = None
    def counts(self):
        if self.count != None:
            return self.count
        self.count = 1
        if len(self.children) > 0:
            self.count += sum([n.counts() for n in self.children])
        return self.count

def print_nodes(nodes, ind = 0):
    for n in nodes:
        print_node(n, ind)
                
def print_node(node, ind = 0):
    print(" "*ind + node.dirs + " " + str(node.counts()))
    print_nodes(node.children, ind + 1)

def parse_node(s):
    start = -1
    curr = ''
    for i in range(0, len(s)):
        if s[i] == '(':
            start = i
            break
        else:
            curr += s[i]
    root = Node(curr)
    if start == -1:
        return root
        
    # find children
    stack = 0
    end = -1
    for i in range(start,len(s)):
        if s[i] == '(':
            stack += 1
        elif s[i] == ')':
            stack -= 1
            if stack < 0:
                print("ERRRROR")
        if stack == 0:
            end = i
            break
    if end == -1:
        print("Something went wrong")
        
    root.children = parse_group(s[start+1:end])
    if end != len(s)-1:
        c = parse_node(s[(end+1):])
        for r in root.children:
            r.children.append(c)
    return root

def parse_group(s):
    nodes = []
    stack = 0
    end = -1
    for i in range(0, len(s)):
        if s[i] == '|' and stack == 0:
            end = i
            break
        elif s[i] == '(':
            stack += 1
        elif s[i] == ')':
            stack -= 1
            if stack < 0:
                print("ERRRROR")
    if end == -1:
        nodes.append(parse_node(s))
    else:
        nodes.append(parse_node(s[:end]))
        nodes.extend(parse_group(s[(end+1):]))
    return nodes
        
run()
