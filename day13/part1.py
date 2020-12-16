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

input = open("day13.input", "r").read().strip().split("\n")

t0 = int(input[0])
buses = input[1].split(",")

best = -1
bestv = -1
for bus in buses:
    if bus == 'x':
        continue
    per = int(bus)
    mod = t0 % per
    if mod == 0:
        best = per
        bestv = t0
        break
    nxt = t0 - mod + per
    if best == -1 or bestv > nxt:
        best = per
        bestv = nxt
print(best * (bestv - t0))