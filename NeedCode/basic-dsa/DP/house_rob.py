'''
https://leetcode.com/problems/house-robber/

'''

from typing import List

# class Solution:
    # def rob(self, nums, size):
    #     if size == 0:
    #         return 0
        
    #     dp = [0] * size
    #     dp[0] = nums[0]
    #     dp[1] = max(nums[0], nums[1])

    #     for i in range(2, size):
    #         dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    #     return dp[-1]


class Solution:
    def rob(self, nums):
        # size = len(nums)
        # if size == 0:
        #     return 0
        
        # dp = [0] * size
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])

        # for i in range(2, size):
        #     dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        # return dp[-1]

        size = len(nums)

        if size == 0:
            return 0

        if size == 1:
            return nums[0]

        return max(self.rob(nums[1:]), nums[0]+self.rob(nums[2:]))
    


'''
 Recursive solution ; worse time complexity; but good to look
'''       

# class Solution:
#     def rob(self, nums):
#         size = len(nums)

#         if size == 0:
#             return 0

#         if size == 1:
#             return nums[0] 

#         return max(self.rob(nums[1:]), nums[0]+self.rob(nums[2:]))

       

sl = Solution()
nums = [1,2,3,1]
print(sl.rob(nums))