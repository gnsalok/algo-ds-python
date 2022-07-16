'''
Index : 0 1 2 3 4
Input : 1 2 3 4 5
Output: 5 4 3 2 1 

TC = O(N)
SP = O(1)
'''


'''
-- More pythonic way

output = []
for i in reversed(range(len(arr))):
    output.append(arr[i])
return output

'''

def reverseArr(arr):
    st = 0
    end = len(arr) - 1

    while(st <= end):
        swap(st, end, arr)
        st += 1
        end -= 1
    return arr

def swap(n1, n2, arr):
    arr[n1], arr[n2] = arr[n2], arr[n1]

arr = [1,2,3,4,5]
ans = reverseArr(arr)
print(ans)
        