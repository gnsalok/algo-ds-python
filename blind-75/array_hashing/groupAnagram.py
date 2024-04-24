# https://leetcode.com/problems/group-anagrams/description/

'''
TC : O(NlogN)
SC : O(N)

'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedAnagram = {}

        for s in strs:
            sortedStr = "".join(sorted(s))
            if sortedStr in groupedAnagram:
                groupedAnagram[sortedStr].append(s)
            else:
                groupedAnagram[sortedStr] = [s]
                
        return list(groupedAnagram.values())
            
   
ob1 = Solution()
print(ob1.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))