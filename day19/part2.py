def lmap(func, x):
    return list(map(func, x))

input = open("day19.input", "r").read().strip().split("\n")

matches = {}
def explore(rules, idx):
    if idx in matches:
        return matches[idx]
    matches[idx] = set()
    for opt in rules[idx]:
        p = []
        for comp in opt:
            if isinstance(comp, str):
                p.append([comp])
            else:
                p.append(explore(rules, comp))
        if len(p) == 1:
            for p1 in p[0]:
                matches[idx].add(p1)
        else:
            for p1 in p[0]:
                for p2 in p[1]:
                    matches[idx].add(p1+p2)
    return matches[idx]

def check_matches(matches, line, n42=0, n31=0):
    if len(line) == 0:
        return n42 >= 2 and n31 >= 1 and n31 < n42
    if n31 == 0:
        for s in matches[42]:
            if not line.startswith(s):
                continue
            if check_matches(matches, line[len(s):], n42+1, n31):
                return True
    if n42 < 2:
        return False
    for s in matches[31]:
        if not line.startswith(s):
            continue
        if check_matches(matches, line[len(s):], n42, n31+1):
            return True
    return False


rules = {}
for line in input:
    if len(line) == 0:
        break
    idx, body = line.split(": ")
    idx = int(idx)
    rules[idx] = []
    opts = body.split(" | ")
    for opt in opts:
        if opt[0] == "\"":
            rules[idx].append(opt[1])
        else:
            r = lmap(int, opt.split(" "))
            rules[idx].append(r)

explore(rules, 8)
explore(rules, 11)

s = 0
for line in input[len(rules)+1:]:
    res = check_matches(matches, line)
    s += res
print(s)