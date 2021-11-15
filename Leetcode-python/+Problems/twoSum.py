class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        ans = []
        for i in range(len(nums)):
            x = nums[i]
            y = target - x

            if y in map:
                ans.insert(0,i) 
                ans.insert(1,map[y]) 
                return ans # return once found 
            else:
                map[x] = i 
                print(map)
        
            

if __name__ == "__main__":
    sl = Solution()
    arr = [2,7,11,15]
    target = 9 
    print(sl.twoSum(arr, target))
    

