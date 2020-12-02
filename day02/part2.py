def lmap(func, x):
    return list(map(func, x))

input = open("day02.input", "r").read().strip().split("\n")

res = 0
for psw in input:
    parts = psw.split(" ")
    m, M = lmap(int, parts[0].split("-"))
    lett = parts[1][:-1]
    if (parts[2][m-1] == lett) ^ (parts[2][M-1] == lett):
        res += 1
print(res)