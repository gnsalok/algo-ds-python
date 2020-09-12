''' Quick Sort implementation '''


def quick_sort(arr, start, end):
    if start < end:

        pivot = partition(arr, start, end)
        print(arr)

        quick_sort(arr, start, pivot-1)
        quick_sort(arr, pivot+1, end)


def partition(arr, start, end):
    p_index = start
    pivot = arr[end]

    for i in range(start, end):
        if arr[i] < pivot:
            arr[i], arr[p_index] = arr[p_index], arr[i]
            p_index += 1

    arr[p_index], arr[end] = arr[end], arr[p_index]
    return p_index


if __name__ == '__main__':
    arr = [6, 4, 5, 0, 20, 1]
    print('--Before Partition--')
    print(arr)
    quick_sort(arr, 0, len(arr)-1)
    print('--after partition--')
    print(arr)