# Same solution
# Time: O(n^2), Space: O(n)

def longestPalindrome(s):
    resLen = 0 # length of palindromic substring
    resIdx = 0 # idx from where length count start ; it will be Left pointer

    for i in range(len(s)):

        # odd length
        l, r = i, i

        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                resIdx = l
                resLen = r - l + 1  
            l -= 1
            r += 1
        
        # even length 
        l, r = i, i + 1

        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                resIdx = l
                resLen = r - l + 1
            l -= 1
            r += 1

    return s[resIdx : resIdx + resLen]


str = "abaab"
print(longestPalindrome(str)) # result = 4