# Problem 6: Sliding Window Maximum

**Difficulty:** Hard 🔴

## Problem Statement

Given an array and a sliding window of size `k`, find the maximum element in each window as it slides from left to right.

### Example:
```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

Window positions:
[1  3  -1] -3  5  3  6  7  → 3
 1 [3  -1  -3] 5  3  6  7  → 3
 1  3 [-1  -3  5] 3  6  7  → 5
 1  3  -1 [-3  5  3] 6  7  → 5
 1  3  -1  -3 [5  3  6] 7  → 6
 1  3  -1  -3  5 [3  6  7] → 7
```

## Solution

<details>
<summary>Click to reveal solution</summary>

```python
from collections import deque

def max_sliding_window(nums, k):
    if not nums:
        return []
    
    result = []
    dq = deque()  # Stores indices
    
    for i in range(len(nums)):
        # Remove indices outside window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Remove smaller elements from rear
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        dq.append(i)
        
        # Add to result once we have k elements
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result

# Time: O(n), Space: O(k)
```

</details>

[← Previous Problem](./problem5.md) | [Back to Queues](./README.md)
