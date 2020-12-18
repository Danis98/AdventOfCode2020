input = open("day17.input", "r").read().strip().split("\n")

def count_neigh(grid, x, y, z):
    ctr = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            for k in range(z-1, z+2):
                if i == x and j == y and k == z:
                    continue
                if (i, j, k) in grid and grid[(i, j, k)] == '#':
                    ctr += 1
    return ctr

def evolve(grid, x, y, z):
    state = grid[(x, y, z)] if (x, y, z) in grid else '.'
    neigh = count_neigh(grid, x, y, z)
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
            grid[(x, y, 0)] = '#'

for t in range(6):
    temp_grid = {}
    for pos in grid:
        if grid[pos] == '.':
            continue
        x, y, z = pos
        temp_grid[pos] = evolve(grid, x, y, z)
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                for k in range(z-1, z+2):
                    temp_grid[(i, j, k)] = evolve(grid, i, j, k)
    grid = temp_grid
num = len([p for p in grid if grid[p] == '#'])
print(num)
