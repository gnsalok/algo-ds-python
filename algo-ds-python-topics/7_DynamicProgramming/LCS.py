'''
TC : O(NM) = space.
'''

def longestCommonSubsequence(str1, str2):
    lcs = [[[] for x in range(len(str1)+1)]
            for y in range(len(str2)+1)]
    
    # print(lcs)

    for i in range(1, len(str2)+1):
        for j in range(1, len(str1)+1):
            if (str2[i-1] == str1[j-1]):
                lcs[i][j] = lcs[i-1][j-1] + [str2[i-1]]
                print(lcs[i][j], "->", i-1, j-1)
            else:
                # immidiate top and left max compare based on key
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1], key = len)
    # last row and last col
    return lcs[-1][-1]

str1 = "ZXVVYZW"
str2 = "XKYKZPW"

result = longestCommonSubsequence(str1, str2) # result -> XYZW
print(result)
