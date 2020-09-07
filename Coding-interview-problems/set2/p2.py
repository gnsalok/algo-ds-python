'''
Problem :  Find out duplicate number between 1 to N numbers.
 - Find array sum
 - Subtract sum of First (n-1) natural numbers from it to find the result.

 Author : Alok Tripathi

'''
# Method to find duplicate in array


def findDuplicate(arr, n):
    return sum(arr) - (((n - 1) * n) // 2)


# Driver method
if __name__ == "__main__":

    arr = [1, 2, 3, 3, 4]
    n = len(arr)
    print(findDuplicate(arr, n))
