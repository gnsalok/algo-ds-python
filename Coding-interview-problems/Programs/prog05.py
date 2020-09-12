"""
Given 
   - a list of integers  l 
   - an integer - s
Find all the pair of integers in the l that sum up to 's'. 
"""


def two_sum_1(l, s):
  """ find two sum """
  ht = {}
  res = []
  for i, v in enumerate(l):
    ht[v] = i

  for i in l:
    complement = s - i
    if complement in ht and (i, complement) not in res and (complement, i) not in res and complement != i:
      res.append((i, complement))

  print(res)


if __name__ == '__main__':
  l = [2, 3, 5, 4, 1, 0]
  s = 4
  two_sum_1(l, s)