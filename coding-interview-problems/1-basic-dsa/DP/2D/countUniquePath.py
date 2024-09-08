''''
Problem:
Count the number of unique paths from the top left to the bottom right. 
You are only allowed to move down or to the right.
'''



# Brute Force - Time: O(2 ^ (n + m)), Space: O(n + m)
def bruteForce(r, c, rows, cols):
    if r == rows or c == cols:
        return 0

    if r == rows - 1 and c == cols - 1: # reached the goal
        return 1
    
    return (bruteForce(r + 1, c, rows, cols) +  
            bruteForce(r, c + 1, rows, cols))

# print(bruteForce(0, 0, 4, 4))


# Memoization - Time and Space: O(n * m)
def memoization(r, c, rows, cols, cache):
    if r == rows or c == cols:
        return 0
    
    if r == rows - 1 and c == cols - 1: # reached the goal
        return 1

    if cache[r][c] > 0:
        return cache[r][c] # get how many ways to reach to that sub-problem
    
    cache[r][c] = (memoization(r + 1, c, rows, cols, cache) +  
                   memoization(r, c + 1, rows, cols, cache))
    
    return cache[r][c]

# print(memoization(0, 0, 4, 4, [[0] * 4 for i in range(4)]))



# Dynamic Programming - Time: O(n * m), Space: O(m), where m is num of cols
# If you understand properly this would be good solution with space optimization
def dp(m, n):
    row = [1] * n

    for i in range(m-1):
        newRow = [1] * n

        for j in range(n-2, -1, -1):
            newRow[j] =  newRow[j+1] + newRow[j]

        row =  newRow
    return row[0]



print(dp(4, 4))

