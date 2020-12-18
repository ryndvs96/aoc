
import sys
sys.setrecursionlimit(10000)

r0,r1,r2,ip,r4,r5 = 0,0,0,0,0,0
def main():
    global r0,r1,r2,ip,r4,r5
    r0 = 1
    f0()

def f0():
    global r0,r1,r2,ip,r4,r5
    r1 = 123
    f1()
    
def f1():
    global r0,r1,r2,ip,r4,r5
    r1 = (r1 & 456)
    r1 = (r1 == 72)
    if r1:
        r1 = 0
        f6()
    else:
        f1()

def f6():
    global r0,r1,r2,ip,r4,r5
    r2 = (r1 | 65536)
    r1 = 10605201
    f8()
    
def f8():
    global r0,r1,r2,ip,r4,r5
    r5 = (r2 & 255)
    r1 = r1 + r5
    r1 = (r1 & 16777215)
    r1 = r1 * 65899
    r1 = (r1 & 16777215)
    r5 = (256 > r2)
    if r5:
        f28()
    else:
        r5 = 0
        f18()

def f18():
    global r0,r1,r2,ip,r4,r5
    r4 = r5 + 1
    r4 = r4 * 256
    r4 = (256 > r2)
    if r4:
        r2 = r5
        f8()
    else:
        r5 = r5 + 1
        f18()

def f28():
    global r0,r1,r2,ip,r4,r5
    r5 = (r0 == r1)
    if r5:
        print("All Done")
        exit()
    else:
        f6()

main()
    
    
    
    
    
    
    
    
