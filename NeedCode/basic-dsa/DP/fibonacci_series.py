

'''
1-D DP

- Memoization => TOP DOWN Dynamic Programming

'''
# Memoization 
def fib(n):
    mem = {}
    if n <= 1:
        return n
    if n in mem:
        return mem[n]
    mem[n] = fib(n-1) + fib(n-2)

    return mem[n]



'''
1-D DP

- Bottom-up Dynamic Programming
    - Start from 0 
'''


'''
Optimization : you can further optimize by using two pointer; as you just need two prev values.
'''
def fibDP(n):
    if n < 2:
        return n
    
    dp = n*[0]
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp)
    return dp[-1]


print(fibDP(5))


