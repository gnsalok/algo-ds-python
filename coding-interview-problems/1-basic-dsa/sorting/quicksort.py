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
    # you can write s >= e as base case here too.
    if e - s + 1 <= 1:
        return arr

    pivot = arr[e]

    # Partition: elements small than pivot on left side
    left = s # pointer for left side to replace pivot later

    # Partition: elements smaller than pivot on left side
    for i in range(s, e):
        if arr[i] < pivot:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1

    # Move the pivot in-between left and right sides
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