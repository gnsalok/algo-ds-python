'''
    Binary Seach works on only sorted collection.
    Time : O(log n)
    Space : O(1)
'''


def binarySearch(arr, target):
    left = 0
    right = len(arr)-1 
    

    while(left <= right):
        mid = (left + right) // 2 

        if(arr[mid] == target):
            return mid
        #if target is greater than mid then set left to min+1
        elif(arr[mid]< target):
            left = mid+1
        else:
            right = mid - 1
    return -1 



if __name__ == "__main__":
    arr = [10,11,12,13,14,15]
    target = 15
    result = binarySearch(arr, target) #5

    if result != -1:
        print("Result is present at index %d"% result)
    else:
        print("Element is not present in the list.")