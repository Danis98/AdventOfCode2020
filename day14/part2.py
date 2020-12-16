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

addrs = set()
def gen_addr(addr, mask, i, cur):
    if i >= len(mask):
        return [cur]
    cur *= 2
    if mask[i] == '0':
        # print(i, addr, len(mask)-i-1, (addr >> (len(mask)-i-1)))
        cur += (addr >> (len(mask)-i-1)) & 1
        return gen_addr(addr, mask, i+1, cur)
    elif mask[i] == '1':
        cur += 1
        return gen_addr(addr, mask, i+1, cur)
    elif mask[i] == 'X':
        return gen_addr(addr, mask, i+1, cur) + gen_addr(addr, mask, i+1, cur+1)


mem = {}
addr_mask = 0

for line in input:
    l, r = line.split(" = ")
    if l == 'mask':
        addr_mask = r
    else:
        addr = int(l[4:-1])
        addrs.clear()
        addrs.add(0)
        for mod_addr in gen_addr(addr, addr_mask, 0, 0):
            print("mem[%s]=%s" % (bin(mod_addr), r))
            mem[mod_addr] = int(r)
print(mem)
print(sum(map(lambda x: mem[x], mem)))
