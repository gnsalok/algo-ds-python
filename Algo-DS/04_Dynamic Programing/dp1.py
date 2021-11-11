def memoizedadd80():
  cache = {}

  def memoized(n):
	  if n in cache:
	    return n + 80
	  else:
	    print('Long time')
	    cache[n] = n+80
	    return cache[n]
  return memoized

memo = memoizedadd80()
print(memo(7))
print(memo(7))



'''
Not working code -- Test it laster

def memoizedadd80(n):
  if n in cache:
    return n + 80
  else:
    print('Long time')
    cache[n] = n+80
    return cache[n]

print(memoizedadd80(6))
print(memoizedadd80(6))

'''