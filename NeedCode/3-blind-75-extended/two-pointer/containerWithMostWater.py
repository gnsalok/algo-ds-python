'''
https://leetcode.com/problems/container-with-most-water/description/
> (r - l) is for horizontal distance
> height - you can take min of left and right 

TC : O(n)
'''


class Solution:
    def maxArea(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1
        res = 0
        
        while l < r :
            area = (r - l) * min(height[l], height[r])
            res = max(area, res)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
        