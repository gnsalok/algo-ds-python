def loopAllPair(arr):
    for i in arr:
        for j in arr:
            print(arr[i - 1], arr[j - 1])


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    loopAllPair(arr)