def mines_adj(grid):
    n = len(grid)
    if(n == 0):
        return
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
    m = len(grid[0])
    newgrid = [["#" for j in range(m)] for i in range(n)]
    for r in range(n):
        for c in range(m):
            if(grid[r][c] == "-"):
                count = 0
                for dir in directions:
                    nr = r + dir[0]
                    nc = c + dir[1]
                    if(nr >= 0 and nr < n and nc >=0 and nc < m and grid[nr][nc] == "#"):
                        count = count + 1
                newgrid[r][c] = count
    return newgrid
grid = [["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"]]

newgrid = mines_adj(grid)
print(newgrid)