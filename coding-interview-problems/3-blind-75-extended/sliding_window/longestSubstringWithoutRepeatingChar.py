'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/

'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        result = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1

            charSet.add(s[right])
            result = max(result, right - left + 1)

        return result

s = "abcabcbb"
sl = Solution()
print(sl.lengthOfLongestSubstring(s))