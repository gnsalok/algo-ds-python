'''
Good Article:
https://leetcode.com/discuss/study-guide/1490172/Dynamic-programming-is-simple


https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/

# Recurrence Relation L:

- When we buy a stock, we spend money (+ pay the fee) and therefore decreasing whatever profit we get from the next recursive call
- When we sell the stock, we get money back => increasing profit
- When we do nothing, profit doesn't change

'''
from functools import lru_cache
from typing import List

# class Solution:
#     def maxProfit(self, prices: List[int], fee: int) -> int:
#         def dp(pos: int, bought: bool) -> int:
#             if pos == len(prices):
#                 return 0  # base case

#             max_profit = 0

#             if not bought:
#                 # Buy stock
#                 max_profit = max(max_profit, dp(pos + 1, True) - prices[pos] - fee)
#             else:
#                 # Sell stock
#                 max_profit = max(max_profit, dp(pos + 1, False) + prices[pos])

#             # Do nothing
#             max_profit = max(max_profit, dp(pos + 1, bought))

#             return max_profit

#         return dp(0, False)


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # @lru_cache(None)
        def dp(pos: int, bought: bool) -> int:
            cache = {}
            if pos == len(prices):
                return 0  # base case
            
            if (pos, bought) in cache:
                return cache[(pos, bought)]

            cache[(pos, bought)] = 0

            if not bought:
                # Buy stock 
                cache[(pos, bought)] = max(cache[(pos, bought)], dp(pos + 1, True) - prices[pos] - fee)
            else:
                # Sell stock
                cache[(pos, bought)] = max(cache[(pos, bought)], dp(pos + 1, False) + prices[pos])

            # Do nothing
            cache[(pos, bought)] = max(cache[(pos, bought)], dp(pos + 1, bought))

            return cache[(pos, bought)]

        return dp(0, False)
        


sl = Solution()
prices = [1,3,2,8,4,9]
fee = 2

print(sl.maxProfit(prices, fee))