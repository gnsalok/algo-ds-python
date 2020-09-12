''' Fibonacci series using Recursion 
fn = fn-1 + fn+1
'''


def fib(n):
    if n >=3:
        return fib(n-1) + fib(n-2)
    else:
        return 1

def fib_rec(n, memo):
    print(n)
    if memo[n]:
        return memo[n]
    else:
        res = fib_rec(n-1, memo) + fib_rec(n-2, memo)
        memo[n] = res
        return res
    
if __name__ == '__main__':
   # print(fib(50))
    n = 10
    memo = [None]*(n+1)
    print(fib_rec(n, memo))

