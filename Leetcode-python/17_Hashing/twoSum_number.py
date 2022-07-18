'''
Time : O(n)
Space : O(n)
'''


class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for i in range(0, len(nums)):
            number = nums[i]
            goal = target - number
            if(goal in seen):
                return [goal, number]
            else:
                seen[number] = True
        return -1

     
            
if __name__ == "__main__":
    sl = Solution()
    arr = [2,7,11,15]
    target = 9 
    ans = sl.twoSum(arr, target)  # [2,7]
    print(ans)

