'''
# palindromic permutations alphabetically 
# refer solution p9.py for this problem

'''

# import library 
import numpy as np 

MAX_CHAR = 26

# Function to count frequency of each in the 
# string. freq[0] for 'a', ...., freq[25] for 'z' 
def countFreq(str, freq, n) : 
	for i in range(0, n) : 
		freq[ord(str[i]) - ord('a')] += 1


# Cases to check whether a palindromic 
# string can be formed or not 
def canMakePalindrome(freq, n) : 
	
	# count_odd to count no of 
	# s with odd frequency 
	count_odd = 0
	for i in range(0, MAX_CHAR) : 
		
		if (freq[i] % 2 != 0): 
			count_odd += 1

	# For even length string 
	# no odd freq character 
	if (n % 2 == 0): 
		if (count_odd > 0): 
			return False
		else: 
			return True
	

	# For odd length string 
	# one odd freq character 
	if (count_odd != 1): 
		return False

	return True


# Function to find odd freq and reducing 
# its freq by 1, returns garbage 
# value if odd freq is not present 
def findOddAndRemoveItsFreq(freq) : 
	
	odd_char = 0
	
	for i in range(0, MAX_CHAR) : 
		if (freq[i] % 2 != 0): 
			freq[i] = freq[i] - 1
			odd_char = (chr)(i + ord('a')) 
			break
			
	return odd_char 


# To find lexicographically first 
# palindromic string. 
def findPalindromicString(str, n) : 
	
	freq = np.zeros(26, dtype = np.int) 
	countFreq(str, freq, n) 

	# Check whether a palindromic string 
	# can be formed or not with the 
	# characters of 'str' 
	if (not(canMakePalindrome(freq, n))): 
		# cannot be formed 
		return False

	# Assigning odd freq character if 
	# present else some garbage value 
	odd_char = findOddAndRemoveItsFreq(freq) 

	# indexes to store acters from 
	# the front and end 
	front_index = 0; rear_index = n - 1

	# Traverse acters in alphabetical order 
	for i in range(0, MAX_CHAR) : 
		if (freq[i] != 0) : 
			ch = (chr)(i + ord('a')) 

			# Store 'ch' to half its frequency times 
			# from the front and rear end. Note that 
			# odd character is removed by 
			# findOddAndRemoveItsFreq() 
			
			for j in range(1, int(freq[i]/2) + 1): 
				str[front_index] = ch 
				front_index += 1
				
				str[rear_index] = ch 
				rear_index -= 1
			
		
	# if True then odd frequency exists 
	# store it to its corresponding index 
	if (front_index == rear_index): 
		str[front_index] = odd_char 

	# palindromic string can be formed 
	return True


# Function to reverse the acters in the 
# range i to j in 'str' 
def reverse( str, i, j): 
	
	while (i < j): 
		str[i], str[j] = str[j], str[i] 
		i += 1
		j -= 1
	


# Function to find next higher palindromic 
# string using the same set of acters 
def nextPalin(str, n) : 
	
	# If length of 'str' is less than '3' 
	# then no higher palindromic string 
	# can be formed 
	if (n <= 3): 
		return False

	# Find the index of last acter 
	# in the 1st half of 'str' 
	mid = int (n / 2) - 1
	

	# Start from the (mid-1)th acter and 
	# find the first acter that is 
	# alphabetically smaller than the 
	# acter next to it 
	i = mid -1
	while(i >= 0) : 
		if (str[i] < str[i + 1]): 
			break
		i -= 1

	# If no such character is found, then 
	# all characters are in descending order 
	# (alphabetcally) which means there cannot 
	# be a higher palindromic string with same 
	# set of characters 
	if (i < 0): 
		return False

	# Find the alphabetically smallest character 
	# on right side of ith character which is 
	# greater than str[i] up to index 'mid' 
	smallest = i + 1; 
	for j in range(i + 2, mid + 1): 
		if (str[j] > str[i] and str[j] < str[smallest]): 
			smallest = j 

	# Swap str[i] with str[smallest] 
	str[i], str[smallest] = str[smallest], str[i] 

	# As the string is a palindrome, the same 
	# swap of characters should be performed 
	# in the 2nd half of 'str' 
	str[n - i - 1], str[n - smallest - 1] = str[n - smallest - 1], str[n - i - 1] 

	# Reverse characters in the range (i+1) to mid 
	reverse(str, i + 1, mid) 

	# If n is even, then reverse characters in the 
	# range mid+1 to n-i-2 
	if (n % 2 == 0): 
		reverse(str, mid + 1, n - i - 2) 

	# else if n is odd, then reverse acters 
	# in the range mid+2 to n-i-2 
	else: 
		reverse(str, mid + 2, n - i - 2) 

	# Next alphabetically higher palindromic 
	# string can be formed 
	return True


# Function to print all the palindromic 
# permutations alphabetically 
def printAllPalinPermutations(str, n) : 
	
	# Check if lexicographically first 
	# palindromic string can be formed 
	# or not using the acters of 'str' 
	if (not(findPalindromicString(str, n))): 
		# cannot be formed 
		print ("-1") 
		return
	
	# Converting list into string 
	print ( "".join(str)) 

	# print all palindromic permutations 
	while (nextPalin(str, n)): 
		
		# converting list into string 
		print ("".join(str)) 
		

# Driver Code 
str= "malayalam"
n = len(str) 

# Convertnig string into list so that 
# replacement of characters would be easy 
str = list(str) 

printAllPalinPermutations(str, n) 


# This article is contributed by 'saloni1297' 
