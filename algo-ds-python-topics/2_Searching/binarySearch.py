'''
    Binary Seach works on only sorted collection.
    Time : O(log n)
    Space : O(1)
'''

def binarySearch(arr, x):
    lo, hi = 0, len(arr)

    while lo < hi:
        mid = lo + (hi - lo) // 2 # in python (low + hi) // 2 will also work. Problem is in Java and C++
        if arr[mid] == x:
            return mid
        if arr[mid] > x:
            hi = mid
        else:
            lo = mid + 1
    return -1

nums = [-1, 0, 3, 5, 9, 12]
target = 9

print(binarySearch(nums, target))
