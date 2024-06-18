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

        