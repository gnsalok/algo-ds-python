import heapq

# Tasks with priorities (lower value indicates higher priority)
tasks = [("email", 3), ("report", 1), ("meeting", 2)]

# Create a min-heap based on task priorities
task_queue = []
for name, priority in tasks:
  heapq.heappush(task_queue, (priority, name))  # Push (priority, task_name)

# Process tasks in order of priority (highest priority first)
while task_queue:
  priority, task_name = heapq.heappop(task_queue)
  print(f"Processing task: {task_name} (priority: {priority})")
