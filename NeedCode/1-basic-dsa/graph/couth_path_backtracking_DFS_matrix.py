'''
Count the unique paths from the top left to the bottom right. 
A single path may only move along 0's and can't visit the same cell more that once.


TC : 4^N*M         - where 4 is the branches of each cell in the grid to find way to reach destination.
'''

# Matrix (2D Grid)
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

# Count paths (backtracking)
def dfs(grid, r, c, visit):
    ROWS, COLS = len(grid), len(grid[0])
    if (min(r, c) < 0 or
        (r == ROWS or c == COLS) or # check r and c are not going above grid's rows and columns
        (r, c) in visit or grid[r][c] == 1):
        return 0
    
    # reached final destination (end of matrix); return 1, meaning you get one unique path.
    if r == ROWS - 1 and c == COLS - 1:
        return 1

    visit.add((r, c))

    count = 0

    # move all 4 direction ; if hit base case then try other path
    count += dfs(grid, r + 1, c, visit)
    count += dfs(grid, r - 1, c, visit)
    count += dfs(grid, r, c + 1, visit)
    count += dfs(grid, r, c - 1, visit)

    # removal is important bcz some other node can visit and form a unique path
    visit.remove((r, c))
    return count
