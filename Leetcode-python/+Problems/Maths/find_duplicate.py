'''
Input : n = 5 and array[] = {1, 2, 3, 4 ,3}
Output: 3
'''


def findDup(arr, n):

    for num in arr:
        absValue = abs(num)  # take abs value
        if(arr[absValue - 1] < 0): # sub -1 from the actual value 
            return absValue #if -ve the its first duplicate 
        arr[absValue - 1] *= -1  # otherwise mark that value as negative to check other iteration 
  
    

arr = [1, 2, 2, 3, 4 ,3]
size = len(arr)
print(findDup(arr, size))



