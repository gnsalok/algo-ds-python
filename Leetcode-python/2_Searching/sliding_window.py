'''
Sliding Window is optimization technique.

Time : O(N)
Space : O(1)
'''

def maxSum(arr, n, k):
    window_sum = sum(arr[i] for i in range(k))
    max_sum = window_sum

    for i in range(0, n-k):
        window_sum = window_sum - arr[i] + arr[i+k]
        max_sum = max(max_sum, window_sum)

    return max_sum


if __name__ == "__main__":
    arr = [80,-50, 90, 100]
    k = 2 # size of window 
    size = len(arr)

    result = maxSum(arr, size, k)
    print(result)