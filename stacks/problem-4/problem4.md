# Problem 4: Next Greater Element

**Difficulty:** Medium 🟡

## Problem Statement

Find the next greater element for each element in an array. The next greater element is the first element to the right that is greater than the current element.

### Example:
```
Input: [4, 5, 2, 10]
Output: [5, 10, 10, -1]

Input: [4, 5, 2, 25]
Output: [5, 25, 25, -1]
```

## Solution

<details>
<summary>Click to reveal solution</summary>

```python
def next_greater_element(nums):
    result = [-1] * len(nums)
    stack = []  # Stores indices
    
    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    
    return result

# Time: O(n), Space: O(n)
```

</details>

[← Previous Problem](./problem3.md) | [Back to Stacks](./README.md) | [Next Problem →](./problem5.md)
