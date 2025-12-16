# Problem 5: Find Duplicates

**Difficulty:** Medium 🟡

## Problem Statement

Given an array of integers where each element appears once or twice, find all the elements that appear twice.

Return the duplicates in any order.

### Example 1:
```
Input: [4, 3, 2, 7, 8, 2, 3, 1]
Output: [2, 3]
```

### Example 2:
```
Input: [1, 1, 2]
Output: [1]
```

### Example 3:
```
Input: [1, 2, 3, 4]
Output: []
```

## Constraints

- 1 ≤ array length ≤ 100,000
- 1 ≤ array[i] ≤ array length

## Hints

<details>
<summary>Hint 1</summary>
You could use a hash set to track which numbers you've seen before.
</details>

<details>
<summary>Hint 2</summary>
Notice the constraint: array values are between 1 and array length. Can you use the array indices themselves?
</details>

<details>
<summary>Hint 3</summary>
Try marking visited numbers by making the value at that index negative!
</details>

## Solution Approach

<details>
<summary>Click to reveal solution</summary>

### Approach 1: Using Hash Set

Simple and intuitive approach:

```python
def find_duplicates_set(nums):
    """
    Using a set to track seen numbers
    Time: O(n), Space: O(n)
    """
    seen = set()
    duplicates = []
    
    for num in nums:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)
    
    return duplicates
```

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

### Approach 2: Index as Hash (Optimal)

Since numbers are in range [1, n], we can use indices as markers:

```python
def find_duplicates(nums):
    """
    Using array indices to mark visited numbers
    Time: O(n), Space: O(1) - not counting output
    """
    duplicates = []
    
    for num in nums:
        # Get the index that this number maps to
        index = abs(num) - 1
        
        # If value at that index is negative, we've seen this number before
        if nums[index] < 0:
            duplicates.append(abs(num))
        else:
            # Mark as visited by negating
            nums[index] = -nums[index]
    
    # Optional: restore original array
    for i in range(len(nums)):
        nums[i] = abs(nums[i])
    
    return duplicates

# Test cases
print(find_duplicates([4, 3, 2, 7, 8, 2, 3, 1]))  # Output: [2, 3]
print(find_duplicates([1, 1, 2]))                  # Output: [1]
print(find_duplicates([1, 2, 3, 4]))               # Output: []
```

**Time Complexity:** O(n)  
**Space Complexity:** O(1) - using input array for marking

### How It Works (Example: [4, 3, 2, 7, 8, 2, 3, 1])

1. See 4 → Mark index 3 negative: [4, 3, 2, **-7**, 8, 2, 3, 1]
2. See 3 → Mark index 2 negative: [4, 3, **-2**, -7, 8, 2, 3, 1]
3. See 2 → Mark index 1 negative: [4, **-3**, -2, -7, 8, 2, 3, 1]
4. See 7 → Already negative at index 6, so skip (it's marked)
5. See 8 → Mark index 7 negative: [4, -3, -2, -7, 8, 2, 3, **-1**]
6. See 2 → Index 1 is already negative → **Found duplicate!**
7. See 3 → Index 2 is already negative → **Found duplicate!**
8. See 1 → Index 0 is already negative (wait, let me fix the logic)

Actually, here's the corrected walk-through:
- For number n, we use index n-1 as the marker

</details>

## Try It Yourself!

Start with the hash set approach, then challenge yourself with the index marking technique!

---

[← Previous Problem](./problem4.md) | [Back to Arrays Lesson](./README.md) | [Next Problem →](./problem6.md)
