'''
Find Max Subset Sum No Adjacent   || Its Rob House Problem.

TIME : O(N)
SPACE : O(N)

'''

def maxSubsetSumNoAdjacent(array):
	n = len(array)
	
	if(n == 0):
		return 0
	
	dp = [0] * n
	dp[0] = array[0]
	
	for i in range(1, n):
		if(i == 1):
			dp[i] = max(array[0], array[1])
		else:
			dp[i] = max(dp[i-1], dp[i-2] + array[i])
	return dp[-1]
		
 
arr = [75, 105, 120, 75, 90, 135]  # output 330 
ans = maxSubsetSumNoAdjacent(arr)
print(ans)
