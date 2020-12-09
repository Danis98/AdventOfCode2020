def lmap(func, x):
    return list(map(func, x))

input = lmap(int, open("day09.input", "r").read().strip().split("\n"))

for i in range(25, len(input)):
    prev = input[i-25:i]
    pres = False
    for p in prev:
        if input[i]-p in prev:
            pres = True
            break
    if not pres:
        print(input[i])
        break