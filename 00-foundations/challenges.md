# Foundations Module - Practice Challenges

These challenges will help you master the concepts from the foundations module, particularly time and space complexity analysis and the problem-solving framework.

## Challenge 1: Analyze Time Complexity (Beginner)

**Objective**: Determine the time complexity of given code snippets.

### Problem 1A

Analyze the time complexity of this function:

```python
def process_first_three(arr):
    """Process the first three elements of an array"""
    if len(arr) < 3:
        return None
    
    total = arr[0] + arr[1] + arr[2]
    return total
```

**Questions**:
1. What is the time complexity? Explain why.
2. How does the runtime change if the array has 10 elements vs 10,000 elements?
3. What operations are being counted?

<details>
<summary>Click to see answer</summary>

**Answer**: **O(1)** - Constant time

**Explanation**:
- The function performs a fixed number of operations regardless of array size
- Operations: 1 length check, 3 array accesses, 2 additions
- Total: ~6 operations, always the same
- Even if array has millions of elements, we only access the first 3
- This is the definition of constant time complexity

</details>

### Problem 1B

Analyze the time complexity of this function:

```python
def find_target_count(arr, target):
    """Count how many times target appears in array"""
    count = 0
    for element in arr:
        if element == target:
            count += 1
    return count
```

**Questions**:
1. What is the time complexity?
2. What is the best case scenario?
3. What is the worst case scenario?
4. Does the position of target values matter?

<details>
<summary>Click to see answer</summary>

**Answer**: **O(n)** - Linear time

**Explanation**:
- The function must examine every element in the array
- Operations per element: 1 comparison, possibly 1 increment
- Total: approximately n operations (where n = array length)
- Best case: Still O(n) - must check all elements
- Worst case: Still O(n) - must check all elements
- Position doesn't matter - we always scan the entire array
- Cannot optimize without additional data structures

</details>

---

## Challenge 2: Analyze Nested Operations (Beginner)

**Objective**: Understand how nested loops affect time complexity.

### Problem 2A

```python
def print_pairs(arr):
    """Print all possible pairs from an array"""
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            print(f"Pair: {arr[i]}, {arr[j]}")
```

**Questions**:
1. What is the time complexity?
2. How many pairs are printed for an array of length 5?
3. How many pairs for an array of length 10?
4. Why is the inner loop starting at `i + 1`?

<details>
<summary>Click to see answer</summary>

**Answer**: **O(n²)** - Quadratic time

**Explanation**:
- Outer loop: runs n times
- Inner loop: runs (n-1), (n-2), ..., 1 times
- Total iterations: (n-1) + (n-2) + ... + 1 = n(n-1)/2
- For n=5: 4 + 3 + 2 + 1 = 10 pairs
- For n=10: 9 + 8 + 7 + ... + 1 = 45 pairs
- The formula n(n-1)/2 simplifies to O(n²) in Big-O notation
- Starting at i+1 avoids duplicates and self-pairs

</details>

### Problem 2B

```python
def create_grid(n):
    """Create an n×n multiplication table"""
    grid = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(i * j)
        grid.append(row)
    return grid
```

**Questions**:
1. What is the time complexity?
2. What is the space complexity?
3. How many multiplications for n=3?
4. How many multiplications for n=100?

<details>
<summary>Click to see answer</summary>

**Answer**: 
- **Time complexity**: **O(n²)**
- **Space complexity**: **O(n²)**

**Explanation**:
- Outer loop: n iterations
- Inner loop: n iterations per outer iteration
- Total iterations: n × n = n²
- Each iteration does 1 multiplication and 1 append
- For n=3: 9 multiplications
- For n=100: 10,000 multiplications
- Space: Creates n×n grid = n² elements stored
- This is a case where time and space complexity match

</details>

---

## Challenge 3: Write O(1) Solution (Intermediate)

**Objective**: Implement a function that achieves constant time complexity.

### Problem Statement

Implement a function `get_middle_element(arr)` that returns the middle element of an array in O(1) time complexity. For arrays with odd length, return the center element. For even length arrays, return the element at index `len(arr) // 2` (using integer division).

