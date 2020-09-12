''' meger sort part 2'''


def merge_sort(arr):
    n = len(arr)
    if n < 2:
        return
    mid = n/2
    l1 = []
    l2 = []

    for i in range(0, mid-1):
        l1[i] = arr[i]

    for j in range(mid, n-1):
        l2[j] = arr[j]


    merge_sort(l1)
    merge_sort(l2)
