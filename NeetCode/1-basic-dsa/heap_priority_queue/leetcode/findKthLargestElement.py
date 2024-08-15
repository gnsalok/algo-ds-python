class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k # get kth index

        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p] # swap pivot with value at p pointer

            if p > k:   return quickSelect(l, p-1)
            elif p < k: return quickSelect(p+1, r)
            else:       return nums[p]

        return quickSelect(0, len(nums)-1)