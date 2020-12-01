import itertools

def lmap(func, x):
    return list(map(func, x))

def pairs(x):
    return itertools.combinations(x, 2)

def pairs(x, y):
    return itertools.product(x, y)

# --------- END OF HELPER FUNCS ---------

input = lmap(int, open("day01.input", "r").read().strip().split("\n"))

for a, b in pairs(input):
    if 2020-a-b in input:
        print(a * b * (2020-a-b))
        break