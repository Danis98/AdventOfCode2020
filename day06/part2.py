input = open("day06.input", "r").read().strip().split("\n")

res = 0
lett = set("abcdefghijklmnopqrstuvxywz")
for line in input:
    if len(line) == 0:
        res += len(lett)
        lett = set("abcdefghijklmnopqrstuvxywz")
    else:
        lett = lett.intersection(line)
res += len(lett)
print(res)