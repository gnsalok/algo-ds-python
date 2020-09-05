"""
Problem : Find out the missing number 
Author : Alok Tripathi

"""


def getMissingNo(arr):
    n = len(arr)
    total = (n + 1)*(n + 2)/2
    sum_of_arr = sum(arr)
    return int(total - sum_of_arr)


if __name__ == "__main__":

    arr = [1, 2, 3, 5]
    miss = getMissingNo(arr)
    print(miss)
