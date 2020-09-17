'''
Problem : Find all the palindromic string in the given Input
Suppose we have a string; we have to count how many palindromic substrings present in this string. 
The substrings with different start indices or end indices are counted as different substrings even 
they consist of same characters. So if the input is like “aaa”, then the 
output will be 6 as there are six palindromic substrings like “a”, “a”, “a”, “aa”, “aa”, “aaa”

Malyalam --
'''
class Solution:
   def countSubstrings(self, s):
      counter = 0
      for i in range(len(s)):
         for j in range(i+1,len(s)+1):
            temp = s[i:j]
            if temp == temp[::-1]:
                counter+=1
      return counter


ob1 = Solution()
print(ob1.countSubstrings("malyalam"))