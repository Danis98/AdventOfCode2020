import itertools

def lmap(func, x):
    return list(map(func, x))

def pairs(x):
    return itertools.combinations(x, 2)

def pairs(x, y):
    return itertools.product(x, y)

# --------- END OF HELPER FUNCS ---------

input = open("dayXX.input", "r").read().strip()