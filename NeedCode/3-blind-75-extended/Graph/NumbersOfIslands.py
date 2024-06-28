'''
https://leetcode.com/problems/number-of-islands/
'''

import collections
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()

        islands = 0

        # iterative algorithm
        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                            # right, left,    up,      down
                directions = [[1,0], [-1,0], [0,-1], [0,1]]

                for dr, dc in directions:
                    new_row, new_col = dr + row, col + dc

                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == "1" and (new_row, new_col) not in visit:
                        q.append((new_row, new_col))
                        visit.add((new_row, new_col))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
        return islands


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
sl = Solution()

print(sl.numIslands(grid)) # output is 1