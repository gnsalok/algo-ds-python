def sortBinary(arr):
    count = 0
    for n in arr:
        if(n == 0):
            arr[count] = 0
            count += 1
    
    for i in range(count, len(arr)):
        arr[i] = 1



arr = [1,0,0,0,1,0,0,1]
sortBinary(arr)
print(arr)