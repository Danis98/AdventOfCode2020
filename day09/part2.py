def lmap(func, x):
    return list(map(func, x))

input = lmap(int, open("day09.input", "r").read().strip().split("\n"))

inv = 0
for i in range(25, len(input)):
    prev = input[i-25:i]
    pres = False
    for p in prev:
        if input[i]-p in prev:
            pres = True
            break
    if not pres:
        inv = input[i]
        break
a = 0
s = 0
for b in range(len(input)):
    s += input[b]
    while s > inv and a < len(input)-1:
        s -= input[a]
        a += 1
    if s == inv:
        print(min(input[a:b+1])+max(input[a:b+1]))
        break