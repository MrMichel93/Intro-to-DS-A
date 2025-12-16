# Problem 2: Reverse an Array

**Difficulty:** Easy 🟢

## Problem Statement

Write a function that reverses an array in-place. This means you should modify the original array without creating a new one.

### Example 1:
```
Input: [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
```

### Example 2:
```
Input: ["hello", "world"]
Output: ["world", "hello"]
```

### Example 3:
```
Input: [7]
Output: [7]
```

## Constraints

- Modify the array in-place (don't create a new array)
- Can contain any type of elements

## Hints

<details>
<summary>Hint 1</summary>
Think about swapping elements from both ends of the array, moving towards the center.
</details>

<details>
<summary>Hint 2</summary>
You only need to swap the first half with the second half!
</details>

## Solution Approach

<details>
<summary>Click to reveal solution</summary>

### Algorithm

1. Use two pointers: one at the start (left) and one at the end (right)
2. Swap the elements at these positions
3. Move left pointer forward and right pointer backward
4. Continue until pointers meet in the middle

### Python Implementation

```python
def reverse_array(arr):
    """
    Reverses an array in-place
    
    Args:
        arr: List to be reversed
    
    Returns:
        The same list, reversed
    """
    left = 0
    right = len(arr) - 1
    
    while left < right:
        # Swap elements
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return arr

# Test cases
print(reverse_array([1, 2, 3, 4, 5]))  # Output: [5, 4, 3, 2, 1]
print(reverse_array(["hello", "world"]))  # Output: ["world", "hello"]
print(reverse_array([7]))  # Output: [7]
```

### Time and Space Complexity

- **Time Complexity:** O(n) - We visit each element once
- **Space Complexity:** O(1) - Only using pointers, no extra arrays

### Alternative Approach

Using Python's built-in reverse:
```python
def reverse_array(arr):
    arr.reverse()
    return arr
```

Or slicing (but this creates a new array):
```python
def reverse_array(arr):
    return arr[::-1]
```

</details>

## Try It Yourself!

Try implementing this with the two-pointer approach before looking at the solution!

---

[← Previous Problem](./problem1.md) | [Back to Arrays Lesson](./README.md) | [Next Problem →](./problem3.md)
