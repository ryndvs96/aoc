
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

#  IP = 3

IP_LOC = 3
ins = []
s = input()
while s != 'done':
    (i,a,b,c) = s.split(" ")
    a,b,c = int(a), int(b), int(c)
    ins.append((i,a,b,c))
    s = input()
    
def runp():
    i = 0
    end = False
    while not end:
        print("running", i)
        end = run(i)
        i += 1
    print("ended with ", i - 1)
    
    
def run(x):
    tot = 0
    ip = 0
    regs = [0,0,0,0,0,0]
    tick = 0
    l = len(ins)
    u = set()
    while 0 <= ip and ip < l:
        tick += 1
        (i,a,b,c) = ins[ip]
        if ip == 28:
            r = regs[1]
            if r not in u:
                print("New R", r)
                u.add(r)
        regs = funcs[i](a,b,c,regs)
        ip = regs[IP_LOC] + 1
        regs[IP_LOC] = ip
        tick += 1
        # else:
    print(regs[0])
    if tick ==10000000:
        return False
    else:
        return True
# FUNCTIONS

def noop(a,b,c,nreg):
    return nreg

def divi(a,b,c,nreg):
    reg = nreg
    reg[c] = int(reg[a] / b)
    return reg
    
def addr(a,b,c,nreg):
    reg = nreg
    reg[c] = reg[a] + reg[b]
    return reg
    
def addi(a,b,c,nreg):
    reg = nreg
    reg[c] = reg[a] + b
    return reg

def mulr(a,b,c,nreg):
    reg = nreg
    reg[c] = reg[a] * reg[b]
    return reg
    
def muli(a,b,c,nreg):
    reg = nreg
    reg[c] = reg[a] * b
    return reg

def banr(a,b,c,nreg):
    reg = nreg
    reg[c] = reg[a] & reg[b]
    return reg

def bani(a,b,c,nreg):
    reg = nreg
    reg[c] = reg[a] & b
    return reg
    
def borr(a,b,c,nreg):
    reg = nreg
    reg[c] = reg[a] | reg[b]
    return reg
    
def bori(a,b,c,nreg):
    reg = nreg
    reg[c] = reg[a] | b
    return reg
    
def setr(a,b,c,nreg):
    reg = nreg
    reg[c] = reg[a]
    return reg
    
def seti(a,b,c,nreg):
    reg = nreg
    reg[c] = a
    return reg

def gtir(a,b,c,nreg):
    reg = nreg
    reg[c] = 1 if a > reg[b] else 0
    return reg   
    
def gtri(a,b,c,nreg):
    reg = nreg
    reg[c] = 1 if reg[a] > b else 0
    return reg 
    
def gtrr(a,b,c,nreg):
    reg = nreg
    reg[c] = 1 if reg[a] > reg[b] else 0
    return reg 

def eqir(a,b,c,nreg):
    reg = nreg
    reg[c] = 1 if a == reg[b] else 0
    return reg   
    
def eqri(a,b,c,nreg):
    reg = nreg
    reg[c] = 1 if reg[a] == b else 0
    return reg 
    
def eqrr(a,b,c,nreg):
    reg = nreg
    reg[c] = 1 if reg[a] == reg[b] else 0
    return reg 

func_list = [
    (noop, 'noop'),
    (divi, 'divi'),
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

funcs = {}
for (f,n) in func_list:
    funcs[n] = f
    
runp()
