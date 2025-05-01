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


'''
Other solution with extra memory
'''

def trap(h):
    
    totalWater = 0

    maxLArr = [0]
    maxRArr = [0]

    maxL = 0
    maxR = h[-1]

    # calculate max left and store
    for i in range(1, len(h)):
        maxL = max(maxL, h[i-1])
        maxLArr.append(maxL)
    
    # calculate max right and store 
    for i in range(len(h)-2,-1,-1):
        maxR = max(maxR,h[i+1])
        maxRArr.insert(0, maxR)


    # Now compare both array with formula : min(l, r) - h[i]
    for i, (x, y) in enumerate(zip(maxLArr, maxRArr)):
        if min(x, y) - h[i] >=0:
            totalWater += min(x, y) - h[i]

    print(totalWater)


height = [0,1,0,2,1,0,1,3,2,1,2,1]
trap(height)