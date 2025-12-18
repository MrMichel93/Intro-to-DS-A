# Problem 1: Find Maximum Element

**Difficulty:** Easy 🟢

## Problem Statement

Write a function that finds and returns the maximum element in an array of integers.

### Example 1:
```
Input: [3, 7, 2, 9, 1]
Output: 9
```

### Example 2:
```
Input: [-5, -2, -10, -1]
Output: -1
```

### Example 3:
```
Input: [42]
Output: 42
```

## Constraints

- The array will have at least one element
- Array elements can be positive, negative, or zero

## Hints

<details>
<summary>Hint 1</summary>
Start by assuming the first element is the maximum, then compare it with every other element.
</details>

<details>
<summary>Hint 2</summary>
You only need to make one pass through the array!
</details>

## Solution Approach

<details>
<summary>Click to reveal solution</summary>

### Algorithm

1. Initialize a variable to store the maximum value (start with the first element)
2. Loop through the rest of the array
3. If you find an element larger than the current maximum, update the maximum
4. Return the maximum value

### Python Implementation

```python
def find_maximum(arr):
    """
    Finds the maximum element in an array
    
    Args:
        arr: List of integers
    
    Returns:
        The maximum integer in the array
    """
    if not arr:
        return None
    
    max_val = arr[0]
    
    for num in arr:
        if num > max_val:
            max_val = num
    
    return max_val

# Test cases
print(find_maximum([3, 7, 2, 9, 1]))  # Output: 9
print(find_maximum([-5, -2, -10, -1]))  # Output: -1
print(find_maximum([42]))  # Output: 42
```

### Time and Space Complexity

- **Time Complexity:** O(n) - We visit each element once
- **Space Complexity:** O(1) - We only use a constant amount of extra space

### Alternative Solution

Python has a built-in `max()` function that does this:
```python
def find_maximum(arr):
    return max(arr)
```

But it's important to understand how to implement it yourself!

</details>

## Try It Yourself!

Before looking at the solution, try to implement this function on your own. Start with the easier approach and then optimize if needed.

---

[← Back to Arrays Lesson](./README.md) | [Next Problem →](./problem2.md)
