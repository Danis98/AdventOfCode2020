def lmap(func, x):
    return list(map(func, x))

input = open("day19.input", "r").read().strip().split("\n")

def check_rule(rules, line, rule_id, pos):
    for opt in rules[rule_id]:
        if not isinstance(opt, list):
            return (line[pos] == opt), pos+1
        newpos = pos
        good = True
        for comp in opt:
            match, newpos = check_rule(rules, line, comp, newpos)
            if not match:
                good = False
                break
        if good:
            return True, newpos
    return False, pos+1

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
s = 0
for line in input[len(rules)+1:]:
    ch = check_rule(rules, line, 0, 0)
    res = ch[0] and ch[1] == len(line)
    s += res
print(s)