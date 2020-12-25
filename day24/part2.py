input = open("day24.input", "r").read().strip().split("\n")

d = {
    'e': (0, 1),
    'w': (0, -1),
    'ne': (-1, 0),
    'nw': (-1, -1),
    'se': (1, 1),
    'sw': (1, 0)
}

def count_neigh(grid, r, c, d):
    ctr = 0
    for dir in d:
        i = r + d[dir][0]
        j = c + d[dir][1]
        if (i, j) in grid and grid[(i,j)] == 1:
            ctr += 1
    return ctr

def evolve(grid, x, y):
    state = grid[(x, y)] if (x, y) in grid else 0
    neigh = count_neigh(grid, x, y, d)
    if state == 1:
        if neigh == 0 or neigh > 2:
            return 0
        else:
            return 1
    else:
        if neigh == 2:
            return 1
        else:
            return 0

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

for t in range(100):
    temp_grid = {}
    for pos in grid:
        if grid[pos] == 0:
            continue
        x, y = pos
        temp_grid[pos] = evolve(grid, x, y)
        for dir in d:
            i = x + d[dir][0]
            j = y + d[dir][1]
            temp_grid[(i, j)] = evolve(grid, i, j)
    grid = temp_grid
num = len([p for p in grid if grid[p] == 1])
print(num)
