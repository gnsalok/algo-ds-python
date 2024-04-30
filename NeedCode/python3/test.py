def printN(n):
    if n == 0:
        return 1
    printN(n-1)
    print(n)
    


printN(5)