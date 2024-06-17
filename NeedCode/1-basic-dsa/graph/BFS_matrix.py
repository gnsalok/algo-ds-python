'''
Matrix BFS in Grid

Find the length of the shortest path from the top left of the grid to the bottom right.

'''

from collections import deque

def bfs(matrix, start):
    # Directions for moving in the matrix
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    queue = deque([start])
    visited.add((0,0))

    while queue:
        row, col = queue.popleft()
        
        # Process the current cell
        print(f"Visiting cell ({row}, {col}) with value {matrix[row][col]}")
        
        # Check all four possible directions
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            # Check if the new position is within bounds and not visited
            if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                queue.append((new_row, new_col))

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

start_position = (0, 0)  # Starting at the top-left corner
bfs(matrix, start_position)
