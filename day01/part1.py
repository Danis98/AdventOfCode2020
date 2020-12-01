def lmap(func, x):
    return list(map(func, x))

# --------- END OF HELPER FUNCS ---------

input = lmap(int, open("day01.input", "r").read().strip().split("\n"))

for num in input:
    if 2020-num in input:
        print(num * (2020-num))
        break