**Requirements**:
- Time complexity must be O(1)
- Space complexity should be O(1)
- Handle edge cases (empty array)

**Examples**:
```python
get_middle_element([1, 2, 3, 4, 5])  # Returns 3 (index 2, the center element)
get_middle_element([1, 2, 3, 4])     # Returns 3 (index 2, len=4, 4//2=2)
get_middle_element([7])              # Returns 7 (single element)
get_middle_element([])               # Returns None (empty array)
```

**Your implementation**:
```python
def get_middle_element(arr):
    """
    Return the middle element of an array in O(1) time.
    
    Args:
        arr: List of elements
        
    Returns:
        Middle element or None if array is empty
    """
    # Your code here
    pass
```

<details>
<summary>Click to see solution</summary>

```python
def get_middle_element(arr):
    """
    Return the middle element of an array in O(1) time.
    
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    if len(arr) == 0:
        return None
    
    mid_index = len(arr) // 2
    return arr[mid_index]
```

**Why it's O(1)**:
- `len(arr)`: O(1) - Python stores array length
- Integer division: O(1) - single operation
- Array access `arr[mid_index]`: O(1) - direct indexing
- No loops or recursive calls
- Operations don't depend on array size

**Key insight**: Direct array indexing is always O(1) because arrays store elements in contiguous memory. The computer can calculate the memory address instantly using: `base_address + (index × element_size)`.

</details>

---

## Challenge 4: Write O(n) Solution (Intermediate)

**Objective**: Implement an efficient linear time solution.

### Problem Statement

Given an array of integers, find the **second largest** element. Your solution must run in O(n) time.

**Requirements**:
- Time complexity must be O(n) - single pass through array
- Space complexity should be O(1)
- Handle edge cases (fewer than 2 elements, all elements the same)

**Examples**:
```python
find_second_largest([10, 5, 20, 8, 15])  # Returns 15
find_second_largest([3, 3, 2, 1])        # Returns 3
find_second_largest([5])                 # Returns None
find_second_largest([7, 7, 7, 7])        # Returns 7
```

**Your implementation**:
```python
def find_second_largest(arr):
    """
    Find the second largest element in an array.
    
    Args:
        arr: List of integers
        
    Returns:
        Second largest integer or None if not enough elements
    """
    # Your code here
    pass
```

**Hints**:
- Keep track of the largest and second largest as you scan
- Update both variables when you find a new maximum
- What happens when you encounter a duplicate of the maximum?

<details>
<summary>Click to see solution</summary>

```python
def find_second_largest(arr):
    """
    Find the second largest element in an array.
    
    Time Complexity: O(n) - single pass
    Space Complexity: O(1) - only two variables
    """
    if len(arr) < 2:
        return None
    
    largest = second_largest = float('-inf')
    
    for num in arr:
        if num > largest:
            # New maximum found, shift everything
            second_largest = largest
            largest = num
        elif num > second_largest:
            # Not larger than max, but larger than second
            second_largest = num
    
    # Handle case where all elements are the same
    if second_largest == float('-inf'):
        return None
    
    return second_largest
```

**Why it's O(n)**:
- Single loop through array: n iterations
- Per iteration: 2 comparisons (worst case), 2 assignments (worst case)
- Total: ~4n operations
- Big-O: O(n) after dropping constant

**Alternative approach** (slightly different semantics):
```python
def find_second_largest_v2(arr):
    """Find second largest unique value"""
    if len(arr) < 2:
        return None
    
    # Remove duplicates and sort would be O(n log n)
    # But we can do it in O(n):
    
    largest = second = float('-inf')
    
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    
    return second if second != float('-inf') else None
```

</details>

---

## Challenge 5: Compare Approaches (Advanced)

**Objective**: Compare different algorithmic approaches to the same problem.

### Problem Statement

Implement TWO different solutions to find all duplicate elements in an array, then analyze their trade-offs.

**Requirements**:
- Solution 1: Optimize for space (minimize memory usage)
- Solution 2: Optimize for time (minimize runtime)
- Analyze time and space complexity for both
- Compare when each approach is preferable

