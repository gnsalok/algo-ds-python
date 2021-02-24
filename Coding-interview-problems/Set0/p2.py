# def fibonacci(size):
#     a = 0
#     b = 1
#     print(a)
#     print(b)

#     for i in range(size - 1):
#         c = a + b
#         a = b
#         b = c
#         print(c)

'''
Fibonacci number -- Using various techniques 

'''


# Using Recursion
# Function for nth Fibonacci number

def Fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)


# Driver Program
print(Fibonacci(9))


# def fib(n):
#     if n >=3:
#         return fib(n-1) + fib(n-2)
#     else:
#         return 1


# Dynamic Programming - Memoization
