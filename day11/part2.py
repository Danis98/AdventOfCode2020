grid = open("day11.input", "r").read().strip().split("\n")

def count_neigh(grid, r, c):
    ctr = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            for d in range(1, min(len(grid), len(grid[0]))):
                nr = r + d*i
                nc = c + d*j
                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                    break
                if grid[nr][nc] == '#':
                    ctr += 1
                if grid[nr][nc] != '.':
                    break
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
            elif grid[r][c] == '#' and n >= 5:
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