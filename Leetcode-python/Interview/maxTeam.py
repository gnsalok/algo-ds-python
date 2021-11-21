# Python 3 program for the above approach

# Function to find if T number of teams
# can be formed or not
def is_possible(teams, T, k):
	# Store the sum of array elements
	sum = 0

	# Traverse the array teams[]
	for i in range(len(teams)):
		sum += min(T, teams[i])

	# Required Condition
	return (sum >= (T * k))

# Function to find the maximum number
# of teams possible

def countOfTeams(teams_list, N, K):
	# Lower and Upper part of the range
	lb = 0
	ub = 1000000000

	# Perform the Binary Search
	while (lb <= ub):

		# Find the value of mid
		mid = lb + (ub - lb) // 2

		# Perform the Binary Search
		if (is_possible(teams_list, mid, K)):
			if (is_possible(teams_list, mid + 1, K)==False):
				return mid

			# Otherwise, update the
			# search range
			else:
				lb = mid + 1

		# Otherwise, update the
		# search range
		else:
			ub = mid - 1
	return 0

# Driver Code
if __name__ == '__main__':
	arr = [3, 4, 3, 1, 6, 5]
	K = 2
	N = len(arr)
	print(countOfTeams(arr, N, K))
	
	# This code is contributed by ipg2016107.
