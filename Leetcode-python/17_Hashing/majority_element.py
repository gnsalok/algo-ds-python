from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        
        for num in nums:
            map[num] = map.get(num,0) + 1
            print(map)
             
        for num in nums:
            if(map[num] > len(nums)//2):
                return num


list = [3,2,3,2,3,2,2,3,3]
sl = Solution()
res = sl.majorityElement(list)
print(res)



'''
3:2 , 2:1
len(num) --> 9 // 2 = 4

Steps: 
1. Put elements count in the hashmap and increase number for occurances.
2. Any Count is greater than len//2 of array then return the number.
'''
        