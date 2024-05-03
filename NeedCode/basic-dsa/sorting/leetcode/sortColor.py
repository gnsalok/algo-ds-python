'''
https://leetcode.com/problems/sort-colors/
'''

## First Solution : Use Bucket Sort

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # this is count of 0,1,2
        counts = [0,0,0]

        for n in nums:
            counts[n] += 1

        arrIdx = 0

        for i in range(len(counts)):
            for j in range(counts[i]):
                nums[arrIdx] = i
                arrIdx += 1
            

## Second Solution : Use Dutch Partitioning Algorithm (low, mid, high ptr approach) in O(N) times

'''
Leetcode : sort colors 

Time : O(N)
Space : O(1)v # No extra space required.

Dutch-Partitoining Algorithm sorts in one pass.
'''

def sortColors(nums):
    low = mid = 0
    high = len(nums) - 1

    while(mid <= high):
        if(nums[mid] == 0):
            nums[low], nums[mid] = nums[mid], nums[low]
            mid += 1
            low += 1
        elif(nums[mid] == 1):
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1




