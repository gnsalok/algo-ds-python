'''
https://neetcode.io/problems/matrixBFS

'''

from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:

        # Directions for moving in the matrix
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows, cols = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        queue.append((0,0,0))

        # Check if the start or end cell is blocked
        if grid[0][0] != 0 or grid[rows-1][cols-1] != 0:
            return -1
        
        # Mark the starting cell as visited
        visited.add((0,0))
        length = 0
        
        while queue:
            row, col, length = queue.popleft()
            
            if (row, col) == (rows-1,cols-1):
                return length

            # Check all four possible directions
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check if the new position is within bounds and not visited
                if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited and grid[new_row][new_col] == 0:
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, length + 1)) 
        return -1
        