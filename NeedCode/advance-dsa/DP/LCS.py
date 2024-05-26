'''
Longest Common Subsequence 

S1 = [A,D,C,B]
S2 = [A,B,C]

LCS : A,C

Code it Now..
'''

from functools import lru_cache


## Recursive solution 
'''
TC : O(2^m+n) ; where m and n are sizes of both string array [height of decision tree]
SC : O(m+n)

Next step : Memoise the solution
'''
def LCS(s1, s2):
    def dfs(s1, s2, i1, i2):
        if i1 == len(s1) or i2 == len(s2):
            return 0
        
        if s1[i1] == s2[i2]:
            return 1 + dfs(s1, s2, i1+1, i2+1)
        else:
            return max(dfs(s1, s2, i1+1, i2), 
                        dfs(s1, s2, i1, i2+1))
    return dfs(s1, s2, 0, 0)

'''
Memoise the recursive call 

TC : O(N+M)
SC : O(N+M)


Note: If you want to complicate things with grid write using 2D array; otherwise use hashmap like below.
'''
def LCSMemo(s1, s2):
    cache = {}
    def dfs(s1, s2, i1, i2):
        if i1 == len(s1) or i2 == len(s2):
            return 0
        
        if (i1, i2) in cache:
            return cache[(i1,i2)]
        
        if s1[i1] == s2[i2]:
            cache[(i1,i2)] =  1 + dfs(s1, s2, i1+1, i2+1)
        else:
            cache[(i1,i2)] = max(dfs(s1, s2, i1+1, i2), 
                        dfs(s1, s2, i1, i2+1))
        return cache[(i1,i2)]
    return dfs(s1, s2, 0, 0)

'''
Memoisation using 2-D grid
'''
# Time: O(n * m), Space: O(n + m)
def memoization(s1, s2):
    N, M = len(s1), len(s2)
    cache = [[-1] * M for _ in range(N)]
    return memoHelper(s1, s2, 0, 0, cache)

def memoHelper(s1, s2, i1, i2, cache):
    if i1 == len(s1) or i2 == len(s2):
        return 0
    if cache[i1][i2] != -1:
        return cache[i1][i2]

    if s1[i1] == s2[i2]:
        cache[i1][i2] = 1 + memoHelper(s1, s2, i1 + 1, i2 + 1, cache)
    else:
        cache[i1][i2] = max(memoHelper(s1, s2, i1 + 1, i2, cache),
                memoHelper(s1, s2, i1, i2 + 1, cache))
    return cache[i1][i2]


# Time: O(n * m), Space: O(n + m)
def dp(s1, s2):
    N, M = len(s1), len(s2)
    dp = [[0] * (M+1) for _ in range(N+1)]

    for i in range(N):
        for j in range(M):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = 1 + dp[i][j] # look to top left diagonally (we didn't decrement i and j because we already going from i+1, j+1). Draw it.
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp[N][M]


# Time: O(n * m), Space: O(m)
def optimizedDp(s1, s2):
    N, M = len(s1), len(s2)
    dp = [0] * (M + 1)

    for i in range(N):
        curRow = [0] * (M + 1)
        for j in range(M):
            if s1[i] == s2[j]:
                curRow[j+1] = 1 + dp[j]
            else:
                curRow[j+1] = max(dp[j + 1], curRow[j])
        dp = curRow
    return dp[M]

s1 = ["A","D","C","B"]
s2 = ["A","B","C"]

print(LCSMemo(s1, s2))