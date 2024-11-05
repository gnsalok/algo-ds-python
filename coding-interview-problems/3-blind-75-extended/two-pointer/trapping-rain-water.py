'''

https://leetcode.com/problems/trapping-rain-water/

'''




class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l , r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        totalWater = 0

        while l < r:
            if maxL < maxR:
                # shift right and update the maxL and totalWater
                l += 1
                maxL = max(maxL, height[l])

                '''
                Note : maxR is not required to calculate the totalWater.
                As we are updating pointer based on minimum value, which is bottleneck for trapping water.
                '''
                
                totalWater += maxL - height[l]

            else:
                # shift right and update the maxR and totalWater
                r -= 1
                maxR = max(maxR, height[r])
                totalWater += maxR - height[r]

        return totalWater
