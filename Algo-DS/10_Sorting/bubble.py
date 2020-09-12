''' Bubble Sort '''


def bubble_sort(arr):
    for n in range(len(arr)-1, 0, -1):
        print('loops: ', n)
        for k in range(n):
            print('bubble: ', k)
            if arr[k] < arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]
        print('arr: ', arr)

    return arr

if __name__ == '__main__':
    arr = [10, 9, 33, 0, -1, 5]
    print(bubble_sort(arr))
