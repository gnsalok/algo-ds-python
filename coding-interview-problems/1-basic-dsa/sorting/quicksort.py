'''
Quick Sort 

Time complexity

- If input is sorted, then tree/partition height will increase, which is worst case.
- In avg. TC is O(N log n)
- Worst Case : O(n^2)


SC : 
- Best and average Case : log N 
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
    left = s # pointer for left side to replace pivot in the end

    # Partition: elements smaller than pivot on left side
    for i in range(s, e):
        if arr[i] < pivot:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1

    # Swap pivot (arr[e]) with arr[left] position
    arr[e], arr[left]  = arr[left], arr[e]

    # Quick sort left side
    quickSort(arr, s, left - 1) # left - 1 because arr[left] is already in-place or in sorted order because we selected the pivot.

    # Quick sort right side
    quickSort(arr, left + 1, e)

    return arr
    
input = [3,2,4,1,6]
sortedArr = quickSort(input, 0, len(input)-1)
print(sortedArr)