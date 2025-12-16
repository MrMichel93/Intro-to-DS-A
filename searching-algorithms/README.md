# Searching Algorithms

## What is Searching?

**Searching** is the process of finding a specific element in a collection of data. It's one of the most common operations in computer science.

```
Array: [3, 7, 1, 9, 4, 2, 8]
Search for: 9
Result: Found at index 3
```

## Why Searching Matters

Searching is fundamental to:
- **Databases** - Finding records
- **File systems** - Locating files
- **Web** - Search engines
- **AI/ML** - Feature matching
- **Games** - Pathfinding

## Algorithm Comparison

| Algorithm | Time (Best) | Time (Avg) | Time (Worst) | Space | Requirements |
|-----------|-------------|------------|--------------|-------|--------------|
| Linear Search | O(1) | O(n) | O(n) | O(1) | None |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) | Sorted array |
| Jump Search | O(1) | O(√n) | O(√n) | O(1) | Sorted array |
| Interpolation | O(1) | O(log log n) | O(n) | O(1) | Sorted, uniform |
| Exponential | O(1) | O(log n) | O(log n) | O(1) | Sorted array |

## Basic Searching Algorithms

### 1. Linear Search
Check each element sequentially until found.

```python
def linear_search(arr, target):
    """
    Search for target in array sequentially
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Found at index i
    return -1  # Not found

# Time: O(n), Space: O(1)
# Good for: Small or unsorted arrays
```

**Example:**
```
Array: [5, 2, 8, 1, 9]
Target: 8

Step 1: Check 5 → Not match
Step 2: Check 2 → Not match
Step 3: Check 8 → Match! Return index 2
```

### 2. Binary Search
Repeatedly divide sorted array in half.

```python
def binary_search(arr, target):
    """
    Search for target in sorted array using divide and conquer
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid  # Found!
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
    
    return -1  # Not found

# Time: O(log n), Space: O(1)
# Good for: Large sorted arrays
```

**Example:**
```
Sorted Array: [1, 3, 5, 7, 9, 11, 13]
Target: 7

Step 1: mid=3, arr[3]=7 → Found!
```

**Recursive Version:**
```python
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
```

## Advanced Searching Algorithms

### 3. Jump Search
Jump ahead by √n steps, then linear search.

```python
import math

def jump_search(arr, target):
    """
    Jump √n elements ahead, then linear search
    """
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    
    # Find block where element may be present
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    # Linear search in block
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    
    if arr[prev] == target:
        return prev
    
    return -1

# Time: O(√n), Space: O(1)
# Good for: Sorted arrays where binary search is expensive (like on disk)
```

### 4. Interpolation Search
Estimate position based on value distribution.

```python
def interpolation_search(arr, target):
    """
    Estimate position using interpolation formula
    """
    left, right = 0, len(arr) - 1
    
    while left <= right and arr[left] <= target <= arr[right]:
        if left == right:
            if arr[left] == target:
                return left
            return -1
        
        # Interpolation formula
        pos = left + int((target - arr[left]) * (right - left) / 
                        (arr[right] - arr[left]))
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
    
    return -1

# Time: O(log log n) average, O(n) worst, Space: O(1)
# Good for: Uniformly distributed sorted data
```

### 5. Exponential Search
Find range with exponential jumps, then binary search.

```python
def exponential_search(arr, target):
    """
    Find range exponentially, then binary search
    """
    if arr[0] == target:
        return 0
    
    # Find range for binary search
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
    
    # Binary search in found range
    return binary_search(arr, target, i // 2, min(i, len(arr) - 1))

# Time: O(log n), Space: O(1)
# Good for: Unbounded/infinite arrays
```

## Specialized Searching

### 6. Ternary Search
Divide array into three parts.

```python
def ternary_search(arr, target, left, right):
    """
    Divide array into three parts
    """
    if left > right:
        return -1
    
    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3
    
    if arr[mid1] == target:
        return mid1
    if arr[mid2] == target:
        return mid2
    
    if target < arr[mid1]:
        return ternary_search(arr, target, left, mid1 - 1)
    elif target > arr[mid2]:
        return ternary_search(arr, target, mid2 + 1, right)
    else:
        return ternary_search(arr, target, mid1 + 1, mid2 - 1)

# Time: O(log₃ n) ≈ O(log n), Space: O(log n)
# Good for: Finding maximum/minimum in unimodal functions
```

### 7. Fibonacci Search
Use Fibonacci numbers to divide array.

```python
def fibonacci_search(arr, target):
    """
    Use Fibonacci numbers for division
    """
    n = len(arr)
    fib2 = 0  # (m-2)th Fibonacci
    fib1 = 1  # (m-1)th Fibonacci
    fib = fib2 + fib1  # mth Fibonacci
    
    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1
    
    offset = -1
    
    while fib > 1:
        i = min(offset + fib2, n - 1)
        
        if arr[i] < target:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif arr[i] > target:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i
    
    if fib1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1
    
    return -1

# Time: O(log n), Space: O(1)
# Good for: When division is expensive
```

## Binary Search Variants

### Find First Occurrence
```python
def find_first(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result
```

### Find Last Occurrence
```python
def find_last(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result
```

### Find Insertion Position
```python
def search_insert(arr, target):
    """
    Find position where target should be inserted
    """
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left
```

## Real-World Applications

### 1. Autocomplete
Binary search in sorted dictionary for prefix matching.

### 2. Version Control
Binary search to find commit that introduced a bug (git bisect).

### 3. Database Indexes
B-trees use binary search for fast lookups.

### 4. Spell Checkers
Search in dictionary of valid words.

### 5. Network Routing
Find optimal path in routing tables.

## When to Use Each Algorithm

### Linear Search:
- Small arrays (< 100 elements)
- Unsorted data
- Need to check all elements anyway

### Binary Search:
- Large sorted arrays
- Random access available
- Need O(log n) performance

### Jump Search:
- Sequential access is faster than random access
- Sorted arrays on disk/tape

### Interpolation Search:
- Uniformly distributed data
- Need better than O(log n)

### Exponential Search:
- Unbounded/infinite arrays
- Target near beginning

## Practice Problems

Master searching with these problems:

1. **[Problem 1: Binary Search](./problem1.md)** - Easy 🟢
2. **[Problem 2: First Bad Version](./problem2.md)** - Easy 🟢
3. **[Problem 3: Search in Rotated Array](./problem3.md)** - Medium 🟡
4. **[Problem 4: Find Peak Element](./problem4.md)** - Medium 🟡
5. **[Problem 5: Search 2D Matrix](./problem5.md)** - Medium 🟡
6. **[Problem 6: Median of Two Sorted Arrays](./problem6.md)** - Hard 🔴

---

💡 **Pro Tip**: Binary search is incredibly powerful! Master it thoroughly - it appears in countless problems beyond simple array searching (finding square roots, optimization problems, etc.)
