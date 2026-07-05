# https://leetcode.com/problems/top-k-frequent-elements/

'''
1. Make list from 0 to n+1
2. Make index as frequency 

'''

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        result = []

        for count in range(len(nums), -1, -1):

            # this is bcz list like this -> [[], [2,4]]
            for num in buckets[count]:
                result.append(num)

                if len(result) == k:
                    return result

        return result
            
nums = [1,2,2,2,3,3,3]
sl = Solution()
print(sl.topKFrequent(nums, 2))
