def lmap(func, x):
    return list(map(func, x))

input = lmap(int, open("day10.input", "r").read().strip().split("\n"))

input += [0, max(input)+3]
input = sorted(input)
res = [0 for i in range(len(input))]
res[0] = 1

start = 0
running = 0
for i in range(1, len(input)):
    running += res[i-1]
    while input[i] - input[start] > 3:
        running -= res[start]
        start += 1
    res[i] = running
    
print(res[-1])