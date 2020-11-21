
def reverseArr(arr):
    list = []
    for i in range(len(arr)-1, -1, -1):
        list.append(arr[i])
    return list


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(reverseArr(arr))
