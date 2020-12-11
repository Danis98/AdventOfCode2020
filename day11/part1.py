grid = open("day11.input", "r").read().strip().split("\n")

def count_neigh(grid, r, c):
    ctr = 0
    for i in range(max(0, r-1), min(len(grid), r+2)):
        for j in range(max(0, c-1), min(len(grid[0]), c+2)):
            if i == r and j == c:
                continue
            if grid[i][j] == '#':
                ctr += 1
    return ctr

iter = 0
while True:
    tmp_grid = [[grid[i][j] for j in range(len(grid[0]))] for i in range(len(grid))]
    change = False
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == '.':
                continue
            n = count_neigh(grid, r, c)
            if grid[r][c] == 'L' and n == 0:
                change = True
                tmp_grid[r][c] = '#'
            elif grid[r][c] == '#' and n >= 4:
                change = True
                tmp_grid[r][c] = 'L'
    iter += 1
    if not change:
        break
    grid = [[tmp_grid[i][j] for j in range(len(grid[0]))] for i in range(len(grid))]
    # for r in grid:
    #     print(''.join(r))
    # for r in range(len(grid)):
    #     print(''.join([str(count_neigh(grid, r, c)) if grid[r][c] != '.' else '.' for c in range(len(grid[0]))]))
    # print("-----------------")

occ = sum(map(lambda x: x.count('#'), grid))
print(occ)