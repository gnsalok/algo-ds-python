# Function to segment given into a space-separated
# sequence of one or more dictionary words
def wordBreak(dict, str, out=""):

	# if we have reached the end of the String,
	# print the output String
	if not str:
		print(out)
		return

	for i in range(1, len(str) + 1):
		# consider all prefixes of current String
		prefix = str[:i]
		

		# if the prefix is present in the dictionary, add prefix to the
		# output and recur for remaining String
		if prefix in dict:
			wordBreak(dict, str[i:], out + " " + prefix)


if __name__ == '__main__':

	# List of Strings to represent dictionary
	dict = [
		"self", "th", "is", "famous", "Word",
		"break", "b", "r", "e", "a", "k", "br",
		"bre", "brea", "ak", "problem"
	]

	# input String
	str = "Wordbreakproblem"

	wordBreak(dict, str)
