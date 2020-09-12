''' Selection Sort '''


def selection_sort(arr):
    for fillslot in range(len(arr)-1, 0, -1):
        print('fillslot : ', fillslot)
        posofmax = 0
        for location in range(1, fillslot+1):
            if arr[location] > arr[posofmax]:
                posofmax = location
                print('curr max pos : ', posofmax)
                print('curr max item : ', arr[posofmax])

        arr[fillslot], arr[posofmax] = arr[posofmax], arr[fillslot]
        print('arr : ', arr)
        print('*' * 20)
    return arr


if __name__ == '__main__':
    arr = [4, 61, 3, 50, -1]
    print(selection_sort(arr))
