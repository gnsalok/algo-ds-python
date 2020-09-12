""" 
Minimum size sub array
Given 
   1. A list of integers, a
   2. An integer, s
Find the minimum sub array (continuous array) where sum of items is >= s
"""
def min_sub_array_sum2(a, sum, n):
   ''' Nested for loops:
       complexity: O(n2)
   ''' 
   min_len = n + 1
   cur_sum = 0
   for i in range(0, n):
      cur_sum = a[i]

      if cur_sum > sum:                                                   
         return 1
      for j in range(i+1, n):
         cur_sum = cur_sum + a[j]
         if cur_sum > sum and (j - i +1) < min_len:
            min_len = j-i+1

   return min_len



def min_sub_array_sum(a, sum, n):
   ''' Minimum sub array sum 
      Complexity : O(n)
    '''
   curr_sum = 0
   start= 0
   end = 0
   min_len = n + 1

   while end < n:
      while curr_sum <= sum and end < n:
         curr_sum = curr_sum + a[end]
         end = end + 1
      while curr_sum > sum and start < n:
         if end - start < min_len:
            min_len = end -start
         curr_sum = curr_sum - a[start]
         start = start +1
   
   print("start - ", start)
   print("end - ", end)
   return min_len

if __name__ == '__main__':
   a = [1, 10, 3, 40, 18]
   sum = 50
   print(min_sub_array_sum(a, sum, len(a)))
   print(min_sub_array_sum2(a, sum, len(a)))