"""
Longest common subsequence:
Given :
        - two different strings
Find the longest common subsequence in both the strings. 
A subsequence is a sequcence that is in order and may not be contigious .
for example
      string 1  :  "longest"
      string 2  : "stone"

    LCS : one
  
"""
def LCS2(a, b):
  ''' LCS using Dynamic programing'''
  x = len(a)
  y = len(b)

  l = [[0 for k in range(y+1)] for l in range(x+1)]
  print(l)

  for i in range(x+1):
    for j in range(y+1):
      if i == 0 or j == 0:
        l[i][j] = 0
      elif a[i-1] == b[j-1]:
        l[i][j] = 1 + l[i-1][j-1]
      else:
        l[i][j] = max(l[i-1][j], l[i][j-1])

  return l[x][y]

def LCS1(a, b, i, j):
  """ LCS recursion """
  if i >= len(a) or j >= len(b):
    return 0
  elif a[i] == b[j]:
    return 1 + LCS1(a, b, i+1, j+1)
  else:
    return max(LCS1(a, b, i+1, j), LCS1(a, b, i, j+1))


if __name__ == '__main__':
  a = 'bd'
  b = 'abcd'
  print(LCS1(a, b, 0, 0))
  print(LCS2(a, b))
