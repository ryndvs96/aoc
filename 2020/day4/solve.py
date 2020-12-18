
lines = []
n = input()
while n != 'done':
    lines.append(n)
    n = input()

passports = []
curr = {}
for l in lines:
    if l == '':
        passports.append(curr)
        curr = {}
    else:
        ls = l.split(' ')
        for lss in ls:
            kvs = lss.split(':')
            k = kvs[0]
            v = kvs[1]
            curr[k] = v

ct = 0
for passport in passports:
    needed = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
    if 'byr' not in passport:
        continue
    else:
        v = int(passport['byr'])
        if v < 1920 or v > 2002:
            continue
    
    if 'iyr' not in passport:
        continue
    else:
        v = int(passport['iyr'])
        if v < 2010 or v > 2020:
            continue
            
    if 'eyr' not in passport:
        continue
    else:
        v = int(passport['eyr'])
        if v < 2020 or v > 2030:
            continue
            
    if 'hgt' not in passport:
        continue
    else:
        v = passport['hgt']
        units = v[-2:]
        v = int(v[:-2])
        if units == 'cm':
            if v < 150 or v > 193:
                continue
        elif units == 'in':
            if v < 59 or v > 76:
                continue
        else:
            continue
    
    if 'hcl' not in passport:
        continue
    else:
        v = passport['hcl']
        hash = v[0]
        hex = v[1:]
        if hash != '#':
            continue
        if len(hex) != 6:
            continue
        allhex = True
        for h in hex:
            if h not in 'abcdef0123456789':
                allhex = False
        if not allhex:
            continue
        
    if 'ecl' not in passport:
        continue
    else:
        v = passport['ecl']
        if v not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            continue
            
    if 'pid' not in passport:
        continue
    else:
        v = passport['pid']
        alldig = True
        for h in v:
            if h not in '0123456789':
                alldig = False
        if not alldig:
            continue
        if len(v) != 9:
            continue
    
    ct += 1
print(ct)

# 78*247*68*69*33

    


