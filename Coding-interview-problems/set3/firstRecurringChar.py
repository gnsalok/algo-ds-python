def first_recurring(arr):
    count = {}
    for char in arr:
        if char in count:
            return char
        count[char] = 1  # adding char into hashtable
        print(count)
    return None


arr = ["a", "b", "c", "d", "a"]
result = first_recurring(arr)
print(result)