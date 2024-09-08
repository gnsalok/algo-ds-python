import heapq

# Sample list of unsorted numbers
data = [8, 3, 1, 4, 2, 7, 6, 5]

# Convert the list into a min-heap (smallest element at the root)
heapq.heapify(data)

print(data)  # Output: [1, 2, 3, 4, 5, 7, 6, 8] (min-heap representation)
