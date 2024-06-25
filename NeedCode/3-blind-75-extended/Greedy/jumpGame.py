'''
https://leetcode.com/problems/jump-game/

TC : O(N)

'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            '''This his means that if you start at index `i` and jump `nums[i]` 
            steps, you can either reach or go beyond the current `goal`
            '''
            if i + nums[i] >= goal:
                goal = i
            
        if goal == 0:
            return True
        else:
            return False


#-- Simple Solution 


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        goal = len(nums) - 1 # which will be last index

        maxSoFar = 0

        for i, n in enumerate(nums):

            # it means you can't reach me
            if i > maxSoFar:
                return False 

            curMax = i + n
            maxSoFar = max(maxSoFar, curMax)

        if maxSoFar >= goal:
            return True
        else:
            return False