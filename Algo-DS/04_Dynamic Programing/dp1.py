def memoizedadd80(n):
    cache = {}   #dict or hashmap 
 
    if n in cache:
        return n + 80
    else:
        print('Long time')
        cache[n] = n+80
        return cache[n]

print(memoizedadd80(6))
print(memoizedadd80(6))