import heapq

# Sample data and desired number of top elements (largest)
data = [10, 5, 12, 3, 7, 18]
k = 4

# Create a max-heap (largest element at the root) using the first k elements
heap = data[:k]
heapq.heapify(heap)  # Convert the initial k elements to a max-heap

print(heap)

# Process remaining elements
for num in data[k:]:
  # If the current element is larger than the root (smallest in the max-heap)
  if num > heap[0]:
    # Replace the root with the current element (potentially larger)
    heapq.heapreplace(heap, num)

# The heap now contains the k largest elements
print(heap)  # Output: [10, 18, 12] (largest elements based on k)
