'''
Counting Sorting 
Time : O(N)
Space : O(1)
'''
def sortBinary(arr):
    count = 0
    for num in arr:
        if(num == 0):
            arr[count] = num
            count += 1

    for c in range(count, len(arr)):
        arr[c] = 1
        

# You can sort using asc and desc both 
arr = [1,0,1,0,0,0,1,1]
sortBinary(arr)
print(arr)