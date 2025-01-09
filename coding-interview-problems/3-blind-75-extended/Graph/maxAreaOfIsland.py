
"""
https://leetcode.com/problems/max-area-of-island/

"""



class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()

        maxIslands = 0
        
        # iterative algorithm_
        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r,c))
            islands_size = 0
            

            while q:
                row, col = q.popleft()
                            # down,   up,     left,  right  # visualize in matrix [[]*col for _ in range(row)]
                directions = [[1,0], [-1,0], [0,-1], [0,1]]

                for dr, dc in directions:
                    new_row, new_col = dr + row, col + dc

                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1 and (new_row, new_col) not in visit:
                        q.append((new_row, new_col))
                        visit.add((new_row, new_col))
                        islands_size += 1
            return islands_size
   
                       

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    islands_size = bfs(r,c)
                    maxIslands = max(maxIslands, islands_size + 1)
        return maxIslands

        