# Problem 2: Number of Recent Calls

**Difficulty:** Easy 🟢

## Problem Statement

Write a class that counts the number of recent requests within a certain time frame. Implement the `RecentCounter` class with a `ping(t)` method that adds a new request at time `t` and returns the number of requests that have happened in the past 3000 milliseconds.

### Example:
```
RecentCounter counter = new RecentCounter()
counter.ping(1)     // returns 1  (requests at [1])
counter.ping(100)   // returns 2  (requests at [1, 100])
counter.ping(3001)  // returns 3  (requests at [1, 100, 3001])
counter.ping(3002)  // returns 3  (requests at [100, 3001, 3002])
```

## Solution

<details>
<summary>Click to reveal solution</summary>

```python
from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = deque()
    
    def ping(self, t):
        self.queue.append(t)
        
        # Remove requests older than 3000ms
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        
        return len(self.queue)

# Time: O(1) amortized, Space: O(W) where W is window size
```

</details>

[← Previous Problem](./problem1.md) | [Back to Queues](./README.md) | [Next Problem →](./problem3.md)
