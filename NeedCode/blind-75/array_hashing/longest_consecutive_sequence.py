
''' 
Longest consecutive Sequence : https://leetcode.com/problems/longest-consecutive-sequence/

TC : O N
SC : O N
'''

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            # check if it's start of sequence
            # if there is no n-1 means it's starting of sequence
            if (n-1) not in numSet:
                
                length = 0
                # check the n+1 count if consecutive number found
                # if n+legth exist is set means, there is sequence, just count how long it is.
                while (n+length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest


sl = Solution()
nums = [100,4,200,1,3,2]
answer = sl.longestConsecutive(nums)
print(answer)