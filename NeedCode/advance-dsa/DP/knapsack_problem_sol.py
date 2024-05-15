# Brute force Solution
# Time: O(2^n), Space: O(n)
# Where n is the number of items.
def dfs(profit, weight, capacity):
    return dfsHelper(0, profit, weight, capacity)

def dfsHelper(i, profit, weight, capacity):
    if i == len(profit):
        return 0

    maxProfit = 0

    # Include item i
    newCap = capacity - weight[i]
    if newCap >= 0:
                    # include the profit at pos
        maxProfit = max(profit[i] + dfsHelper(i + 1, profit, weight, newCap), 
                        # not include the profit
                        dfsHelper(i + 1, profit, weight, capacity))
    return maxProfit

# Memoization Solution
# Time: O(n * m), Space: O(n * m)
# Where n is the number of items & m is the capacity.
def memoization(profit, weight, capacity):
    # A 2d array, with N rows and M + 1 columns, init with -1's
    N, M = len(profit), capacity
    cache = [[-1] * (M + 1) for _ in range(N)]
    return memoHelper(0, profit, weight, capacity, cache)

def memoHelper(i, profit, weight, capacity, cache):
    if i == len(profit):
        return 0
    if cache[i][capacity] != -1:
        return cache[i][capacity]

    # Skip item i
    cache[i][capacity] = memoHelper(i + 1, profit, weight, capacity, cache)
    
    # Include item i
    newCap = capacity - weight[i]
    if newCap >= 0:
        p = profit[i] + memoHelper(i + 1, profit, weight, newCap, cache)
        # Compute the max
        cache[i][capacity] = max(cache[i][capacity], p)

    return cache[i][capacity]



# Memoization Solution (Using HashMap -- Easy to write)
# Time: O(n * m), Space: O(n * m) ## similar time complexity
# Where n is the number of items & m is the capacity.
def memoizationHashMap(profit, weight, capacity):
    cache = {}
    return memoHelperH(0, profit, weight, capacity, cache)

def memoHelperH(i, profit, weight, capacity, cache):
    if i == len(profit):
        return 0
    
    # check if (items, capacity) pairs in map
    if (i, capacity) in cache:
        return cache[(i, capacity)]

    # Skip item i (profits)
    cache[(i, capacity)] = memoHelperH(i + 1, profit, weight, capacity, cache)
    
    # Include item i
    newCap = capacity - weight[i]
    if newCap >= 0:
        p = profit[i] + memoHelperH(i + 1, profit, weight, newCap, cache)
        # Compute the max
        cache[(i, capacity)] = max(cache[(i, capacity)], p)

    return cache[(i, capacity)]


## -----------------------------------
# ----  True DP approach ---- (tables)
## ----------------------------------


# this is not totally optimize, still we can optimize space 
# Dynamic Programming Solution
# Time: O(n * m), Space: O(n * m)
# Where n is the number of items & m is the capacity.
def dp(profit, weight, capacity):
    N, M = len(profit), capacity
    dp = [[0] * (M + 1) for _ in range(N)]

    # Fill the first column and row to reduce edge cases
    for i in range(N):
        dp[i][0] = 0
    for c in range(M + 1):
        if weight[0] <= c:
            dp[0][c] = profit[0] 

    for i in range(1, N):
        for c in range(1, M + 1):
            skip = dp[i-1][c]
            include = 0
            if c - weight[i] >= 0:
                include = profit[i] + dp[i-1][c - weight[i]]
            dp[i][c] = max(include, skip)
    return dp[N-1][M]


# Memory optimized Dynamic Programming Solution
# Time: O(n * m), Space: O(m)
def optimizedDp(profit, weight, capacity):
    N, M = len(profit), capacity
    dp = [0] * (M + 1)

    # Fill the first row to reduce edge cases
    for c in range(M + 1):
        if weight[0] <= c:
            dp[c] = profit[0] 

    for i in range(1, N):
        curRow = [0] * (M + 1)
        for c in range(1, M + 1):
            skip = dp[c]
            include = 0
            if c - weight[i] >= 0:
                include = profit[i] + dp[c - weight[i]]
            curRow[c] = max(include, skip)
        dp = curRow
    return dp[M]


profit = [4, 4, 7, 1]
weight = [5, 2, 3, 1]
cap = 8
print(memoizationHashMap(profit, weight, cap)) # 12