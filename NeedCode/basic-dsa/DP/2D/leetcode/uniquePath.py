'''

TC : O(n*m)
SC : O(n*m)
https://leetcode.com/problems/unique-paths/


Suggestion:-
You can optimize this solution in terms of space complexity from 
O(n*m) to O(2*m) -> O(m) by using bottom-up (true DP) approach.

'''


class Solution:
    def uniquePaths(self, r: int, c: int) -> int:

        # inner function to cache the compute of each unique path
        def memoization_uniquePaths(r, c, rows, cols, cache):

            # base cases ; make sure it's inbound
            if r == rows or c == cols:
                return 0

            # reached at the goal
            if r == rows-1 and c == cols-1:
                return 1

            # cache the result if it's greater than 1
            if cache[r][c] > 0:
                return cache[r][c]

            cache[r][c] = (memoization_uniquePaths(r+1,c,rows, cols, cache) +
                            memoization_uniquePaths(r, c+1, rows, cols, cache))
            
            return cache[r][c]
        
        return memoization_uniquePaths(0, 0, r , c, [[0]*c for i in range(r)])


        