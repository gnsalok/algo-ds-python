'''

It is solve by Kadans Algorithms

TC : O(n)
SC : O(n)

'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0

        # this is Kadans Algorithm
        for n in nums:
            curSum = max(n, n + curSum) # this will handle -ve sum total ; if get positive then choose positive
            maxSum = max(curSum, maxSum)
        return maxSum
