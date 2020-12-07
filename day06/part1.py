input = open("day06.input", "r").read().strip().split("\n")

res = 0
str = ""
for line in input:
    if len(line) == 0:
        res += len(set(str))
        str = ""
    else:
        str += line
res += len(set(str))
print(res)