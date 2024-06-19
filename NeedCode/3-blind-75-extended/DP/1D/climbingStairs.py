'''
climb stairs 
- https://leetcode.com/problems/climbing-stairs/

'''
class Solution:
    def climbStairs(self, n):
        # recursive solution
        # if n == 0:
        #     return 0
    
        # return self.climbStairs(n-1) + 1 # 1 is the count of n which is last step


        # Using 2 ptr technique 
        one_step = 1
        two_step = 2

        for i in range(2, n):
            temp = two_step
            next_step = one_step + two_step
            one_step = two_step
            two_step = next_step

        return two_step