**Examples**:
```python
find_duplicates([1, 2, 3, 2, 4, 1, 5])  # Returns [1, 2]
find_duplicates([1, 1, 1, 1])           # Returns [1]
find_duplicates([1, 2, 3, 4])           # Returns []
```

**Your implementations**:
```python
def find_duplicates_space_optimized(arr):
    """
    Find duplicates minimizing space usage.
    
    Args:
        arr: List of integers
        
    Returns:
        List of duplicate values
    """
    # Your code here
    pass

def find_duplicates_time_optimized(arr):
    """
    Find duplicates minimizing time.
    
    Args:
        arr: List of integers
        
    Returns:
        List of duplicate values
    """
    # Your code here
    pass
```

<details>
<summary>Click to see solutions</summary>

### Solution 1: Space-Optimized (Sorting Approach)

```python
def find_duplicates_space_optimized(arr):
    """
    Find duplicates by sorting first.
    
    Time Complexity: O(n log n) - dominated by sorting
    Space Complexity: O(1) - only stores result (if we sort in-place)
                      O(n) - if using Python's sort (creates new list)
    """
    if len(arr) < 2:
        return []
    
    duplicates = []
    sorted_arr = sorted(arr)  # O(n log n) time, O(n) space
    
    for i in range(1, len(sorted_arr)):
        # Check adjacent elements
        if sorted_arr[i] == sorted_arr[i-1]:
            # Avoid adding same duplicate multiple times
            if not duplicates or duplicates[-1] != sorted_arr[i]:
                duplicates.append(sorted_arr[i])
    
    return duplicates
```

### Solution 2: Time-Optimized (Hash Set Approach)

```python
def find_duplicates_time_optimized(arr):
    """
    Find duplicates using a hash set for O(1) lookups.
    
    Time Complexity: O(n) - single pass through array
    Space Complexity: O(n) - hash set stores up to n elements
    """
    if len(arr) < 2:
        return []
    
    seen = set()
    duplicates = set()
    
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return list(duplicates)
```

### Complexity Comparison

| Approach | Time | Space | Best For |
|----------|------|-------|----------|
| Space-Optimized | O(n log n) | O(1)* | Memory-constrained systems |
| Time-Optimized | O(n) | O(n) | Time-critical applications |

*Assuming in-place sort; Python's sort uses O(n) space

### When to Use Each Approach

**Use Space-Optimized (Sorting) when**:
- Memory is limited (embedded systems, mobile devices)
- Array is already sorted or nearly sorted
- You can modify the original array
- n is small enough that O(n log n) is acceptable

**Use Time-Optimized (Hash Set) when**:
- Speed is critical
- Memory is abundant
- Working with large datasets where O(n log n) vs O(n) matters
- Need to preserve original array order

**Example scenario**:
```
Small array (n=100):
- Sorting: ~700 operations, minimal memory
- Hash Set: ~100 operations, ~100 memory units
Both acceptable!

Large array (n=1,000,000):
- Sorting: ~20,000,000 operations, minimal memory
- Hash Set: ~1,000,000 operations, ~1,000,000 memory units
Hash set 20x faster! (if memory available)
```

</details>

---

## Challenge 6: Optimize an Algorithm (Advanced)

**Objective**: Take an inefficient algorithm and optimize it using better data structures or algorithmic techniques.

### Problem Statement

The function below checks if two arrays have any common elements. It works correctly but is inefficient.

**Given inefficient code**:
```python
def has_common_elements_slow(arr1, arr2):
    """
    Check if two arrays share any common elements.
    This version is SLOW - can you make it faster?
    """
    for element1 in arr1:
        for element2 in arr2:
            if element1 == element2:
                return True
    return False
```

**Your tasks**:
1. Analyze the time and space complexity of the given code
2. Implement an optimized version that's faster
3. Compare the complexities of both versions
4. Calculate the real-world difference for large inputs

**Test cases**:
```python
has_common_elements([1, 2, 3], [4, 5, 6])      # False
has_common_elements([1, 2, 3], [3, 4, 5])      # True
has_common_elements([], [1, 2, 3])             # False
has_common_elements([1, 2, 3], [])             # False
```

