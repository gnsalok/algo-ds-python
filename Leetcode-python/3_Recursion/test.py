def printN(n):
    if(n == 0):
        return 
    # 9, 8, 7 ...... 1
    print(n)
    printN(n-1)
    




printN(10)