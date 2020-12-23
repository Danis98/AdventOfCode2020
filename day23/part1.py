def lmap(func, x):
    return list(map(func, x))

input = open("day23.input", "r").read().strip().split("\n")

cups = lmap(int, list(input[0]))

cur_idx = 0
for i in range(100):
    cur = cups[cur_idx]
    tak = cups[cur_idx+1:cur_idx+4]
    if len(tak) < 3:
        rem = 3 - len(tak)
        tak += cups[:rem]
        cups = cups[rem:cur_idx+1]
    else:
        cups = cups[:cur_idx+1] + cups[cur_idx+4:]
    f = False
    idx = None
    for v in range(cur-1, -1, -1):
        if v in cups:
            idx = cups.index(v)
            break
    if idx == None:
        idx = cups.index(max(cups))
    cups = cups[:idx+1]+tak+cups[idx+1:]
    if cups[cur_idx] != cur:
        d = cups.index(cur) - cur_idx
        cups = cups[d:] + cups[:d]
    cur_idx = (cur_idx+1)%len(cups)
    
start = cups.index(1)
cups = cups[start+1:]+cups[:start]
print(''.join(lmap(str, cups)))
