'''
Binary Search 

IMP : Only works on sorted arr input

TC. : O(logN)

'''

def binarySearch(arr, target):

    left, right = 0, len(arr)-1

    while left <= right:
        
        mid = (left + right)//2

        if target < arr[mid]:
            right = mid - 1
        elif target > arr[mid]:
            left = mid + 1
        else:
            return mid
    return -1 


arr = [1,2,3,4,5,6,7,8]
target = 5
result = binarySearch(arr, target)
print(result) # output: 4