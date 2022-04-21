class Solution:
   def groupAnagrams(self, strs):
      result = {}
      for s in strs:
         # sorted returns list of items, need to convert into str
         x = "".join(sorted(s))
         print(x)
         if x in result:
            result[x].append(s)
         else:
            result[x] = [s]
      return list(result.values())
ob1 = Solution()

print(ob1.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))