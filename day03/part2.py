from functools import reduce
import operator

def lmap(func, x):
    return list(map(func, x))

input = open("day03.input", "r").read().strip().split("\n")

def calc_trees(slope):
    trees = 0
    for idx, line in enumerate(input):
        if idx % slope[0] != 0:
            continue
        trees += line[int((slope[1]*idx/slope[0])%len(line))] == '#'
    return trees

slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
tot_trees = reduce(operator.mul, lmap(calc_trees, slopes), 1)
print(tot_trees)