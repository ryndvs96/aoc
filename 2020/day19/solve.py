from parse import compile
from copy import copy, deepcopy
from collections import defaultdict, Counter, deque
from blist import *
import itertools
import math
import sys
# sys.setrecursionlimit(10000)

reg = compile("{}: {}")

# simple class
class Rule(object):
    def __init__(self, k):
        self.subrules = []
        self.matches = []
        self.char = None
        self.key = k
    
    def __str__(self):
        if self.subrules:
            return 'subrules: ({})'.format(len(self.subrules))
        if self.matches:
            return 'matches: {}'.format(self.matches)
        if self.char:
            return 'char: \'{}\''.format(self.char)
        return 'Not a rule??'

def resolve(rulestr, k):
    rs = rulestr.split(' | ')
    rule = Rule(k)
    if len(rs) > 1:
        for i, r in enumerate(rs):
            rule.subrules.append(resolve(r, '{}_{}'.format(k,i)))
    else:
        rs = rulestr.split(' ')
        if len(rs) == 1:
            r = rs[0]
            if r == '\"a\"':
                rule.char = 'a'
            elif r == '\"b\"':
                rule.char = 'b'
            elif r == '\"c\"':
                rule.char = 'c'
            else:
                rule.matches.append(int(r))
        else:
            for r in rs:
                rule.matches.append(int(r))
    return rule
    
    
def solve(line, rules):
    (valid, rets) = solverec(line, 0, rules[0], rules)
    if valid:
        for (r,v) in rets:
            if r == len(line) - 1:
                print('{} is valid with steps {}'.format(line, v))
                return True
    print('{} is NOT valid'.format(line))
    return False
    
def solverec(line, i, rule, rules):
    if i > len(line) - 1:
        return (False, None)
    c = line[i]
    if rule.subrules:
        rets = []
        for r in rule.subrules:
            (valid, reti) = solverec(line, i, r, rules)
            if valid:
                rr = []
                for (r,s) in reti:
                    rr.append((r, '{}({})'.format(rule.key, s)))
                rets.extend(rr)
                # stepsi = '{}({})'.format(rule.key, steps)
                # print(i, c, steps, rule.key)
        if rets:
            return (True, rets)
        return (False, None)
    elif rule.matches:
        reti = []
        steps = rule.key
        for m in rule.matches:
            if not reti:
                (valid, reti) = solverec(line, i, rules[m], rules)
            else:
                rr = []
                for (ri, stepsi) in reti:
                    (valid, rets) = solverec(line, ri + 1, rules[m], rules)
                    if valid:
                        rr.extend(rets)
                reti = rr
            # print(i, c, steps, rule.key)
            if not reti:
                return (False, None)
            rr = []
            for (r,s) in reti:
                rr.append((r, steps + '({})'.format(s)))
            reti = rr
        # print(i, c, steps, rule.key)
        return (True, reti)
            
    elif rule.char:
        if c == rule.char:
            steps = rule.char
            # print(i, c, steps, rule.key)
            return (True, [(i, steps)])
        else:
            return (False, None)
    

s = input()
rules = {}
while s != '':
    k, r = reg.parse(s)
    rules[int(k)] = resolve(r.strip(), k)
    s = input()

s = input()    
tot = 0
while s != 'done':
    valid = solve(s, rules)
    if valid:
        tot += 1
    s = input()
print(tot)
    

"""
valid 11_0
(11_0 
 (42_0
  (9_1
   (a)
   (26_1
    (a)
    (20_0
     (b)
     (b)
    )
   )
  )
  (b)
 )
 (31_1
  (a)
  (13_0
   (b)
   (3_1
    (16_1
     (b)
     (b)
    )
    (a)
   )
  )
 )
)(31_1(a)(13_1(a)(12_1(19_1(b)(b))(a)))))(31_1(a)(13_0(b)(3_1(16_0(15_0(a))(a))(a)))))

"""
    
"""
8:
    42:
        9 14:
            14 27:
                "b"
                ---
                1 6:
                    "a"
                    ---
                    14 14: "bb"
                    1 14:  "ab"
            1 26:
                "a"
                ---
                14 22:
                    "b"
                    ---
                    14 14: "bb"
                1 20:
                    "a"
                    ---
                    14 14: "bb"
                    1 15:
                        "a"
                        ---
                        1:  "a"
                        14: "b"
            ---
            "b"
        10 1:
            23 14:
                25 1:
                    1 1: "aa"
                    1 14: "ab"
                    ---
                    "a"
                22 14:
                    14 14: "bb"
                    ---
                    "b"
            28 1:
                16 1:
                    15 1:
                        1:  "a"
                        14: "b"
                        ---
                        1:  "a"
                    14 14: "bb"
                    ---
                    "a"
            ---
            "a"
    42 8:
"""
    
    
    
    
    
    
    
    
    
    # hello