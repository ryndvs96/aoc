lines = []
n = input()
while n != 'done':
    lines.append(n)
    n = input()
    
ops = []
for l in lines:
    ls = l.split(' ')
    op = ls[0]
    arg = int(ls[1])
    ops.append((op, arg))
    
acc = 0    
opi = 0
ran = []
last = len(ops)
loop = []
while True:
    if opi in ran:
        if opi in loop:
            break
        loop.append(opi)
    else: 
        ran.append(opi)
    (op, arg) = ops[opi]
    nextijmp = opi + arg
    nextinop = opi + 1
    if op == 'acc':
        acc += arg
        opi += 1
    elif op == 'jmp':
        if nextinop == last:
            break
        opi += arg
    elif op == 'nop':
        if nextijmp == last:
            break
        opi += 1
    # print(acc)
    
    
print('loop is', loop)
for opc in loop:
    if ops[opc][0] == 'jmp':
        print('switching', opc, ops[opc])
        newops = list(ops)
        newops[opc] = ('nop', ops[opc][1])
        
        acc = 0    
        opi = 0
        ran = []
        last = len(ops)
        loop = []
        while True:
            if opi in ran:
                if opi in loop:
                    break
                loop.append(opi)
            else: 
                ran.append(opi)
            (op, arg) = newops[opi]
            nextijmp = opi + arg
            nextinop = opi + 1
            if op == 'acc':
                acc += arg
                opi += 1
            elif op == 'jmp':
                if nextinop == last:
                    break
                opi += arg
            elif op == 'nop':
                if nextijmp == last:
                    break
                opi += 1
        if not loop:
            print(acc)    
        
    elif ops[opc] == 'nop':
        print('switching', opc, ops[opc])
        newops = list(ops)
        newops[opc] = ('jmp', ops[opc][1])
        
        acc = 0    
        opi = 0
        ran = []
        last = len(ops)
        loop = []
        while True:
            if opi in ran:
                if opi in loop:
                    break
                loop.append(opi)
            else: 
                ran.append(opi)
            (op, arg) = newops[opi]
            nextijmp = opi + arg
            nextinop = opi + 1
            if op == 'acc':
                acc += arg
                opi += 1
            elif op == 'jmp':
                if nextinop == last:
                    break
                opi += arg
            elif op == 'nop':
                if nextijmp == last:
                    break
                opi += 1
        if not loop:
            print(acc)    