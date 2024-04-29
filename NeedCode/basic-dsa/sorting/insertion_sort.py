'''

Insertion Sort

TC : 
- O(n2) - worst case 
- O(n)linear - best case

SC:
O(1)
'''


def insertionSort(arr):
    # traverse from 1 to len(arr)
    for i in range(1, len(arr)):
        # i to keep track to arr index 
        # j is to track left neighbour 
        j = i-1

        while(j>=0 and arr[j+1] < arr[j]):
            tmp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = tmp
            j -= 1
    return arr


input = [2,3,4,1,6]
op = insertionSort(input)
print(op)