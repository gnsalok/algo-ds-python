"""
Problem : Find out the missing number 
Author : Alok Tripathi

"""


def getMissingNo(arr):
    n = len(arr)
    total = (n + 1) * (n + 2) / 2  # Sum of (N+1) * (N+2) natural number [n is length of arr]
    sum_of_arr = sum(arr)
    return int(total - sum_of_arr)  # sum of n... natural no. - sum of array


if __name__ == "__main__":

    arr = [1, 2, 3, 5]
    miss = getMissingNo(arr)
    print(miss)
