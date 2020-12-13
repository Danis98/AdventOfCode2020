input = open("day12.input", "r").read().strip().split("\n")

dir = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]

x, y = (0, 0)
d = 0
for instr in input:
    lett, arg = instr[:1], instr[1:]
    arg = int(arg)
    if lett == 'N':
        y += arg
    elif lett == 'S':
        y -= arg
    elif lett == 'W':
        x -= arg
    elif lett == 'E':
        x += arg
    elif lett == 'R':
        d -= arg // 90
        d %= 4
    elif lett == 'L':
        d += arg // 90
        d %= 4
    elif lett == 'F':
        x += dir[d][0] * arg
        y += dir[d][1] * arg
print(abs(x)+abs(y))