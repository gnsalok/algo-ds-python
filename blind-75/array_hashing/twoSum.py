from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i,n in enumerate(nums):
            find = target - n

            if find in map:
                return [map[find],i]
            else:
                map[n] = i
    

