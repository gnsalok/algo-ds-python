''''
Coin Change : https://leetcode.com/problems/coin-change/
Time : O (amount * len(coin))
space : O (amount) -> DP 
'''


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount+1)
        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    '''
                    coin = 4
                    amount we want to calculate is = 7
                    dp[4] = 1 + min (dp[7], dp[7-4]) 
                    '''

                    # this is recurrence relation
                    dp[a] = min(dp[a], 1 + dp[a-c])
        return dp[-1] if dp[-1] != float("inf") else -1
                 

        