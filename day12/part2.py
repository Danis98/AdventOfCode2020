input = open("day12.input", "r").read().strip().split("\n")

wx, wy = (10, 1)
sx, sy = (0, 0)
for instr in input:
    lett, arg = instr[:1], instr[1:]
    arg = int(arg)
    if lett == 'N':
        wy += arg
    elif lett == 'S':
        wy -= arg
    elif lett == 'W':
        wx -= arg
    elif lett == 'E':
        wx += arg
    elif lett == 'R':
        for i in range(arg//90):
            wx, wy = wy, -wx
    elif lett == 'L':
        for i in range(arg//90):
            wx, wy = -wy, wx
    elif lett == 'F':
        sx, sy = sx+arg*wx, sy+arg*wy
print(abs(sx)+abs(sy))