def fib(n):
    a=0
    b=1
    if n < 0:
        return "Invalid"
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
    return c


if __name__ == '__main__':
    result = fib(6)
    print(result)