def printN(n):

    if(n == 0):
        return 0

    print(n)
    return n + printN(n-1)
    



ans = printN(10)
print(ans)