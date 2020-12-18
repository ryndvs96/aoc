from copy import copy, deepcopy
from collections import defaultdict, deque, Counter
from blist import *
from parse import compile
import sys

# Input example
# 5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))

s = input()
lines = []
while s != 'done':
    lines.append(s.replace(' ', ''))
    s = input()
    
# Lower number is higher precedence.
ORDER_OPS = [
    (0, '+', lambda x,y: x + y), 
    (1, '*', lambda x,y: x * y)
]
OPS = [op[1] for op in ORDER_OPS]
NUM_CHARS = [str(n) for n in range(0,10)]
    
def eval(expr):
    """Takes in a tokenized expression as a list and evaluates it.
    
    Parentheses are not allowed, those should have already been evaluated.
    
    Given a line like [2, '+', 3, '*' 4] would resolve to 20 or 14 depending on
    operator precedence. Order of operations is determined by ORDER_OPS."""
    
    # Base case, we're left with one value to return.
    if len(expr) == 1:
        return expr[0]
    
    # Operation at the highest level of recursion will be done last, so we need
    # to reverse the order of ops for recursion.
    for (_, op, func) in sorted(ORDER_OPS, reverse=True):
        for i, token in enumerate(expr):
            if token == op:
                tot = func(eval(expr[0:i]), eval(expr[i+1:]))
                # print('{} = {}'.format(expr, tot))
                return tot


def resolve(line):
    """Takes in a str expression and evaluates it.
    
    Given a line like '2*(3+4)' would resolve to 14.
    Order of operations is determined by ORDER_OPS, parens always have highest
    precedence over any others."""
    
    # Keep track of overall expression, tokenized and numbers as ints.
    expr = []
    
    # Keep track of how deep we are in parens. When we get back to 0 we need to
    # recurse on what we have so far as nested expression string.
    in_paren = 0
    nested = ''
    num = ''
    
    # Parse line char by char.
    for i, c in enumerate(line, 1):
        # If we're already in a nested paren section, keep adding to it until we
        # pop back out of it.
        if in_paren > 0:
            if c == '(':
                nested += c
                in_paren += 1
            elif c == ')':
                in_paren -= 1
                # If we've reached top level, send nested expr for evaluation
                # and add result as part of expression.
                if in_paren == 0:
                    expr.append(resolve(nested))
                    nested = ''
                else:
                    nested += c
            else:
                nested += c
        else:
            if c in NUM_CHARS:
                num += c
            else:
                if len(num) > 0:
                    expr.append(int(num))
                    num = ''
                    
                if c == '(':
                    in_paren += 1
                elif c == ')':
                    print('Paren mismatch at char {} for \'{}\'.'.format(i, line))
                    exit()
                elif c in OPS:
                    expr.append(c)
                else:
                    print('Unknown char \'{}\' at {} in \'{}\'.'.format(c, i, line))
    if len(num) > 0:
        expr.append(int(num))
    
    # After expression is tokenized we can evaluate it.
    return eval(expr)

tot = sum([resolve(l) for l in lines])
print(tot)