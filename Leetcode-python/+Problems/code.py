
def pairSum(arr, sum):
    map = {}
    result = []

    for i in range(len(arr)):
        x = arr[i]
        y = sum - arr[i]

        if y in map:
            result.insert(0,arr[i])
            result.insert(1,y)
        else:
            map.append(arr[i])
    return result


    '''
    x=2
    y= 9 - 2 = 7


    map = {2:2, }
    
    '''









if __name__ == "__main__":
    arr = [2,7,11,15]
    sum = 9 

    res = pairSum(arr, sum)
    print(res)
    