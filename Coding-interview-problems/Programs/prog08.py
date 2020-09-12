"""
Remove dupliate elements in a sorted array.
Given : a sorted array of integers 
    
    Don't allocate space for another array (used slicing)
    Can we deallocate the memeory is list.
"""

def remove_dup(a):
  """ remove duplicates using extra array """
  res = []
  count = 0
  for i in range(0, len(a)-1):
    if a[i] != a[i+1]:
      res.append(a[i])
      count = count + 1
  
  res.append(a[len(a)-1])
  print('Total count of unique elements: {}'.format(count +1))

  return res


def remove_dup2(a):
  """ remove dup in sorted array without using another array """
  n = len(a)
  j = 0
  print("before removing -- ", a )
  for i in range(0, n-1):
    if a[i] != a[i+1]:
      a[j] = a[i]
      j = j+ 1
  
  a[j] = a[n-1]

  print("after removing -- ", a )

  return a[0: j+1]


if __name__ == '__main__':
  sorted_a = [1, 2, 2, 3, 3, 4, 5, 10, 11, 11]
  #res = remove_dup(sorted_a)
  res = remove_dup2(sorted_a)
  print(res)