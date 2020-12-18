
from copy import copy, deepcopy
from collections import defaultdict, deque, Counter
from blist import *
from parse import compile
import math
# from z3 import *

# units, hp, weak_to, immune_to, attack, type, initiative
imm = [
    (1466, 7549, ['fire', 'bludgeoning'], [], 49, 'fire', 1, 0),
    (8647, 6003, ['radiation', 'cold'], [], 6, 'cold', 3, 0),
    (2777, 7460, ['fire'], ['slashing'], 24, 'bludgeoning', 7, 0),
    (470, 1938, ['fire', 'cold'], [], 40, 'cold', 18, 0),
    (4203, 6288, [], ['fire'], 13, 'cold', 9, 0),
    (2975, 4211, [], ['slashing'], 14, 'slashing', 20, 0),
    (123, 10083, ['fire'], ['radiation'], 777, 'bludgeoning', 15, 0),
    (3455, 6391, ['radiation', 'slashing'], ['cold', 'bludgeoning'], 16, 'bludgeoning', 19, 0),
    (4323, 4880, ['cold'], ['radiation'], 10, 'slashing', 14, 0),
    (1586, 3567, ['bludgeoning', 'radiation'], ['slashing', 'cold'], 17, 'radiation', 4, 0)
]
inf = [
    (5380, 18316, [], [], 5, 'slashing', 17, 1),
    (6230, 12274, ['slashing'], [], 3, 'fire', 16, 1),
    (214, 27761, ['bludgeoning'], [], 233, 'fire', 11, 1),
    (1515, 47688, ['slashing'], ['radiation'], 49, 'cold', 8, 1),
    (268, 44231, [], [], 259,'fire', 6, 1),
    (2318, 22996, [], [], 18,'fire', 5, 1),
    (9492, 19449, ['bludgeoning', 'slashing'], ['cold'], 4, 'radiation', 13, 1),
    (1113, 39287, [], [], 69, 'fire', 12, 1),
    (1382, 15277, ['radiation', 'fire'], [], 19, 'cold', 2, 1),
    (2101, 25567, [], [], 17, 'slashing', 10, 1)
]
    
boost = 27# 500 #1250
# imm = [
#     (17, 5390, ['radiation', 'bludgeoning'], [], 4507, 'fire', '(init 2) immune 1', 0),
#     (989, 1274, ['bludgeoning', 'slashing'], ['fire'], 25, 'slashing', '(init 3) immune 2', 0)
# ]
# 
# inf = [
#     (801, 4706, ['radiation'], [], 116, 'bludgeoning', '(init 1) infect 1', 1),
#     (4485, 2961, ['fire', 'cold'], ['radiation'], 12, 'slashing', '(init 4) infect 2', 1)
# ]
    
def run(imm, inf):
    # 0     1   2           3           4       5   6
    # units, hp, weak_to, immune_to, attack, type, initiative
    
    unit_map = {}
    new_imm = []
    new_inf = []
    for g in imm:
        (a,b,c,d,e,f,ge,h) = g
        unit_map[g[6]] = (a,b,c,d,e + boost,f,ge,h)
        new_imm.append(g[6])
    for g in inf:
        unit_map[g[6]] = g
        new_inf.append(g[6])
    imm = new_imm
    inf = new_inf
    
    round = 0
    while True:
        print("######### Round", round)
        round += 1
        
        all = []
        ## Phase 1
        # 1) sort by effective power, desc (tie breaks by initiative)
        for i in imm:
            g = unit_map[i]
            ep = g[0] * g[4]
            print("{} has {} units with damage {}".format(g[6], g[0], g[4]))
            all.append((ep, i, 'imm'))
        for i in inf:
            g = unit_map[i]
            ep = g[0] * g[4]
            print("{} has {} units with damage {}".format(g[6], g[0], g[4]))
            all.append((ep, i, 'inf'))
        print(" ")
        # 2) The attacking group chooses to target the group 
        #    in the enemy army to which it would deal the most damage
        imm_chosen = set()
        inf_chosen = set()
        chosen = {}
        for (ep, i, type) in sorted(all, reverse=True):
            if type == 'imm':
                gp = most_damage(unit_map[i], inf, imm_chosen, unit_map)
                if gp is not None:
                    imm_chosen.add(gp[6])
                    # print("Immune Group {} with {} ep is picking {}".format(i, ep, gp[6]))
                    chosen[i] = gp[6]
                else:
                    # print("Immune Group {} with {} ep is picking None".format(i, ep))
                    chosen[i] = None
            else:
                gp = most_damage(unit_map[i], imm, inf_chosen, unit_map)
                if gp is not None:
                    inf_chosen.add(gp[6])
                    # print("Infect Group {} with {} ep is picking {}".format(i, ep, gp[6]))
                    chosen[i] = gp[6]
                else:
                    # print("Infect Group {} with {} ep is picking None".format(i, ep))
                    chosen[i] = None
        print("   ")
        
        print([b[1] for b in all])
        ## Phase 2 Attacking
        for (ep, i, type) in sorted(all, key=lambda b: b[1], reverse=True):
            g = unit_map[i]
            damage = g[0] * g[4]
            if damage == 0:
                continue
            if chosen[i] is None:
                continue
            gp = unit_map[chosen[g[6]]]
            (units, hp, ww,ii,c,d,e,tt) = gp
            if g[5] in ww:
                damage *= 2
            elif g[5] in ii:
                damage = 0
            if damage == 0:
                continue
            total = units * hp
            total -= damage
            total = int(math.ceil(total / hp))
            total = max(total, 0)
            print("Group {} is dealing {} damage to {}; killing {}".format(
                i, damage, chosen[g[6]], units - total
            ))
            unit_map[chosen[g[6]]] = (total, hp, ww, ii, c, d, e,tt)
            
        ## Check is all groups are dead in one army
        alive_imm = 0
        alive_inf = 0
        for i in imm:
            alive_imm += unit_map[i][0]
        for i in inf:
            alive_inf += unit_map[i][0]
        if alive_imm == 0:
            rest, win = alive_inf, 'Infection Wins'
            break
        elif alive_inf == 0:
            rest, win = alive_imm, 'Immune Wins'
            break
    
    print("Result is", rest, win)
    return 0
        
def most_damage(g, others, chosen, unit_map):
    # 0     1   2           3           4       5   6
    # units, hp, weak_to, immune_to, attack, type, initiative
    type = g[5]
    ep = g[0] * g[4]
    most = None
    mostd = 0
    mostep = 0
    mosti = 0
    for gp in others:
        if gp in chosen:
            continue
        x = unit_map[gp]
        damage = 0 
        (units, _, weak, immune, attack, _, init, t) = x
        if units == 0:
            continue
        if type in weak:
            damage = 2 * ep
        elif type in immune:
            damage = 0
        else:
            damage = ep
        eep = units * attack
        print("{} would deal {} to {}".format(g[6], damage, init))
        if damage == 0:
            continue
        if damage > mostd:
            mostd, most, mostep, mosti = damage, x, eep, init
        elif damage == mostd:
            if eep > mostep:
                mostd, most, mostep, mosti = damage, x, eep, init
            elif eep == mostep:
                if init > mosti:
                    mostd, most, mostep, mosti = damage, x, eep, init

    return most
    
        
run(imm, inf)




















