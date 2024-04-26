# https://leetcode.com/problems/group-anagrams/description/

'''
TC : O(NlogN)
SC : O(N)


Solution :
1. Sort the char and convert in to string 
2. Make sorted string as key in map.
3. Check if key (sorted) is preset in dict,
4. If Yes, then append original str. 
else, put value at the sorted key in the map.

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