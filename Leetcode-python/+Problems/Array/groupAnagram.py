class Solution:
   def groupAnagrams(self, strs):
      result = {}
      for i in strs:
         # sorted returns list of items, need to convert into str
         x = "".join(sorted(i))
         print(x)
         if x in result:
            result[x].append(i)
         else:
            result[x] = [i]
      return list(result.values())
ob1 = Solution()

print(ob1.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))