'''
https://leetcode.com/problems/jump-game/

TC : O(N)

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


Note:
If there is 0 in the array you cant reach to the end. Array without 0 is will lead to you result.

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