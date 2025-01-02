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
                    dp[7] = 1 + dp[4-3] could be one possible solution ; here 1 is for coin
                    '''

                    # this is recurrence relation
                    dp[a] = min(dp[a], 1 + dp[a-c])
        return dp[-1] if dp[-1] != float("inf") else -1
                 


# ----
# Solution with memoization

'''
Time complexity: O(length of count ∗ amount)
Space complexity: O(amount)
'''


def coinChange(amount, coins):
    memo = {}
    def dfs(amount):
        if amount == 0:
            return 0

        if amount in memo:
            return memo[amount]
        
        res = float("inf")

        for coin in coins:
            if amount - coin >= 0:
                res = min(res, 1 + dfs(amount - coin))
            memo[amount] = res
        return res

    minCoins = dfs(amount)
    return -1 if minCoins >= float("inf") else minCoins