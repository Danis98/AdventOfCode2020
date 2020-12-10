def lmap(func, x):
    return list(map(func, x))

input = lmap(int, open("day10.input", "r").read().strip().split("\n"))

jmp = {}
input.append(0)
input = sorted(input)

for i in range(len(input)):
    j = input[i] - input[i-1]
    if j not in jmp:
        jmp[j] = 0
    jmp[j] += 1
jmp[3] += 1

print(jmp[1] * jmp[3])