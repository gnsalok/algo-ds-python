

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

def isPalindrome(string):
	left = 0
	right = len(string) - 1
	
	while(left < right):
		if(string[left] != string[right]):
			return False 
		left += 1
		right -= 1
		
	return True
		
		

# str = "abcdcba"
# print(isPalindrome(str))




