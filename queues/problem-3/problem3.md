# Problem 3: Moving Average from Data Stream

**Difficulty:** Medium 🟡

## Problem Statement

Calculate the moving average of all integers in a sliding window of size `size`.

### Example:
```
MovingAverage m = new MovingAverage(3)
m.next(1)  // returns 1.0 = 1/1
m.next(10) // returns 5.5 = (1+10)/2
m.next(3)  // returns 4.67 = (1+10+3)/3
m.next(5)  // returns 6.0 = (10+3+5)/3
```

## Solution

<details>
<summary>Click to reveal solution</summary>

```python
from collections import deque

class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.queue = deque()
        self.sum = 0
    
    def next(self, val):
        self.queue.append(val)
        self.sum += val
        
        # Remove oldest if exceeds size
        if len(self.queue) > self.size:
            removed = self.queue.popleft()
            self.sum -= removed
        
        return self.sum / len(self.queue)

# Time: O(1), Space: O(size)
```

</details>

[← Previous Problem](./problem2.md) | [Back to Queues](./README.md) | [Next Problem →](./problem4.md)
