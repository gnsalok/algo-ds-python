'''

nums = [2,2,1] ; return 1
'''

def singleNumber(nums):
    res = 0 
    for n in nums:
        res = n ^ res
    return res

nums = [2,2,1]
print(singleNumber(nums))


