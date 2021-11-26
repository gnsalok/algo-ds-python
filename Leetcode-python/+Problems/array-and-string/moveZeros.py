'''
Leetcode #283 -- Counting Sort - 
Input : 0,1,0,3,12 --> 1,3,12,0,0 (Maintain the relative order)

TC : O(2*N) --> O(N)
SP : O(1)
'''
from typing import List

class Solution:
    def moveZeros(self, nums: List[int]) -> None:
        j = 0
        n = len(nums)

        for num in nums:
            if(num!=0):
                nums[j] = num
                j += 1

        for x in range(j, n):
            arr[x] = 0


arr = [0,1,0,3,12]
sl = Solution()
sl.moveZeros(arr)
print(arr)


