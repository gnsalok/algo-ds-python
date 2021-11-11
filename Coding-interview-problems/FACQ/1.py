# A Python program to sort a
# binary array
# Pivet is 0 here, solving by Quicksort

def sortBinaryArray(arr, n):
    i = -1  # value less than pivot

    for j in range(n):
        # if i th ele is less than pivot, then increment i and swap the value of array.
        if arr[j] < 1:
            #increment i-th element
            i = i + 1
            arr[j], arr[i] = arr[i], arr[j]
        


if __name__ == '__main__':
    # Driver program
    a = [1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1,
         1, 1, 0, 0, 1, 1, 0, 1, 0, 0]
    n = len(a)

    sortBinaryArray(a, n)

    for i in range(n):
        print(a[i])

