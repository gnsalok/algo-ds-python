"""
To sum in a sorted array

Given:
   l: a list of sorted arrays
   s: integer
find unique pair of items in the list l where sum is 's'

Problems:
 1. Not working when there is a duplicate item is the list - [2, 3, 5, 4, 2, 1, 0]

"""

def two_sum_sorted_array(l, sum):
  l.sort()
  print(l)
  a = 0
  z = len(l)-1

  while a < z:
    sum = l[a] + l[z]
    if sum == s:
      print(l[a], l[z])
      a = a + 1
      z = z - 1
    elif sum > s:
      z = z-1
    else:
      a = a + 1

if __name__ == '__main__':
  l = [2, 3, 5, 4, 2, 1, 0]
  s = 4
  two_sum_sorted_array(l, s)