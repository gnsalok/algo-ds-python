
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        totalSum = 0
        result = float("inf")

        for r in range(len(nums)):
            totalSum += nums[r]
            while totalSum >= target:
                result = min(r-l+1, result)
                totalSum -= nums[l]
                l += 1

        return 0 if result == float("inf") else result

target = 10
nums = [2,1,5,1,5,3]

sl = Solution()
print(sl.minSubArrayLen(target, nums))