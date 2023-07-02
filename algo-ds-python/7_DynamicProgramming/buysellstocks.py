from typing import List 



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = 1<<32 #max int/float value   
        profit = 0

        for i, price in enumerate(prices):
            if(buyPrice > price):
                buyPrice = price
                print("BP : ", buyPrice)
            else:
                profit = max(profit, price-buyPrice)
                print("Profit : ",profit)
        return profit

prices = [7,1,5,3,6,4]  
sl = Solution()
print(sl.maxProfit(prices))  # ans is 5 ; bought price is 1 and sell for 6 > max profile 6 - 1 = 5