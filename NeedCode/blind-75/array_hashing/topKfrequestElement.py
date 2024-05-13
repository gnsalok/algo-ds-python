# https://leetcode.com/problems/top-k-frequent-elements/

from typing import List
class Solution:

    '''
    TC : O N
    SP : O N
    '''
    # Solution using hashmap
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        frequency = [[] for i in range(len(nums+1))]
        for n in nums:
            seen[n] = seen.get(n,0) + 1

        for n, c in seen.items():
            frequency[c].append(n)

        return 
        
    





sl = Solution()
sl.topKFrequent([1,1,1,2,2,3], 2)