

# 1st Func
# def isPalindrome(string):
# 	reverseString = ""
# 	for i in reversed(range(len(string))):
# 		reverseString += string[i]
# 	return string == reverseString
		

# 2nd Func
def isPalindrome(string):
	reversedChar = []
	for i in reversed(range(len(string))):
		reversedChar.append(string[i])
	return string == "".join(reversedChar)
   
# TODO : Use 2 Pointer Approach one at left and second at right 

# str = "abcdcba"
# print(isPalindrome(str))




