
import sys
sys.setrecursionlimit(10000)

r0,r1,r2,ip,r4,r5 = 0,0,0,0,0,0
m = 100000000000
uniqs = set()
def main():
    global r0,r1,r2,ip,r4,r5
    r0 = 0
    f0()

def f0():
    global r0,r1,r2,ip,r4,r5
    r1 = 123
    f1()
    
def f1():
    global uniqs,m,r0,r1,r2,ip,r4,r5
    r1 = (r1 & 456)
    r1 = (r1 == 72)
    if not r1:
        f1()
    else:
        r1 = 0
        # f6()
        f6 = True
        while f6:
            r2 = (r1 | 65536)
            r1 = 10605201
            # f8()
            f8 = True
            while f8:
                r1 = r1 + (r2 & 255)
                r1 = (r1 & 16777215)
                r1 = r1 * 65899
                r1 = (r1 & 16777215)
                if (256 > r2):
                    # f28()
                    nm = min(r1,m)
                    if r1 not in uniqs:
                        print("Adding new r1", r1)
                        uniqs.add(r1)
                    if nm != m:
                        print("New min is", nm)
                    m = nm
                    if (r0 == r1):
                        print("All Done")
                        exit()
                    else:
                        f8 = False
                else:
                    r5 = 0
                    while ((r5 * 256) + 1) > r2:
                        r5 = r5 + 1
                    r2 = r5
                    
                    # r2 = r2 - 256
                    # r2 = r2 / 256
                    # r2 = r2 + 1
                    # r5 = 0
                    # f18():
                    # r5 > (r2 - 256) / 256:
                    r2 = 1 + int((r2 - 256) / 256)

main()
    
    
    
    
    
    
    
    
