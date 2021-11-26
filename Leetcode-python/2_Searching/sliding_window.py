'''
Sliding Window is optimization technique.

Time : O(N)
Space : O(1
'''

def maxSum(arr, n, k):   
    # Array size is less than window size
    if n <= k:
        print("Invalid operation")
        return -1

    window_sum = sum(arr[i] for i in range(k)) 
    max_sum = window_sum

    for i in range(0, n-k):
        #print("window sum ",window_sum)  # log to make sure of the sum
        window_sum = window_sum - arr[i] + arr[i+k]
        max_sum = max(max_sum, window_sum)
    return max_sum


if __name__ == "__main__":
    arr = [80,-50, 90, 100]
    k = 2 # window size
    size = len(arr)

    result = maxSum(arr, size, k)
    print(result)