'''
Leetcode : sort colors 

Time : O(N)
Space : O(1)

Dutch-Partitioning Algorithm sorts in one pass.
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



nums = [2,0,2,1,1,0]
sortColors(nums)
print(nums)

    