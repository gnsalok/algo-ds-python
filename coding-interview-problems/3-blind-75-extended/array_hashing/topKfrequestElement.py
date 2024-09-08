# https://leetcode.com/problems/top-k-frequent-elements/

'''
1. Make list from 0 to n+1
2. Make index as frequency 

'''

from typing import Counter, List
class Solution:

    '''
    TC : O N
    SP : O N
    '''

    
    # Solution using hashmap
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter = Counter(nums)
        buckets = [0] * (n+1)

        for num, freq in counter.items():
            if buckets[freq] == 0:
                buckets[freq] = [num]
            else:
                buckets[freq].append(num)

        print(buckets)
        
        kFreqElements = []

        for i in range(n,0,-1):
            if buckets[i] != 0:
                kFreqElements.extend(buckets[i])
            
            if len(kFreqElements) == k:
                return kFreqElements
            
nums = [1,2,2,2,3,3,3]
sl = Solution()
print(sl.topKFrequent(nums, 2))
