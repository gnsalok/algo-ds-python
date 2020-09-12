''' Merge sort algo '''


def merge(arr, start, mid, last):
    print(start)
    n1 = mid-start+1
    n2 = last-mid

    l1 = []
    l2 = []

    for i in range(0, n1):
        l1[i] = arr[start+i]

    for j in range(0, n2):
        l2[j] = arr[mid+1+j]

    # merging tem arrays back into main array arr[start.. end]
    i = 0
    j = 0
    k = start

    while i < n1 and j < n2:
        if l1[i] < l2[j]:
            arr[k] = l1[i]
            i += 1
            k += 1
        if l2[j] > l1[i]:
            arr[k] = l2[j]
            j += 1
            k += 1

    while i < n1:
        arr[k] = arr[i]
        k += 1
        i += 1

    while j < n2:
        arr[k] = arr[j]
        k += 1
        j += 1


def merge_sort(arr, start, end):
    if start < end:
        mid = int((start+(end-1))/2)
        print(mid)

        # sort first and second halves
        merge_sort(arr, start, mid)
        merge_sort(arr, mid+1, end)


        #merge
        merge(arr, start, mid, end)


if __name__ == '__main__':
    arr = [6, 4, 5, 0, 20, 1]
    print('--Before Sorting--')
    print(arr)
    merge_sort(arr, 0, len(arr)-1)
    print('--After Sorting--')
    print(arr)
