
import sys
sys.path.append('/Users/ryan/Code/competitive/algorithms')
import unionfind as UF

s = input()
lines = []
while s != 'done':
    x,y,z,t = map(int, s.split(','))
    lines.append((x,y,z,t))
    s = input()
    
def run(lines):
    uf = UF.UnionFind(lines)
    roots = uf.union_on(lambda x, y: dist(x, y) <= 3)
    print(len(roots))
    
def dist(p1, p2):
    a,b,c,d = p1
    x,y,z,t = p2
    return abs(a - x) + abs(b - y) + abs(c - z) + abs(d - t)
        
run(lines)
