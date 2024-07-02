import heapq
from typing import List

def kth_largest_number(nums: List[int], k: int) -> int:
  """
  Finds the kth largest number in an array using a min-heap.

  Args:
      nums: List of integers representing the array.
      k: An integer representing the kth largest element to find.

  Returns:
      The kth largest element in the array.
  """

  # Create a min-heap to store the k largest elements encountered so far
  heap = []
  for num in nums:
    # Add elements to the heap, maintaining a size of k
    heapq.heappush(heap, num)
    if len(heap) > k:
      heapq.heappop(heap)  # Remove the smallest element if heap size exceeds k

  # The element at the root of the min-heap is the kth largest
  return heap[0]

# Example usage
nums = [3, 2, 1, 5, 6, 4]
k = 2
result = kth_largest_number(nums, k)
print(f"The {k}th largest number is: {result}")
