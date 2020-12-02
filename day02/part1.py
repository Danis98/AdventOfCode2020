def lmap(func, x):
    return list(map(func, x))

input = open("day02.input", "r").read().strip().split("\n")

res = 0
for psw in input:
    parts = psw.split(" ")
    m, M = lmap(int, parts[0].split("-"))
    lett = parts[1][:-1]
    cnt = parts[2].count(lett)
    if m <= cnt and cnt <= M:
        res += 1
print(res)