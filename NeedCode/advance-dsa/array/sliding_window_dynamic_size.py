# Find the length of longest subarray with the same number
# value in each position: O(n)
def longestSubarray(nums):
    length = 0
    L = 0
    
    for R in range(len(nums)):
        if nums[L] != nums[R]:
            L = R 
        length = max(length, R - L + 1)
    return length

# Find length of the minimum size subarray where the sum is 
# greater than or equal to the target.
# Assume all values in the input are positive.
# O(n)
def shortestSubarray(nums, target):
    L, total = 0, 0
    length = float("inf")
    
    for R in range(len(nums)):
        total += nums[R]

        # this inner loop is to find min length of subarray 
        # but it will not going to execute all the time. - DO DRY RUN
        # TC. for whole solution assumed as O(N) 
        while total >= target:
            length = min(R - L + 1, length)
            total -= nums[L]
            L += 1
    return 0 if length == float("inf") else length
