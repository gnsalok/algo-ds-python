'''
Input : n = 5 and array[] = {1, 2, 3, 4 ,3}
Output: 3
'''


''''
This will work only when given arr in 1..n  and you can mutate the array.
'''
'''
def findDup(arr, n):
    for num in arr:
        absValue = abs(num)  # take abs value
        if(arr[absValue - 1] < 0): # sub -1 from the actual value 
            return absValue #if -ve the its first duplicate 
        arr[absValue - 1] *= -1  # otherwise mark that value as negative to check other iteration 
'''

# Will work for every case
def findDup(arr, n):
    seen = set()
    for n in arr:
        if(n in seen):
            return n
        else:
            seen.add()
    

arr = [1, 2, 2, 3, 4 ,3]
size = len(arr)
print(findDup(arr, size))



