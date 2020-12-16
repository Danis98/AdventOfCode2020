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

input = open("day15.input", "r").read().strip().split(",")
input = lmap(int, input)

last = {}
lastn = -1
for i in range(30000000):
    if i < len(input):
        last[lastn] = i-1
        lastn = input[i]
    else:
        temp = 0
        if lastn in last:
            temp = i-1 - last[lastn]
        last[lastn] = i-1
        lastn = temp
print(lastn)

