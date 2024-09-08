if __name__ == "__main__":

    arr = [64, 34, 25, 12, 22, 11, 90]  # sorted array

    n = len(arr)
    for i in range(n):
        # Last i elements are already in place, so we don't need to check them
        # In each iteration last element of the arr will be placed in the correct order.
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)

