# https://leetcode.com/problems/top-k-frequent-elements/

'''
1. Make list from 0 to n+1
2. Make index as frequency 

'''

from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        result = []

        for count in range(len(nums), 0, -1):

            # this is bcz list like this -> [[], [2,4]]
            for num in buckets[count]:
                result.append(num)

                if len(result) == k:
                    return result

        return result
            
nums = [1,2,2,2,3,3,3]
sl = Solution()
print(sl.topKFrequent(nums, 2))


'''
- heapq version of it


import heapq
from collections import Counter

def topKFrequent(nums, k):
    # 1. Count the frequency of every number
    # Example: [1,1,1,2,2,3] -> {1: 3, 2: 2, 3: 1}
    count = Counter(nums)
    
    # 2. Use a min-heap to keep track of the top k elements
    heap = []
    
    for num, freq in count.items():
        # Push a tuple of (frequency, number) into the heap
        # Python's heapq sorts tuples by the first element (frequency)
        heapq.heappush(heap, (freq, num))
        
        # If the heap gets larger than k, remove the one with the smallest frequency
        if len(heap) > k:
            heapq.heappop(heap)

    result = []
    for _,v in heap:
        result.append(v)
    return result


'''