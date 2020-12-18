
lines = []
n = input()
while n != 'done':
    lines.append(n)
    n = input()
    
# muted coral bags contain 1 bright magenta bag, 1 dim aqua bag.
rules = {}
for l in lines:
    ls = l.split(' bags contain ')
    k = ls[0]
    rest = ls[1].split(', ')
    rrs = []
    for r in rest:
        tts = r.split(' ')
        if tts[0] == 'no':
            num = 0
        else:
            num = int(tts[0])
        bag = tts[1:-1]
        rrs.append((num, ' '.join(bag)))
    rules[k] = rrs
    
can_hold = {}
for bag in rules:
    ch = rules[bag]
    for (num, bagt) in ch:
        if bagt in can_hold:
            can_hold[bagt].append(bag)
        else:
            can_hold[bagt] = [bag]

mine = 'shiny gold'
def in_bag(bag):
    if bag == 'other':
        return 1
    can_hold = rules[bag]
    print(bag, 'can hold', can_hold)
    tot = 0
    for (ct, newbag) in can_hold:
        if ct == 0 and newbag == 'other':
            return 1
        else:
            ctt = in_bag(newbag)
            tot += ct * ctt
            if ctt > 1:
                tot += ct
            
    print(bag, 'can hold', tot, 'bags')
    return tot 
    
print(in_bag(mine) )
    
        
    
        