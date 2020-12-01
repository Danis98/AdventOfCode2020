input = list(map(int, open("day01.input", "r").read().strip().split("\n")))

f=False
for a in input:
    for b in input:
        if 2020-a-b in input:
            print(a * b * (2020-a-b))
            f=True
            break
    if f:
        break