def twoSum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        comp = target - n
        if comp in seen:
            print("Got indexes",seen)
            return [seen[comp], i]
        else:
            seen[n] = i
            print("upating dict", seen)
            

list = [2,7,11,15]
target = 9

res = twoSum(list, target)
print(res)