# Problem 6: Largest Rectangle in Histogram

**Difficulty:** Hard 🔴

## Problem Statement

Given heights of bars in a histogram, find the area of the largest rectangle that can be formed.

### Example:
```
Input: heights = [2, 1, 5, 6, 2, 3]
Output: 10
Explanation: Rectangle of height 5 and width 2 (bars 5 and 6)
```

## Solution

<details>
<summary>Click to reveal solution</summary>

```python
def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    index = 0
    
    while index < len(heights):
        if not stack or heights[index] >= heights[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            top = stack.pop()
            width = index if not stack else index - stack[-1] - 1
            area = heights[top] * width
            max_area = max(max_area, area)
    
    while stack:
        top = stack.pop()
        width = index if not stack else index - stack[-1] - 1
        area = heights[top] * width
        max_area = max(max_area, area)
    
    return max_area

# Time: O(n), Space: O(n)
```

</details>

[← Previous Problem](./problem5.md) | [Back to Stacks](./README.md)
