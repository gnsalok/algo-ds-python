
def twoSum( nums, target):
    d = {}
    for i, n in enumerate(nums):
        m = target - n
        if m in d:
            print("final return",d)
            return [d[m], i]
        else:
           
            d[n] = i
            print("upating ", d)
            

            




list = [2,7,11,15]
target = 9

res = twoSum(list, target)
print(res)