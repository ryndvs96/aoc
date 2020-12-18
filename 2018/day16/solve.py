
from copy import copy, deepcopy
from collections import defaultdict, deque, Counter
from blist import *
from parse import compile

# Before: [2, 3, 2, 2]
# 0 3 3 0
# After:  [0, 3, 2, 2]
#

# s = input()
# 
# reg = compile("{} => {}")
# f,v = reg.parse(s)

regb = compile("Before: [{}, {}, {}, {}]")
rega = compile("After:  [{}, {}, {}, {}]")

s = input()
tests = []
while s != 'done pt1':
    (a,b,c,d) = map(int, regb.parse(s))
    (e,f,g,h) = map(int, input().split(" "))
    (i,j,k,l) = map(int, rega.parse(input()))
    tests.append(([a,b,c,d], (e,f,g,h), [i,j,k,l]))
    input()
    s = input()
    
ins = []
s = input()
while s != 'done pt2':
    (i,a,b,c) = map(int, s.split(" "))
    ins.append((i,a,b,c))
    s = input()

codes = defaultdict(set)
final = dict()
    
def run():
    tot = 0
    for (i,(d,a,b,c),out) in tests:
        t = 0
        corr = set()
        for (f,n) in funcs:
            if out == f(a,b,c,i):
                corr.add(f)
        if len(corr) > 2:
            tot += 1
        codes[d] |= corr
    print("Part 1", tot)
    while len(final) != 16:
        for i, s in codes.items():
            if len(s) == 1:
                final[i] = s.pop()
        for i, fs in final.items():
            for j, s in codes.items():
                if j == i:
                    continue
                if fs in s:
                    s.remove(fs)
    
    # for i in codes:
    #     final[i] = codes[i].pop()
    
    for i in range(0, 16):
        print(i, final[i])
                
    reg = [0,0,0,0]
    for (i,a,b,c) in ins:
        print("Processing", i, a, b, c, "with", reg, final[i])
        reg = final[i](a,b,c,reg)
    print(reg[0])
    
def addr(a,b,c,nreg):
    reg = copy(nreg)
    reg[c] = reg[a] + reg[b]
    return reg
    
def addi(a,b,c,nreg):
    reg = copy(nreg)
    reg[c] = reg[a] + b
    return reg

def mulr(a,b,c,nreg):
    reg = copy(nreg)
    reg[c] = reg[a] * reg[b]
    return reg
    
def muli(a,b,c,nreg):
    reg = copy(nreg)
    reg[c] = reg[a] * b
    return reg

def banr(a,b,c,nreg):
    reg = copy(nreg)
    reg[c] = reg[a] & reg[b]
    return reg

def bani(a,b,c,nreg):
    reg = copy(nreg)
    reg[c] = reg[a] & b
    return reg
    
def borr(a,b,c,nreg):
    reg = copy(nreg)
    reg[c] = reg[a] | reg[b]
    return reg
    
def bori(a,b,c,nreg):
    reg = copy(nreg)
    reg[c] = reg[a] | b
    return reg
    
def setr(a,b,c,nreg):
    reg = copy(nreg)
    reg[c] = reg[a]
    return reg
    
def seti(a,b,c,nreg):
    reg = copy(nreg)
    reg[c] = a
    return reg

def gtir(a,b,c,nreg):
    reg = copy(nreg)
    reg[c] = 1 if a > reg[b] else 0
    return reg   
    
def gtri(a,b,c,nreg):
    reg = copy(nreg)
    reg[c] = 1 if reg[a] > b else 0
    return reg 
    
def gtrr(a,b,c,nreg):
    reg = copy(nreg)
    reg[c] = 1 if reg[a] > reg[b] else 0
    return reg 

def eqir(a,b,c,nreg):
    reg = copy(nreg)
    reg[c] = 1 if a == reg[b] else 0
    return reg   
    
def eqri(a,b,c,nreg):
    reg = copy(nreg)
    reg[c] = 1 if reg[a] == b else 0
    return reg 
    
def eqrr(a,b,c,nreg):
    reg = copy(nreg)
    reg[c] = 1 if reg[a] == reg[b] else 0
    return reg 

funcs = [
    (addr, 'addr'),
    (addi, 'addi'),
    (mulr, 'mulr'),
    (muli, 'muli'),
    (banr, 'banr'),
    (bani, 'bani'),
    (borr, 'borr'),
    (bori, 'bori'),
    (setr, 'setr'),
    (seti, 'seti'),
    (gtir, 'gtir'),
    (gtri, 'gtri'),
    (gtrr, 'gtrr'),
    (eqir, 'eqir'),
    (eqri, 'eqri'),
    (eqrr, 'eqrr')
]
    
run()
