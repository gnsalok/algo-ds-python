# class Solution(object):
#    def twoSum(self, nums, target):
#       """
#       :type nums: List[int]
#       :type target: int
#       :rtype: List[int]
#       """
#       required = {}
#       for i in range(len(nums)):
#          if target - nums[i] in required:
#             return [required[target - nums[i]],i]
#          else:
#             required[nums[i]]=i
# input_list = [2,8,12,15]
# ob1 = Solution()
# print(ob1.twoSum(input_list, 20))



# ll = [1,2,3,4,5]

# newll = []

# for i in range(len(ll)):
#     if i == 5:
#         newll[0] = i


class Stack:
    def __init__(self):
        print("Id of class -- self ", id(self))



st = Stack()
print("Id of object -- self ", id(st))




    

