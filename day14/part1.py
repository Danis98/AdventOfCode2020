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

def count_neigh(grid, r, c):
    ctr = 0
    for i in range(max(0, r-1), min(len(grid), r+2)):
        for j in range(max(0, c-1), min(len(grid[0]), c+2)):
            if i == r and j == c:
                continue
            if grid[i][j] == '#':
                ctr += 1
    return ctr

# --------- END OF HELPER FUNCS ---------

input = open("day14.input", "r").read().strip().split("\n")

def gen_masks(mask):
    or_mask, and_mask = (0, 0)
    for ch in mask:
        or_mask *= 2
        and_mask *= 2
        if ch == 'X':
            or_mask += 0
            and_mask += 1
        else:
            or_mask += int(ch)
            and_mask += int(ch)
    return or_mask, and_mask

mem = {}
or_mask, and_mask = (0, 0)

for line in input:
    l, r = line.split(" = ")
    if l == 'mask':
        or_mask, and_mask = gen_masks(r)
    else:
        addr = int(l[4:-1])
        mem[addr] = (int(r) | or_mask) & and_mask
print(mem)
print(sum(map(lambda x: mem[x], mem)))
