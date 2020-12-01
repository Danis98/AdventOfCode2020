input = list(map(int, open("day01.input", "r").read().strip().split("\n")))

for num in input:
    if 2020-num in input:
        print(num * (2020-num))
        break