'''
1-D BFS Approach to achieve linear time complexity
'''


class Solution:
    def jump(self, nums: List[int]) -> int:
        minJumpToReachToEnd = 0
        l = r = 0

        while r < len(nums) - 1:
            maxJumpSoFar = 0
            for i in range(l, r + 1):
                maxJumpSoFar = max(maxJumpSoFar, nums[i]+i)

            l = r + 1
            r = maxJumpSoFar
            minJumpToReachToEnd += 1

        return minJumpToReachToEnd

