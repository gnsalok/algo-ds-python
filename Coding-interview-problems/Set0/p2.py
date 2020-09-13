def fibonacci(size):
    a = 0
    b = 1
    print(a)
    print(b)

    for i in range(size - 1):
        c = a + b
        a = b
        b = c
        print(c)