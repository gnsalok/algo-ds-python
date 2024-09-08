'''
https://leetcode.com/problems/climbing-stairs/description/
Very good explanation : https://www.youtube.com/watch?v=Y0lT9Fck7qI

TC : O(N)
'''
class Solution:
    def climbStairs(self, n):
        one, two = 1, 1

        # counting from 0
        for i in range(n-1):
            temp = one
            one = one + two 
            two = temp
        return one
