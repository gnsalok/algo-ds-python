
def fact(n):
    if(n == 1):
        return 1
    
    print(n)
    
    return nfact(n-1)




ans = fact(5)
print(ans)