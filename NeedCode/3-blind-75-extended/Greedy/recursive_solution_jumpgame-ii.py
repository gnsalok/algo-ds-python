class Solution:
    def jump(self, nums: List[int]) -> int:
        def getMinJumps(index, memo):
            if index == len(nums) - 1:
                return 0  # Reached the end, minimum jumps required is 0

            if index in memo:
                return memo[index]

            min_jumps = float('inf')
            for jump in range(1, nums[index] + 1):  # Explore all possible jumps within range
                next_index = index + jump
                if 0 <= next_index < len(nums):  # Ensure next index is within bounds
                    result = getMinJumps(next_index, memo)
                    if result != float('inf'):  # Update min_jumps if a valid path exists
                        min_jumps = min(min_jumps, result + 1)

            memo[index] = min_jumps
            return min_jumps

        memo = {}  # Dictionary to store minimum jumps for each index (memoization)
        result = getMinJumps(0, memo)
        return result if result != float('inf') else -1  # -1 if no valid path exists
