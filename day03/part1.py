input = open("day03.input", "r").read().strip().split("\n")

trees = 0
for idx, line in enumerate(input):
    trees += line[(3*idx)%len(line)] == '#'
print(trees)