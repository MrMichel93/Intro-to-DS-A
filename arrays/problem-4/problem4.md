# Problem 4: Rotate Array

**Difficulty:** Medium 🟡

## Problem Statement

Given an array, rotate the array to the right by `k` steps, where `k` is non-negative.

### Example 1:
```
Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
Output: [5, 6, 7, 1, 2, 3, 4]
Explanation:
  Rotate 1 step: [7, 1, 2, 3, 4, 5, 6]
  Rotate 2 steps: [6, 7, 1, 2, 3, 4, 5]
  Rotate 3 steps: [5, 6, 7, 1, 2, 3, 4]
```

### Example 2:
```
Input: nums = [-1, -100, 3, 99], k = 2
Output: [3, 99, -1, -100]
```

### Example 3:
```
Input: nums = [1, 2], k = 3
Output: [2, 1]
Explanation: k=3 is same as k=1 for array of length 2
```

## Constraints

- Rotate the array in-place
- 1 ≤ array length ≤ 100,000
- k ≥ 0

## Hints

<details>
<summary>Hint 1</summary>
What if k is larger than the array length? Think about the pattern!
</details>

<details>
<summary>Hint 2</summary>
Reversing parts of the array can help you achieve rotation efficiently.
</details>

<details>
<summary>Hint 3</summary>
Try reversing: (1) entire array, (2) first k elements, (3) remaining elements
</details>

## Solution Approach

<details>
<summary>Click to reveal solution</summary>

### Approach 1: Using Extra Array

```python
def rotate_simple(nums, k):
    """
    Simple approach using extra space
    Time: O(n), Space: O(n)
    """
    n = len(nums)
    k = k % n  # Handle k > n
    
    # Create rotated array
    rotated = nums[n-k:] + nums[:n-k]
    
    # Copy back to original
    for i in range(n):
        nums[i] = rotated[i]
```

### Approach 2: Reversal Algorithm (Optimal)

This clever solution reverses parts of the array:

```python
def rotate(nums, k):
    """
    Reversal algorithm - no extra space needed
    Time: O(n), Space: O(1)
    """
    n = len(nums)
    k = k % n  # Handle k larger than array length
    
    # Helper function to reverse a portion of array
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    # Three reversal steps
    reverse(0, n - 1)       # Reverse entire array
    reverse(0, k - 1)       # Reverse first k elements
    reverse(k, n - 1)       # Reverse remaining elements

# Test cases
nums1 = [1, 2, 3, 4, 5, 6, 7]
rotate(nums1, 3)
print(nums1)  # Output: [5, 6, 7, 1, 2, 3, 4]

nums2 = [-1, -100, 3, 99]
rotate(nums2, 2)
print(nums2)  # Output: [3, 99, -1, -100]
```

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

### Why This Works

For `[1, 2, 3, 4, 5, 6, 7]` with k=3:

1. Reverse all: `[7, 6, 5, 4, 3, 2, 1]`
2. Reverse first k: `[5, 6, 7, 4, 3, 2, 1]`
3. Reverse rest: `[5, 6, 7, 1, 2, 3, 4]` ✓

</details>

## Try It Yourself!

Try implementing both approaches. The reversal algorithm is tricky but elegant!

---

[← Previous Problem](./problem3.md) | [Back to Arrays Lesson](./README.md) | [Next Problem →](./problem5.md)
