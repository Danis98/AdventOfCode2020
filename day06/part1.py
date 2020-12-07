import itertools
from functools import reduce
import operator

def lmap(func, x):
    return list(map(func, x))

def pairs(x):
    return itertools.combinations(x, 2)

def pairs(x, y):
    return itertools.product(x, y)

def mult(a):
    return reduce(operator.mul, a, 1)

# --------- END OF HELPER FUNCS ---------

input = open("day06.input", "r").read().strip().split("\n")

res = 0
str = ""
for line in input:
    if len(line) == 0:
        res += len(set(str))
        str = ""
    else:
        str += line
res += len(set(str))
print(res)