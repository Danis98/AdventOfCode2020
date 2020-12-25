input = open("day24.input", "r").read().strip().split("\n")

d = {
    'e': (0, 1),
    'w': (0, -1),
    'ne': (-1, 0),
    'nw': (-1, -1),
    'se': (1, 1),
    'sw': (1, 0)
}
grid = {}
for line in input:
    p = 0
    pos = (0, 0)
    while p < len(line):
        if line[p] in 'ew':
            dir = line[p]
            p += 1
        elif line[p] in 'ns':
            dir = line[p:p+2]
            p += 2
        pos = (pos[0]+d[dir][0], pos[1]+d[dir][1])
    if pos not in grid:
        grid[pos] = 0
    grid[pos] = 1 - grid[pos]

s = 0
for pos in grid:
    if grid[pos] == 1:
        s += 1
print(s)