


# Input                 Output
# 0 0 1 0 0 1 0 1 -->   0 0 0 0 0 1 1


def sort_binary(arr, n):
    c = -1 # count no. of ele which are lesser than pivot 
    sb0 = []
    sb1 = []
    for i in range(n):
        if arr[i] < 1:
            c = c + 1
            arr[c], arr[i] = arr[i], arr[c]
            sb0.append(arr[c])
            sb1.append(arr[i])

    return sb0+sb1
        
        

if __name__ == '__main__':
    listBinary = [0,0,1,0,0,1,0,1]
    ll = len(listBinary)
    sb  = sort_binary(listBinary, ll)
    print(sb)

    # for i in range(ll):
    #     print(listBinary[i])
    

