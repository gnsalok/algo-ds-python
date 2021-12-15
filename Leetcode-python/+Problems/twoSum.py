'''
Time : O(n)
Space : O(n)
'''

class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        for i in range(0,len(nums)):
            goal = target - nums[i]
            if goal in map:
                return [map[goal], i]
            map[nums[i]] = i
            
if __name__ == "__main__":
    sl = Solution()
    arr = [2,7,11,15]
    target = 9 
    ans = sl.twoSum(arr, target)
    print(ans)
    

