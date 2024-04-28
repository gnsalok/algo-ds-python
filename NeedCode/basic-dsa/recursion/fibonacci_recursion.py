'''
TC : O (2 pow N)

To improve time complexity, we can use dict. to memoize the solution
check _dp solution for the same.

'''
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + (n-2)
    


#             f(0), f1, f2, f3 .... .
# Fib series : 0,1,1,2,3,5 
print(fib(3))  # expected output = 2

