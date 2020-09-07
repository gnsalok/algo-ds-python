
'''
Problem :  Find all pair a,b,c and d of array such that a+b = c+d 
Solution : Using Hash Map, Time complexity is O(n**2), 
Author : Alok Tripathi

'''

# function to find a, b, c, d such that
# (a + b) = (c + d)


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
    arr = [3, 4, 7, 1, 2, 9, 8]
    n = len(arr)
    findPairs(arr, n)
