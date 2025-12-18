# Problem 5: Daily Temperatures

**Difficulty:** Medium 🟡

## Problem Statement

Given an array of daily temperatures, return an array where each element tells you how many days you have to wait until a warmer temperature. If there is no future day with a warmer temperature, put 0 instead.

### Example:
```
Input: [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]
```

## Solution

<details>
<summary>Click to reveal solution</summary>

```python
def daily_temperatures(temperatures):
    n = len(temperatures)
    result = [0] * n
    stack = []  # Stores indices
    
    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_idx = stack.pop()
            result[prev_idx] = i - prev_idx
        stack.append(i)
    
    return result

# Time: O(n), Space: O(n)
```

</details>

[← Previous Problem](./problem4.md) | [Back to Stacks](./README.md) | [Next Problem →](./problem6.md)
