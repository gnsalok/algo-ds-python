# from functools import lru_cache

# @lru_cache(maxsize = 1000)
# def fib(n):
#   if n < 2:
#     return n
#   else:
#     return fib(n-1) + fib(n-2)


# print(fib(10))
# print(fib.cache_info())



cache = {}

def fibo(n):
#lookup in dict if value is available or not
  if n in cache:
    return cache[n]
  elif n < 2:
    cache[n] = n
    return cache[n]
  else :
    cache[n] = fibo(n-1) + fibo(n-2)
    return cache[n]

if __name__ == "__main__":

    x = fibo(10)
    print(cache)
    print(x)