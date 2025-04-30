'''
Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/description/

DP : O(n^2)
'''

def lengthOfLIS(nums):
    LIS = [1] * len(nums)

    for i in range(len(nums)-1, -1, -1):
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1+LIS[j])
    
    return max(LIS)



nums = [1,2,3,4]
print(lengthOfLIS(nums)) # answer: 4