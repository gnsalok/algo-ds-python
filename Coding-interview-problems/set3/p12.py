'''
@problem :Find all pairs (a, b) in an array such that a+b=c+d
@author : Alok Tripathi
'''


def findPairs(arr, n):

    # Create an empty hashmap to store mapping
    # from sum to pair indexes
    Hash = {}

    # Traverse through all possible pairs of arr[]
    for i in range(n - 1):
        for j in range(i + 1, n):
            sum = arr[i] + arr[j]
        # Sum already present in hash
            if sum in Hash.keys():
                # print previous pair and current
                prev = Hash.get(sum)
                print(str(prev) + " and (%d, %d)" % (arr[i], arr[j]))
                return True
            else:
                # sum is not in hash
                # store it and continue to next pair
                Hash[sum] = (arr[i], arr[j])
    return False


if __name__ == "__main__":
    print("Hello world")
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    findPairs(arr, n)
