

'''
As we are using dict to store the calculation in two path recursion, so we avoid calculating same 
value again and again.

Time Complexity for this DP solution in Linear. 

O(N)


'''
def fib(n):
    if n <= 1:
        return n
    memoize={1:1, 2:1}
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = fib(n-1) + fib(n-2)
    return memoize[n]

# Fib series : 0,1,1,2,3,5 
print(fib(3))  # expected output = 2

