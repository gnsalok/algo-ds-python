'''
There are  n items, each with a value, and a target sum.
You need to find a subset of items that gives the target sum.

# Example:
items = [1, 2, 3, 4, 5]
target_sum = 9



'''

# TODO: add logic to return the values with will make the sum


def rec(level, sum_taken, cache={}):
    # Pruning
    if sum_taken > target_sum:
        return 0

    # Base case
    if level == n:
        return int(sum_taken == target_sum)

    # Cache check
    if (level, sum_taken) in cache:
        return cache[(level, sum_taken)]

    # Choice: skip or take the current item
    ans = rec(level + 1, sum_taken, cache) or rec(level + 1, sum_taken + items[level], cache)

    cache[(level, sum_taken)] = ans
    return ans

items = [1, 2, 3, 4, 5]
target_sum = 9
n = len(items)

print(rec(0, 0, {}))  # Output: 1



