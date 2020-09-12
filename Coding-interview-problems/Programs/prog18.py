"""
Maximum contiguous sub array
Given 
    1. a list of positive or negative integers
To a a subarray (contigious) whose sum is maximum
"""

def max_sum_subaarry(a):
  """ Kadane's algo """
  max_so_far = 0
  max_ending_here = 0
  n = len(a)
  start = 0
  end = 0
  s = 0

  for i in range(0, n):
    max_ending_here = max_ending_here + a[i]
    if max_ending_here < 0:
      max_ending_here = 0
      s = i + 1
    
    if max_ending_here > max_so_far:
      max_so_far = max_ending_here
      start = s 
      end = i

  
  return max_so_far, a[start:end+1]

if __name__ == '__main__':
  a = [-2, -3, 4, -1, -2, 1, 5, -3]
  print(max_sum_subaarry(a))