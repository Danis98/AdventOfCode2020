input = open("day17.input", "r").read().strip().split("\n")

def count_neigh(grid, x, y, z, w):
    ctr = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            for k in range(z-1, z+2):
                for l in range(w-1, w+2):
                    if i == x and j == y and k == z and l == w:
                        continue
                    if (i, j, k, l) in grid and grid[(i, j, k, l)] == '#':
                        ctr += 1
    return ctr

def evolve(grid, x, y, z, w):
    state = grid[(x, y, z, w)] if (x, y, z, w) in grid else '.'
    neigh = count_neigh(grid, x, y, z, w)
    if state == '#':
        if neigh in [2, 3]:
            return '#'
        else:
            return '.'
    else:
        if neigh == 3:
            return '#'
        else:
            return '.'
grid = {}
for y in range(len(input)):
    for x in range(len(input[0])):
        if input[y][x] == '#':
            grid[(x, y, 0, 0)] = '#'

for t in range(6):
    temp_grid = {}
    for pos in grid:
        if grid[pos] == '.':
            continue
        x, y, z, w = pos
        temp_grid[pos] = evolve(grid, x, y, z, w)
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                for k in range(z-1, z+2):
                    for l in range(w-1, w+2):
                        temp_grid[(i, j, k, l)] = evolve(grid, i, j, k, l)
    grid = temp_grid
num = len([p for p in grid if grid[p] == '#'])
print(num)
