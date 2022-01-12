





arr = [1,2,3]




for i in range(len(arr)):
    newArr = arr[:i] + arr[i+1:]
    print(newArr)
        