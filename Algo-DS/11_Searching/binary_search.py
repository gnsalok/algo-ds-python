''' binary search
Note: Binary search always works on Sorted array.
'''


def binary_search(arr, elem):
    start = 0
    end = len(arr)-1

    found = False

    while start <= end and not found:
        mid = (start+end)//2
        if elem == arr[mid]:
            found = True
        elif elem < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return found


def r_binary_search(arr, start, end, item):
    if start < end:
        mid = (start+end)//2
        if item == arr[mid]:
            return True
        elif item < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
        return r_binary_search(arr, start, end, item)
    else:
        return False


def r_binary_search2(arr, item):
    if len(arr) == 0:
        return False


    mid = len(arr)//2

    if item == arr[mid]:
        return True
    elif item < arr[mid]:
        return r_binary_search2(arr[:mid], item)
    else:
        return r_binary_search2(arr[mid+1:], item)


if __name__ == '__main__':
    arr = [3, 4, 5, 6, 7]
    print(binary_search(arr, 5))
    print(r_binary_search(arr, 0, len(arr)-1, 6))
    print(r_binary_search2(arr, 9))