'''
1,2,3,4 .....
0,1,1,2,3,5,8,13.....

fib(n) = fib(n-1) + fin(n-2)  for n > 2
fib(7) == 33 (sum of)
'''

'''
For Recursive Solution
#Time Complexity : O(2**n) 
#Spcae Complexity : O(n) Why? Because we are using function call stack a lot. 

'''


# def fib(n):
#     if(n == 1):
#         return 0
#     if(n == 2):
#         return 1
#     return fib(n-1) + fib(n-2)



# Lets memoize it 
# TC : O(n)
# SP : O(1)
def fib(n):
    memoize={1:0, 2:1}

    if n in memoize:
        return memoize[n]
    else:
        memoize[n] =  fib(n-1) + fib(n-2)
    return memoize[n]

    
print(fib(5))
