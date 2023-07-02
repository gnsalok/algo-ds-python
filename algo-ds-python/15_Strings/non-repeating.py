
def firstNonRepeatingCharacter(string):
	map = {}
	for s in string:
		map[s] = map.get(s,0) + 1
	
	print(map) #logging
		
	for i, s in enumerate(string):
		if(map[s] == 1):
			return s
	return None



string = "abcdcaf"
ans = firstNonRepeatingCharacter(string)
print(ans)