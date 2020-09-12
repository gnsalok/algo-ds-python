"""
Longest common substring:
Given :
        - two different strings
Find the longest common substring in both the strings. 
A subsequence is a sequcence that is in order and have to be contigious
for example
      string 1  :  "geeksforgeeks"
      string 2  : "geeks"

    LCS : geeks
  
"""

def LCS(x, y):
  ''' LCS using dynamic Programing '''
  m = len(x)
  n = len(y)
  l = [[0 for k in range(n+1)] for l in range(m+1)] 
  print(l)

  result = 0

  for i in range(m+1):
    for j in range(n+1):
      if i ==0 or j==0:
        l[i][j] == 0
      elif x[i-1] == y[j-1]:
        l[i][j] = l[i-1][j-1] + 1
        result = max(result, l[i][j])
      else:
        l[i][j] = 0

  return result



if __name__ == '__main__':
  a = 'geeksforgeeks'
  b = 'geeks'
  print(LCS(a, b))