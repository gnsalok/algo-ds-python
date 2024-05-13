'''
https://leetcode.com/problems/maximum-subarray/

'''

# Brute Force: O(n^2)
def bruteForce(nums):
    maxSum = nums[0]

    for i in range(len(nums)):
        curSum = 0
        for j in range(i, len(nums)):
            curSum += nums[j]
            maxSum = max(maxSum, curSum)
    return maxSum


# Kadane's Algorithm: O(n)
def kadanes(nums):
    maxSum = nums[0]
    curSum = 0

    for n in nums:
        curSum = max(n, n+curSum) # achieve in one line
        # curSum += n # do not needed here you can achieve using above algorithm 
        maxSum = max(curSum, maxSum)
    return maxSum


arr = [4,-1,2,-7,3,4] # output
print(kadanes(arr))

