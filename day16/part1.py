def lmap(func, x):
    return list(map(func, x))

input = open("day16.input", "r").read().strip().split("\n")

rules = {}
idx = 0
for i in range(len(input)):
    if len(input[i]) == 0:
        idx = i+1
        break
    rule, ranges = input[i].split(": ")
    ranges = ranges.split(" or ")
    ranges = lmap(lambda x: x.split("-"), ranges)
    rules[rule] = []
    for rng in ranges:
        rules[rule].append((int(rng[0]), int(rng[1])))
your = lmap(int, input[idx+1].split(","))
nearby = []
for i in range(idx+4, len(input)):
    nearby.append(lmap(int, input[i].split(",")))

err_sum = 0
for ticket in nearby:
    for field in ticket:
        err = True
        for rule in rules:
            for rng in rules[rule]:
                if field >= rng[0] and field <= rng[1]:
                    err = False
                    break
            if not err:
                break
        if err:
            err_sum += field
print(err_sum)