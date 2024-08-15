'''
# Check if array contains a pair of duplicate values,
# where the two duplicates are no farther than k positions from 
'''

from typing import List

'''
TC : O(n)
'''
def containsDuplicate(arr: List, k: int) -> bool:

    # always maintain k values in window
    # remove from left and insert at right
    window = set()
    L = 0

    for R in range(len(arr)):
        if R - L + 1 > k:
            window.remove(arr[L])
            L += 1
        if arr[R] in window:
            return True
        window.add(arr[R])
    return False

arr = [1,1]
k = 2
print(containsDuplicate(arr, k))