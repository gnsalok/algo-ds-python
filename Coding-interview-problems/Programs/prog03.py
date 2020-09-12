''' programs on fibonacci series '''

def fibonacci(size):
    a = 0
    b = 1
    print(a)
    print(b)

    for i in range(size-1):
        c = a + b
        a = b
        b = c
        print(c)

def fibonacci_nth(n):
    a = 0
    b = 1
    if n < 0:
        print('invalid')
        return
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b 
            a = b
            b = c
    
    print(c)  # returning b not c

def fibonacci_nth_rec(n):
    if n < 0:
        print('invalid number')
    if n == 0:
        return 0
    if n == 1 :
        return 1
    
    return fibonacci_nth_rec(n-2) + fibonacci_nth_rec(n-1)

fibstore = [0, 1]
def fibonacci_memo(n):
    if n < 0:
        print('invalid')
    if n <= len(fibstore):
        return fibstore[n-1]
    else:
        fib = fibonacci_memo(n-2) + fibonacci_memo(n-1)
        fibstore.append(fib)
        return fib


fibdict = {0: 0, 1: 1}

def fibonacci_memo_2(n):
    if n < 0:
        print('invalid')
        return
    if n in fibdict.keys():
        print('fib already in dict')
        return fibdict[n]
    else:
        fib = fibonacci_memo_2(n-2) + fibonacci_memo_2(n-1)
        fibdict[n] = fib
        return fib
    


if __name__ == '__main__':
    fibonacci(8)
    print('*' * 20)
    fibonacci_nth(9)
    print('*' * 20)
    print(fibonacci_nth_rec(9))
    # print(fibonacci_memo(10))
    #print(fibonacci_memo_2(100))