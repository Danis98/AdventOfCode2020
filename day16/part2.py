def lmap(func, x):
    return list(map(func, x))

input = open("day16.input", "r").read().strip().split("\n")

def check_rule(val, rule):
    for rng in rule:
        if val >= rng[0] and val <= rng[1]:
            return True
    return False

def check_val(val, rules):
    for rule in rules:
        if check_rule(val, rules[rule]):
            return True
    return False

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

valid = [your]
for ticket in nearby:
    err = False
    for field in ticket:
        if not check_val(field, rules):
            err = True
    if not err:
        valid.append(ticket)

field_poss = []
for field in range(len(your)):
    poss = set()
    for rule in rules:
        err = False
        for ticket in valid:
            if not check_rule(ticket[field], rules[rule]):
                err = True
        if not err:
            poss.add(rule)
    field_poss.append(poss)

found = {}
while len(found) != len(your):
    for i in range(len(field_poss)):
        if len(field_poss[i]) == 1 and list(field_poss[i])[0] not in found:
            field = list(field_poss[i])[0]
            found[field] = i
            for j in range(len(field_poss)):
                if field in field_poss[j] and i != j:
                    field_poss[j].remove(field)

res = 1
for f in found:
    print(f, your[found[f]])
    if 'departure' in f:
        res *= your[found[f]]
print(res)