'''

1,2,3,4 .....
0,1,1,2,3,5,8,13.....

fib(n) = fib(n-1) + fin(n-2)  for n > 2

fib(7) == 33 (sum of)
'''

def fib(n):
    if(n <= 1):
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(5)) # ans -> 5


   
    


