# def dfs(profit, weight, capacity):
#     return dfsHelper(0, profit, weight, capacity)

# top-down code
def dfsHelper(i, profit, weight, capacity):
    if i == len(profit):
        return 0

    # Skip item i
    maxProfit = dfsHelper(i + 1, profit, weight, capacity)

    # Include item i
    newCap = capacity - weight[i]
    if newCap >= 0:
        p = profit[i] + dfsHelper(i + 1, profit, weight, newCap)
        # Compute the max
        maxProfit = max(maxProfit, p)

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

## ------------ >>>>>> --------------------

# author : @ Alok Tripathi

##  My version start with base condition (Bottom-up)

# Brute force Solution
# Time: O(2^n), Space: O(n)
# Where n is the number of items.
def dfs(profit, weight, capacity):
    return dfsHelper(profit, weight, capacity, len(profit))

# bottom-up : recursive 
def dfsHelper(profit, weight, capacity, size):
    if size == 0:
        return 0
    maxProfit = 0
    # Include item last item case 
    # if we have capacity
    newCap = capacity - weight[size-1]
    if newCap>=0:
        #   val at nth profit + (n-1)th profit
        maxProfit = max(profit[size-1] + dfsHelper(profit, weight, newCap, size-1),
                            dfsHelper(profit, weight, capacity, size-1))
    return maxProfit




## Memoization 

# Dynamic Programming Solution
# Time: O(n * m), Space: O(n * m)
# Where n is the number of items & m is the capacity.
def memo(profit, weight, capacity):
    '''
    Note : -
    if you see recursive solution, then profit and capacity params are changing (meaning, its keep calculating in recursive call)
    Cache that information and use if when it attempt to calculate again.
    '''

    # A 2D array with N  rows and M columns 
    N, M = len(profit), capacity
    cache = [[-1]+(M+1) for r in range(N)]
    return memoHelper(profit, weight, capacity, len(profit), cache)

# bottom-up : recursive 
def memoHelper(profit, weight, capacity, size, cache):
    if size == 0:
        return 0
    
    if cache[size-1][capacity] != -1:
        return cache[size-1][capacity]
    

    maxProfit = 0
    # Include item last item case 
    # if we have capacity
    newCap = capacity - weight[size-1]
    if newCap>=0:
        # Choice :
        # for choosing val at nth profit + (n-1)th profit or skip ; if you skip you end up getting nth val only
                          
        cache[size-1][capacity] = max(profit[size-1] + memoHelper(profit, weight, newCap, size-1, cache),
                            memoHelper(profit, weight, capacity, size-1, cache))
    return cache[size-1][capacity] 

profit = [4, 4, 7, 1]
weight = [5, 2, 3, 1]
cap = 8
print(dfs(profit, weight, cap)) # 12
