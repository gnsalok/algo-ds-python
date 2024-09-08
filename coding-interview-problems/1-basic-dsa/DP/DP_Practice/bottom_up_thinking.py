## 

'''
We can find the largest number in an array using top-down recursion.


Find the largest value in the array. (Using Recursion)
'''

# This is top-down approach to solve a problem or Recursive Solution

def findLargest(nums, firstIdx, lastIdx):
    if firstIdx == lastIdx:
        return nums[firstIdx]
    
    mid = (firstIdx + lastIdx) // 2
    firstHalfLargest = findLargest(nums, firstIdx, mid)
    secondLargest = findLargest(nums, mid + 1, lastIdx)

    return max(firstHalfLargest, secondLargest)






nums = [1,2,4,8,5,9]
result = findLargest(nums, 0, len(nums)-1)
print(result)