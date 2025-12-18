# Problem 5: Task Scheduler

**Difficulty:** Medium 🟡

## Problem Statement

Given tasks represented by characters and a cooldown period `n`, find the minimum time to complete all tasks. The same task must wait at least `n` intervals before it can be executed again.

### Example:
```
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B
```

## Solution

<details>
<summary>Click to reveal solution</summary>

```python
from collections import Counter
import heapq

def least_interval(tasks, n):
    # Count frequency of each task
    counts = Counter(tasks)
    max_heap = [-count for count in counts.values()]
    heapq.heapify(max_heap)
    
    time = 0
    queue = []  # (count, available_time)
    
    while max_heap or queue:
        time += 1
        
        if max_heap:
            count = heapq.heappop(max_heap) + 1
            if count < 0:  # Still has tasks remaining
                queue.append((count, time + n))
        
        # Check if any task is ready from cooldown
        if queue and queue[0][1] == time:
            heapq.heappush(max_heap, queue.pop(0)[0])
    
    return time

# Time: O(n), Space: O(1) - at most 26 unique tasks
```

</details>

[← Previous Problem](./problem4.md) | [Back to Queues](./README.md) | [Next Problem →](./problem6.md)
