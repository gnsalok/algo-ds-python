# https://leetcode.com/problems/valid-anagram/

'''
TC : O(Nlogn)
SC : O(S+T)

'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)