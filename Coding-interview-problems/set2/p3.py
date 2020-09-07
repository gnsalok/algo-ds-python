'''
Problem : Find out middle index where sum of both ends is equal.
Code for: Sum of numbers preceeding the index is equal to sum of number succeeding the index.

Author : Alok Tripathi

'''

arr = [2, 4, 4, 5, 4, 1]

for i in range(len(arr)):
    if sum(arr[:i]) == sum(arr[i:]):
        print("Middle Index:", i-1)
