# Problem 3: Two Sum

**Difficulty:** Medium 🟡

## Problem Statement

Given an array of integers and a target sum, find two numbers in the array that add up to the target. Return the indices of these two numbers.

You may assume that each input has exactly one solution, and you cannot use the same element twice.

### Example 1:
```
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9
```

### Example 2:
```
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
```

### Example 3:
```
Input: nums = [3, 3], target = 6
Output: [0, 1]
```

## Constraints

- Array has at least 2 elements
- Only one valid answer exists
- Cannot use the same element twice

## Hints

<details>
<summary>Hint 1</summary>
For each number, what's its complement? (The number needed to reach the target)
</details>

<details>
<summary>Hint 2</summary>
A hash table can help you quickly check if you've seen a number before!
</details>

<details>
<summary>Hint 3</summary>
Think about storing numbers you've seen along with their indices.
</details>

## Solution Approach

<details>
<summary>Click to reveal solution</summary>

### Approach 1: Brute Force

Check every pair of numbers:

```python
def two_sum_brute(nums, target):
    """
    Brute force solution - check all pairs
    Time: O(n²), Space: O(1)
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```

**Time Complexity:** O(n²)  
**Space Complexity:** O(1)

### Approach 2: Hash Table (Optimal)

Use a dictionary to store numbers we've seen:

```python
def two_sum(nums, target):
    """
    Hash table solution - one pass
    Time: O(n), Space: O(n)
    """
    seen = {}  # Maps number to its index
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if we've seen the complement
        if complement in seen:
            return [seen[complement], i]
        
        # Store this number and its index
        seen[num] = i
    
    return []

# Test cases
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(two_sum([3, 2, 4], 6))       # Output: [1, 2]
print(two_sum([3, 3], 6))          # Output: [0, 1]
```

**Time Complexity:** O(n) - Single pass through array  
**Space Complexity:** O(n) - Hash table storage

### How It Works

1. For each number, calculate what we need to add to reach target (complement)
2. Check if we've already seen that complement
3. If yes, we found our pair!
4. If no, store current number for future lookups

</details>

## Try It Yourself!

Start with the brute force approach, then try to optimize using a hash table!

---

[← Previous Problem](./problem2.md) | [Back to Arrays Lesson](./README.md) | [Next Problem →](./problem4.md)
