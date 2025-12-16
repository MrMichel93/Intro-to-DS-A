# Problem 6: Merge Sorted Arrays

**Difficulty:** Hard 🔴

## Problem Statement

You are given two sorted arrays `nums1` and `nums2`. Merge `nums2` into `nums1` as one sorted array.

The number of elements in `nums1` and `nums2` are `m` and `n` respectively. You may assume that `nums1` has enough space (size = m + n) to hold all elements.

### Example 1:
```
Input: 
  nums1 = [1, 2, 3, 0, 0, 0], m = 3
  nums2 = [2, 5, 6], n = 3
Output: [1, 2, 2, 3, 5, 6]
Explanation: Merge [1,2,3] and [2,5,6] into nums1
```

### Example 2:
```
Input:
  nums1 = [1], m = 1
  nums2 = [], n = 0
Output: [1]
```

### Example 3:
```
Input:
  nums1 = [0], m = 0
  nums2 = [1], n = 1
Output: [1]
```

## Constraints

- nums1 has length m + n (extra space already allocated)
- nums2 has length n
- Both arrays are sorted in non-decreasing order

## Hints

<details>
<summary>Hint 1</summary>
If you merge from the beginning, you'll have to shift elements. What if you merge from the end instead?
</details>

<details>
<summary>Hint 2</summary>
Use three pointers: one for the last element of nums1's actual data, one for the last of nums2, and one for the final position.
</details>

<details>
<summary>Hint 3</summary>
Start comparing from the largest elements and work backwards!
</details>

## Solution Approach

<details>
<summary>Click to reveal solution</summary>

### Approach 1: Merge and Sort

Simple but not optimal:

```python
def merge_simple(nums1, m, nums2, n):
    """
    Copy nums2 to end of nums1, then sort
    Time: O((m+n)log(m+n)), Space: O(1)
    """
    # Copy nums2 into nums1
    for i in range(n):
        nums1[m + i] = nums2[i]
    
    # Sort the entire array
    nums1.sort()
```

### Approach 2: Three Pointers (Optimal)

Merge from the end to avoid shifting:

```python
def merge(nums1, m, nums2, n):
    """
    Merge from the end using three pointers
    Time: O(m+n), Space: O(1)
    """
    # Three pointers
    p1 = m - 1      # Last element in nums1's actual data
    p2 = n - 1      # Last element in nums2
    p = m + n - 1   # Last position in nums1
    
    # Merge from the end
    while p2 >= 0:
        # If p1 is valid and nums1[p1] is larger
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            # nums2[p2] is larger or nums1 is exhausted
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

# Test cases
nums1 = [1, 2, 3, 0, 0, 0]
merge(nums1, 3, [2, 5, 6], 3)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]

nums1 = [1]
merge(nums1, 1, [], 0)
print(nums1)  # Output: [1]

nums1 = [0]
merge(nums1, 0, [1], 1)
print(nums1)  # Output: [1]
```

**Time Complexity:** O(m + n) - Single pass through both arrays  
**Space Complexity:** O(1) - Merging in-place

### How It Works

For `nums1 = [1, 2, 3, _, _, _]` and `nums2 = [2, 5, 6]`:

```
Step 1: Compare 3 vs 6 → Place 6
  [1, 2, 3, _, _, 6]
  
Step 2: Compare 3 vs 5 → Place 5
  [1, 2, 3, _, 5, 6]
  
Step 3: Compare 3 vs 2 → Place 3
  [1, 2, 3, 3, 5, 6] (wait, this should be)
  [1, 2, _, 3, 5, 6]
  
Step 4: Compare 2 vs 2 → Place 2 from nums2
  [1, 2, 2, 3, 5, 6]
  
Step 5: nums2 exhausted, nums1 elements already in place
```

The key insight: By filling from the end, we never overwrite data we still need!

</details>

## Try It Yourself!

This is a classic interview problem. Try implementing the three-pointer solution step by step!

---

[← Previous Problem](./problem5.md) | [Back to Arrays Lesson](./README.md)
