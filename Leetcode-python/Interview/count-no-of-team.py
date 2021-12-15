


def numTeam(arr):
    n = len(arr)
    res = 0

    for i in range(0,n):
        ll , ls = 0, 0
        rl , rs = 0, 0
        for j in range(0,i):
            if(arr[j] > arr[i]):
                ll += 1
            if(arr[j] < arr[i]):
                ls += 1
        for j in range(i+1, n):
            if(arr[j]>arr[i]):
                rl += 1
            if(arr[j] < arr[i]):
                rs += 1
        res += (ls * rl) + (rs * ll)
    return res



if __name__ == "__main__":
    rating = [2,5,3,4,1]
    result = numTeam(rating)
    print(result)
    