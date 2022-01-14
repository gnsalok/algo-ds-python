'''
Climbing N Stairs.
You can take either 1 or 2 steps at a time.
'''

class Solution:
    def climbingStairs(self, n):
        # takes 1 step to reach 1 
        if(n == 1): 
            return 1

        dp = [0] * (n+1) # take dp array to n+1
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
            print(dp)
        return dp[n]

if __name__ == "__main__":
    sl = Solution()
    print(sl.climbingStairs(4))