**Your optimized implementation**:
```python
def has_common_elements_fast(arr1, arr2):
    """
    Optimized version: Check if two arrays share common elements.
    
    Args:
        arr1: First array
        arr2: Second array
        
    Returns:
        Boolean: True if any common elements exist
    """
    # Your code here
    pass
```

<details>
<summary>Click to see solution</summary>

### Analysis of Original (Slow) Version

```python
def has_common_elements_slow(arr1, arr2):
    """INEFFICIENT VERSION"""
    for element1 in arr1:           # O(n) iterations
        for element2 in arr2:       # O(m) iterations per outer
            if element1 == element2:
                return True
    return False
```

**Complexity**:
- Time: **O(n × m)** where n = len(arr1), m = len(arr2)
- Space: **O(1)** - no additional data structures
- For n=1000, m=1000: up to 1,000,000 comparisons!

### Optimized Solution

```python
def has_common_elements_fast(arr1, arr2):
    """
    OPTIMIZED VERSION using hash set
    
    Time Complexity: O(n + m) - linear in total elements
    Space Complexity: O(n) - store first array in set
    """
    # Edge cases
    if not arr1 or not arr2:
        return False
    
    # Convert first array to set for O(1) lookups
    set1 = set(arr1)  # O(n) time, O(n) space
    
    # Check each element of second array
    for element in arr2:  # O(m) iterations
        if element in set1:  # O(1) lookup
            return True
    
    return False
```

**Why it's faster**:
- Creating set from arr1: O(n)
- Checking each arr2 element against set: O(m)
- Total: O(n + m) instead of O(n × m)
- Set lookup is O(1) vs array scan O(n)

### Alternative: Use Set Intersection

```python
def has_common_elements_pythonic(arr1, arr2):
    """
    Most Pythonic version
    
    Time Complexity: O(n + m)
    Space Complexity: O(n + m)
    """
    if not arr1 or not arr2:
        return False
    
    return len(set(arr1) & set(arr2)) > 0
    
    # Or even simpler:
    # return bool(set(arr1) & set(arr2))
```

### Performance Comparison

Let's compare with concrete numbers:

| Array Sizes | Slow O(n×m) | Fast O(n+m) | Speedup |
|-------------|-------------|-------------|---------|
| n=10, m=10 | 100 ops | 20 ops | 5x |
| n=100, m=100 | 10,000 ops | 200 ops | 50x |
| n=1000, m=1000 | 1,000,000 ops | 2,000 ops | 500x |
| n=10000, m=10000 | 100,000,000 ops | 20,000 ops | 5,000x |

**Real-world impact**:
```
Assume 1 operation = 1 microsecond

n=1000, m=1000:
- Slow: 1,000,000 μs = 1 second
- Fast: 2,000 μs = 0.002 seconds
500x faster!

n=10000, m=10000:
- Slow: 100,000,000 μs = 100 seconds (1.7 minutes)
- Fast: 20,000 μs = 0.02 seconds
5,000x faster!
```

### Key Takeaway

**The right data structure makes all the difference!** 

By using a hash set (which provides O(1) lookups) instead of repeatedly scanning an array (O(n) per scan), we transformed an O(n × m) algorithm into an O(n + m) algorithm.

This is the essence of why data structures matter – they enable more efficient algorithms!

</details>

---

## Summary and Next Steps

These challenges covered:
- ✅ Analyzing time complexity of code (Challenges 1-2)
- ✅ Writing code with specific complexity requirements (Challenges 3-4)
- ✅ Comparing different algorithmic approaches (Challenges 5-6)

### Key Lessons

1. **Time complexity matters** - O(n²) vs O(n) can mean seconds vs hours
2. **Space-time trade-offs** - Often you can trade memory for speed
3. **Data structures enable efficiency** - Hash sets/tables provide O(1) lookups
4. **Always analyze before optimizing** - Understand current complexity first
5. **Real-world impact scales** - Small improvements matter at scale

### Ready for More?

Once you're comfortable with these challenges, you're ready to dive into specific data structures in the main modules!

Start with **[Arrays](../arrays/)** to see these concepts in action.

---

💡 **Remember**: The best way to learn is by doing. Don't just read the solutions – try to solve each challenge yourself first!
