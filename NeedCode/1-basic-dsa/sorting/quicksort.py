'''
Quick Sort 

Time complexity

- If input is sorted, then tree/partition height will increase, which is worst case. Then TC. O(N^2)
- In avg. TC is O(N log n)


SC : 
- AVG Case : log N 
- Worst : O(n)
'''

# Implementation of QuickSort
def quickSort(arr, s, e):
    # length of sub-array is <= 1 then arr is already sorted.
    if e - s + 1 <= 1:
        return arr

    pivot = arr[e]

    # left ptr is for swap the value at the index where pivot is greater the ith Index.
    # so that we can make sure value at left side of pivot is lesser and right side is greater.
    left = s # pointer for left side

    # Partition: elements smaller than pivot on left side
    for i in range(s, e):
        if arr[i] < pivot:
            tmp = arr[left]
            arr[left] = arr[i]
            arr[i] = tmp
            left += 1

    # Move pivot in-between left & right sides
    arr[e] = arr[left]
    arr[left] = pivot
    
    # Quick sort left side
    quickSort(arr, s, left - 1)

    # Quick sort right side
    quickSort(arr, left + 1, e)

    return arr
    
input = [3,2,4,1,6]
sortedArr = quickSort(input, 0, len(input)-1)
print(sortedArr)