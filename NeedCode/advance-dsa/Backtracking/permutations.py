'''
https://leetcode.com/problems/permutations/

The time complexity of the provided backtracking solution to find all permutations of 
a distinct integer array is O(n!), where n is the length of the input array.
'''

def permute(self, nums: List[int]) -> List[List[int]]:
    result = []

    def backtrack(used, current_perm):
        if len(current_perm) == len(nums):
            result.append(current_perm.copy())
            return 
        
        for num in nums:
            if num not in used:
                used.add(num)
                current_perm.append(num)
                backtrack(used, current_perm)
                current_perm.pop()
                used.remove(num)
    backtrack(set(), [])
    return result


# Example usage
nums = [1, 2, 3]
permutations = permute(nums)
print(permutations)


'''
Explanation :
Iterate over unused numbers:
    - Loop through each number (num) in nums.
    - If num is not present in the used set:
    - Add num to the used set to mark it as used in the current permutation.
    - Append num to the current_perm list.
    - Call backtrack recursively to explore permutations with the current choice (num) included.
    After the recursive call (exploring possibilities with num), backtrack by:
    - Removing num from the current_perm list.
    - Removing num from the used set to allow it for future permutations.

'''