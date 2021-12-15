'''
Leetcode #283 -- Counting Sort - 
Input : 0,1,0,3,12 --> 1,3,12,0,0 (Maintain the relative order)

TC : O(2*N) --> O(N)
SP : O(1)
'''
from typing import List

class Solution:
    def moveZeros(self, nums: List[int]) -> None:
        count = 0
        for num in nums:
            if(num != 0):
                nums[count] = num
                count += 1
           
        for i in range(count, len(nums)): 
            nums[i] = 0





arr = [0,1,0,3,12]
sl = Solution()
sl.moveZeros(arr)
print(arr)


