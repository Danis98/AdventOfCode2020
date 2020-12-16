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

def modpow(a, b, MOD):
    res = 1;
    while b:
        if b & 1:
            res = (res * a) % MOD;
        b //= 2
        a = (a * a) % MOD
    return res

def modinv(a, MOD):
	return modpow(a, MOD-2, MOD)

# def egcd(a, b):
#     if a == 0:
#         return (b, 0, 1)
#     else:
#         g, y, x = egcd(b % a, a)
#         return (g, x - (b // a) * y, y)
#
# def modinv(a, m):
#     g, x, y = egcd(a, m)
#     if g != 1:
#         raise Exception('modular inverse does not exist')
#     else:
#         return x % m

# --------- END OF HELPER FUNCS ---------

input = open("day13.input", "r").read().strip().split("\n")

t0 = int(input[0])
buses = input[1].split(",")

n1 = int(buses[0])
a1 = 0
for i in range(1, len(buses)):
    if buses[i] == 'x':
        continue
    n2 = int(buses[i])
    a2 = n2 - i%n2
    print(a2, n2)
    n = n1*n2
    i1 = modinv(n1%n2, n2)
    i2 = modinv(n2%n1, n1)
    print(n2, i2, n1, (i2*n2)%n1, "inv")
    a = (a1*n2*modinv(n2, n1)+a2*n1*modinv(n1, n2)) % n
    a1, n1 = a, n
    print("->",a1,n1)
print(a1, n1)

# p0 = int(buses[0])
# mult = 0
# while True:
#     found = True
#     t0 = 1802
#     for i in range(len(buses)):
#         if buses[i] == 'x':
#             continue
#         p = int(buses[i])
#         print(i, p, t0%p)
#         if (t0+i)%p != 0:
#             found = False
#             break
#     if found:
#         print(t0, "GOOD")
#         break
#     mult += 1