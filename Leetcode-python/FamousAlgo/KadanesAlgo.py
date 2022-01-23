'''
- Maximum sum subarray using Kadane's algorithm.
- It uses DP to keep track of maxEnding here, and maxSoFor 
'''
# Time O(N), Space O(1)


def kadanesAlgorithm(arr):
    maxEndingHere = arr[0]
    maxSoFor = arr[0]

    for i in range(1, len(arr)):
        num = arr[i]
        maxEndingHere = max(num, maxEndingHere + num)
        maxSoFor = max(maxSoFor, maxEndingHere)
        print(maxSoFor, end="")
    return maxSoFor


arr = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
print(kadanesAlgorithm(arr))
