class PrefixSum:

    def __init__(self, nums):
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)
        
    def rangeSum(self, left, right):
        preRight = self.prefix[right]
        if left-1 >= 0:
            preLeft = self.prefix[left - 1] 
        else:
            return 0
        return (preRight - preLeft)


arr = [2,-1,3,-3,4]
ps = PrefixSum(arr)
print(ps.rangeSum(1,3))