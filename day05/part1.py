input = open("day05.input", "r").read().strip().split("\n")

res = 0
for line in input:
    acc = 0
    for c in line:
        acc *= 2
        if c in "BR":
            acc += 1
    res = max(res, acc)
print(res)