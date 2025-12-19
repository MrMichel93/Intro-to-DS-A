# Arrays

## Overview
An **array** is a fundamental data structure that stores elements in contiguous memory locations, allowing direct access to any element using its index position. Think of it like a row of numbered boxes where each box holds a value, and you can instantly jump to any box by knowing its position number. Arrays are the building blocks for more complex data structures and are one of the most widely used structures in programming.

## Why It Matters
Arrays power countless real-world applications and are essential for efficient data management:

- **Music Streaming Apps (Spotify, Apple Music)**: Your playlists are stored as arrays of songs. When you skip to track #5, the app uses array indexing to instantly jump to that song without checking tracks 1-4.

- **Image Processing (Instagram, Photoshop)**: Digital images are 2D arrays (matrices) of pixel values. When you apply a filter, the algorithm processes each pixel by accessing its position in the array. A 1920x1080 image is actually a 2D array with over 2 million elements!

- **Gaming Leaderboards (Fortnite, League of Legends)**: Player scores are stored in arrays, making it fast to display rankings. Arrays allow quick access to "Who's in 3rd place?" or "What's my rank?" without searching through all players.

- **E-commerce Shopping Carts (Amazon, eBay)**: Items in your cart are stored in an array. When you click "remove item #3", the system uses array operations to modify your cart instantly.

- **Stock Market Data**: Trading platforms use arrays to store historical stock prices. Each index represents a time point, allowing traders to quickly analyze price trends and patterns.

## Visual Representation
```
Array Visualization:
┌─────┬─────┬─────┬─────┬─────┐
│ 10  │ 25  │ 30  │ 47  │ 52  │  <- Values
└─────┴─────┴─────┴─────┴─────┘
   0     1     2     3     4      <- Indices (start at 0)
   ↑                         ↑
 First                     Last
element                  element

Memory Layout (Contiguous):
┌──────────────────────────────┐
│ [10][25][30][47][52]         │  <- All elements stored side-by-side
└──────────────────────────────┘
  Memory address: 1000→1020

Why this matters: 
- If arr[0] is at address 1000 and each element is 4 bytes,
- arr[2] is at address 1000 + (2 × 4) = 1008
- Computer can calculate any position instantly!

2D Array (Matrix) Example:
      Column: 0   1   2
           ┌───┬───┬───┐
    Row 0: │ 1 │ 2 │ 3 │
           ├───┼───┼───┤
    Row 1: │ 4 │ 5 │ 6 │
           ├───┼───┼───┤
    Row 2: │ 7 │ 8 │ 9 │
           └───┴───┴───┘

Access: matrix[1][2] = 6 (row 1, column 2)
```

## Key Concepts

### 1. **Zero-Based Indexing**
Arrays use indices starting from 0, not 1. The first element is at index 0, the second at index 1, and so on. This is because indices represent the offset from the starting memory address.

**Think Like a Programmer:** If an array has `n` elements, valid indices are `0` to `n-1`. The last element is always at index `len(array) - 1`.

### 2. **Contiguous Memory Allocation**
All array elements are stored in consecutive memory locations. This enables O(1) access time because the computer can calculate any element's exact memory address using: `base_address + (index × element_size)`.

**Think Like a Programmer:** Contiguous storage is why arrays are fast for reading but slow for inserting. Adding an element in the middle requires shifting all subsequent elements.

### 3. **Fixed Size (in classical arrays)**
Traditional arrays have a predetermined size that cannot change after creation. Python lists are dynamic arrays that automatically resize, but classical arrays in languages like C or Java have fixed capacity.

**Think Like a Programmer:** If you're working with truly fixed-size data (like a chess board: always 8×8), arrays are perfect. For variable-size data, consider dynamic alternatives.

### 4. **Homogeneous Elements**
Arrays typically store elements of the same data type (all integers, all strings, etc.). This uniformity allows the computer to know exactly how much memory each element needs, enabling fast address calculation.

**Think Like a Programmer:** While Python lists can mix types, keeping arrays homogeneous is often better for performance and code clarity.

### 5. **Direct Access (Random Access)**
You can access any element directly by its index without traversing other elements. This is array's superpower compared to linked lists where you must walk through elements sequentially.

**Think Like a Programmer:** If your algorithm frequently needs "give me element at position i", arrays are your best choice.

### 6. **Cache Friendliness**
Because elements are contiguous in memory, arrays work well with CPU caches. When you access one element, nearby elements are automatically loaded into fast cache memory, making sequential access incredibly efficient.

**Think Like a Programmer:** This is why iterating through an array is much faster than traversing scattered data structures like linked lists.

## How It Works

### Array Creation and Access
When you create an array, the computer allocates a continuous block of memory. Each element occupies a fixed amount of space based on its data type.

**Step-by-step process for accessing an element:**
1. Start with the base address (memory location of first element)
2. Multiply the index by element size
3. Add this offset to the base address
4. Read the value at that memory location

**Mathematical formula:** `element_address = base_address + (index × element_size)`

This calculation takes the same time regardless of which element you're accessing, giving us O(1) constant time complexity.

### Example Walkthrough

**Scenario:** You're building a grade tracking system for a class of 5 students.

```python
# Create an array to store test scores
test_scores = [85, 92, 78, 95, 88]

# Student names (for reference)
students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
```

**Operation 1: Accessing a grade (O(1) - Instant)**
```python
# Teacher asks: "What did Charlie score?"
# Charlie is student #2 (index 2, since we start at 0)
charlie_score = test_scores[2]
print(f"Charlie scored: {charlie_score}")  # Output: 78

# Behind the scenes:
# 1. Computer knows array starts at memory address 1000
# 2. Each integer takes 4 bytes
# 3. Charlie's score is at: 1000 + (2 × 4) = address 1008
# 4. Read value at 1008 → returns 78
# Total operations: 1 calculation + 1 read = O(1)
```

**Operation 2: Updating a grade (O(1) - Instant)**
```python
# Charlie retook the test and scored better!
test_scores[2] = 88
print(test_scores)  # [85, 92, 88, 95, 88]

# Behind the scenes:
# 1. Calculate address: 1000 + (2 × 4) = 1008
# 2. Write new value (88) to address 1008
# Total operations: 1 calculation + 1 write = O(1)
```

**Operation 3: Finding a score (O(n) - Must search)**
```python
# "Which student scored 95?"
def find_student_by_score(scores, target):
    for i in range(len(scores)):
        if scores[i] == target:
            return i
    return -1

student_index = find_student_by_score(test_scores, 95)
print(f"Student at index {student_index} scored 95")  # Diana, index 3

# Behind the scenes:
# 1. Check scores[0]: 85 ≠ 95
# 2. Check scores[1]: 92 ≠ 95
# 3. Check scores[2]: 88 ≠ 95
# 4. Check scores[3]: 95 = 95 ✓ Found!
# Worst case: must check all n elements = O(n)
```

**Operation 4: Calculating class average**
```python
# Calculate the average test score
total = sum(test_scores)  # 85 + 92 + 88 + 95 + 88 = 448
average = total / len(test_scores)  # 448 / 5 = 89.6
print(f"Class average: {average}")

# Behind the scenes:
# Must visit every element to sum them: O(n)
```

**Operation 5: Finding highest and lowest scores**
```python
highest = max(test_scores)  # 95
lowest = min(test_scores)   # 78
print(f"Range: {lowest} to {highest}")

# Behind the scenes:
# Must check every element to find min/max: O(n)
```

## Python Implementation

```python
# ============================================
# BASIC ARRAY OPERATIONS IN PYTHON
# ============================================

class ArrayOperations:
    """
    Demonstrates fundamental array operations with detailed explanations.
    Python lists are dynamic arrays - they can grow/shrink automatically.
    """
    
    def __init__(self):
        # Create an empty array
        self.data = []
    
    # =============== CREATION ===============
    
    def create_array(self, size, default_value=0):
        """
        Create an array of given size with default values.
        Time Complexity: O(n) - must initialize n elements
        Space Complexity: O(n) - stores n elements
        """
        # Method 1: Using list multiplication
        arr = [default_value] * size
        
        # Method 2: Using list comprehension
        # arr = [default_value for _ in range(size)]
        
        return arr
    
    # =============== ACCESS ===============
    
    def get_element(self, arr, index):
        """
        Access element at specific index.
        Time Complexity: O(1) - direct memory address calculation
        Space Complexity: O(1) - no extra space needed
        """
        # Always check bounds to avoid errors!
        if index < 0 or index >= len(arr):
            raise IndexError(f"Index {index} out of bounds for array of length {len(arr)}")
        
        # Direct access by index - this is array's superpower!
        return arr[index]
    
    # =============== UPDATE ===============
    
    def set_element(self, arr, index, value):
        """
        Update element at specific index.
        Time Complexity: O(1) - direct memory access
        Space Complexity: O(1) - modifying in place
        """
        # Validate index
        if index < 0 or index >= len(arr):
            raise IndexError(f"Index {index} out of bounds")
        
        # Direct assignment - also O(1)
        arr[index] = value
        return arr
    
    # =============== SEARCH ===============
    
    def linear_search(self, arr, target):
        """
        Search for target value, return first index found.
        Time Complexity: O(n) - may need to check all elements
        Space Complexity: O(1) - only using index variable
        
        Real-world use: Finding a song in an unsorted playlist
        """
        # Must check each element sequentially
        for i in range(len(arr)):
            if arr[i] == target:
                return i  # Found! Return index
        
        return -1  # Not found (common convention)
    
    def find_all_occurrences(self, arr, target):
        """
        Find ALL indices where target appears.
        Time Complexity: O(n) - must check every element
        Space Complexity: O(k) - k is number of matches found
        """
        indices = []
        for i in range(len(arr)):
            if arr[i] == target:
                indices.append(i)
        
        return indices if indices else -1
    
    # =============== INSERT ===============
    
    def insert_at_end(self, arr, value):
        """
        Add element to end of array.
        Time Complexity: O(1) amortized - usually constant, occasionally O(n) to resize
        Space Complexity: O(1) - one new element
        
        Python lists handle resizing automatically!
        """
        arr.append(value)  # Efficient in Python
        return arr
    
    def insert_at_beginning(self, arr, value):
        """
        Add element to beginning of array.
        Time Complexity: O(n) - must shift all existing elements right
        Space Complexity: O(1) - just one new element
        
        Why O(n)? Every existing element must move one position right.
        """
        arr.insert(0, value)
        # Behind the scenes:
        # [1, 2, 3] → [_, 1, 2, 3] → [0, 1, 2, 3]
        # All elements shifted!
        return arr
    
    def insert_at_position(self, arr, index, value):
        """
        Insert element at specific position.
        Time Complexity: O(n) - must shift elements from index onwards
        Space Complexity: O(1) - one new element
        """
        if index < 0 or index > len(arr):
            raise IndexError(f"Index {index} out of bounds")
        
        arr.insert(index, value)
        # Elements at index and beyond shift right
        return arr
    
    # =============== DELETE ===============
    
    def delete_at_index(self, arr, index):
        """
        Remove element at specific index.
        Time Complexity: O(n) - must shift elements left to fill gap
        Space Complexity: O(1) - reducing size by one
        """
        if index < 0 or index >= len(arr):
            raise IndexError(f"Index {index} out of bounds")
        
        # Method 1: Using del
        del arr[index]
        
        # Method 2: Using pop (also returns the removed value)
        # removed_value = arr.pop(index)
        
        return arr
    
    def delete_by_value(self, arr, value):
        """
        Remove first occurrence of value.
        Time Complexity: O(n) - search O(n) + potential shift O(n)
        Space Complexity: O(1)
        """
        if value in arr:  # O(n) search
            arr.remove(value)  # O(n) removal and shift
            return arr
        return arr  # Value not found, no change
    
    # =============== ADVANCED OPERATIONS ===============
    
    def reverse_array(self, arr):
        """
        Reverse array in place using two pointers.
        Time Complexity: O(n) - swap n/2 pairs
        Space Complexity: O(1) - only two pointer variables
        
        Think Like a Programmer: Two pointers moving toward center
        is a classic pattern for many array problems!
        """
        left = 0
        right = len(arr) - 1
        
        while left < right:
            # Swap elements
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        
        return arr
    
    def find_max_min(self, arr):
        """
        Find maximum and minimum values in single pass.
        Time Complexity: O(n) - one traversal
        Space Complexity: O(1) - two variables
        """
        if not arr:
            return None, None
        
        max_val = arr[0]
        min_val = arr[0]
        
        # Single loop to find both
        for num in arr:
            if num > max_val:
                max_val = num
            if num < min_val:
                min_val = num
        
        return max_val, min_val
    
    def rotate_array(self, arr, k):
        """
        Rotate array right by k positions.
        Example: [1,2,3,4,5] rotated by 2 → [4,5,1,2,3]
        
        Time Complexity: O(n) - must move all elements
        Space Complexity: O(1) with reversal method
        
        Real-world use: Circular buffers, rotating carousel displays
        """
        if not arr or k == 0:
            return arr
        
        n = len(arr)
        k = k % n  # Handle k > n
        
        # Efficient method: Three reversals
        # [1,2,3,4,5], k=2
        # Step 1: Reverse all → [5,4,3,2,1]
        # Step 2: Reverse first k → [4,5,3,2,1]
        # Step 3: Reverse remaining → [4,5,1,2,3]
        
        def reverse(start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        
        reverse(0, n - 1)      # Reverse entire array
        reverse(0, k - 1)      # Reverse first k
        reverse(k, n - 1)      # Reverse remaining
        
        return arr


# ============================================
# PRACTICAL EXAMPLES
# ============================================

def example_grade_tracker():
    """Real-world example: Managing student grades"""
    print("=== Grade Tracker Example ===")
    
    # Initialize grades for 5 students
    grades = [85, 92, 78, 95, 88]
    students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    
    # Calculate class statistics
    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)
    
    print(f"Class Average: {average:.1f}")
    print(f"Highest Score: {highest}")
    print(f"Lowest Score: {lowest}")
    
    # Find who got the highest score
    top_student_idx = grades.index(highest)
    print(f"Top Student: {students[top_student_idx]} with {highest}")
    
    return grades

def example_temperature_tracker():
    """Real-world example: Weekly temperature tracking"""
    print("\n=== Temperature Tracker ===")
    
    # Store daily high temperatures (°F)
    temps = [72, 75, 68, 71, 74, 76, 73]
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    
    # Find warmest and coldest days
    warmest_temp = max(temps)
    coldest_temp = min(temps)
    warmest_day = days[temps.index(warmest_temp)]
    coldest_day = days[temps.index(coldest_temp)]
    
    print(f"Warmest Day: {warmest_day} ({warmest_temp}°F)")
    print(f"Coldest Day: {coldest_day} ({coldest_temp}°F)")
    
    # Calculate weekly average
    weekly_avg = sum(temps) / len(temps)
    print(f"Weekly Average: {weekly_avg:.1f}°F")
    
    return temps


# ============================================
# DEMO
# ============================================
if __name__ == "__main__":
    ops = ArrayOperations()
    
    # Create and manipulate array
    arr = ops.create_array(5, 0)
    print(f"Created array: {arr}")
    
    # Add some values
    for i in range(5):
        ops.set_element(arr, i, (i + 1) * 10)
    print(f"After adding values: {arr}")
    
    # Search
    index = ops.linear_search(arr, 30)
    print(f"Found 30 at index: {index}")
    
    # Run examples
    example_grade_tracker()
    example_temperature_tracker()
```

## Time and Space Complexity

| Operation | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Access by index | O(1) | O(1) | Direct memory calculation |
| Update by index | O(1) | O(1) | Direct memory write |
| Search (unsorted) | O(n) | O(1) | Must check each element |
| Search (sorted, binary) | O(log n) | O(1) | Can eliminate half each step |
| Insert at end | O(1)* | O(1) | *Amortized; occasional O(n) resize |
| Insert at beginning | O(n) | O(1) | Must shift all elements right |
| Insert at middle | O(n) | O(1) | Shift elements from insertion point |
| Delete at end | O(1) | O(1) | Just remove last element |
| Delete at beginning | O(n) | O(1) | Must shift all elements left |
| Delete at middle | O(n) | O(1) | Shift elements after deletion point |
| Find min/max | O(n) | O(1) | Must check all elements |
| Reverse | O(n) | O(1) | Swap n/2 pairs |
| Concatenate two arrays | O(n + m) | O(n + m) | Create new array with all elements |

**Understanding Amortized O(1):**
Dynamic arrays (like Python lists) occasionally need to resize. When full, they:
1. Allocate new larger memory (usually 2× current size)
2. Copy all elements to new location - O(n)
3. This happens rarely, so average (amortized) is still O(1)

## When to Use

✅ **Use arrays when:**
- You need fast access to elements by index (O(1) lookup)
- You know the approximate size in advance
- You're working with sequential data (temperatures, scores, stock prices)
- Memory locality matters (performance-critical code)
- You need to frequently iterate through all elements
- You're implementing other data structures (stacks, queues, heaps)

❌ **Don't use arrays when:**
- You need frequent insertions/deletions in the middle (O(n) cost)
- Size is highly unpredictable and changes often
- You need fast insertion at the beginning (use linked list instead)
- You need to maintain sorted order with frequent inserts (use binary search tree)
- You need fast lookup by key, not index (use hash table instead)

**Think Like a Programmer:** Arrays shine for static or sequential data with index-based access. Choose linked lists for frequent modifications, hash tables for key-based lookup, or trees for sorted operations.

## Common Pitfalls

### 1. **Index Out of Bounds**
One of the most common errors! Always validate indices before access.
```python
arr = [10, 20, 30]
# ❌ Wrong - crashes with IndexError
value = arr[5]  # Only indices 0-2 exist!

# ✓ Correct - check bounds first
if index >= 0 and index < len(arr):
    value = arr[index]
```

**Think Like a Programmer:** Remember: for an array of length `n`, valid indices are `0` to `n-1`, not `1` to `n`.

### 2. **Off-by-One Errors**
Forgetting that arrays start at index 0, not 1.
```python
arr = [10, 20, 30, 40, 50]

# ❌ Wrong - misses last element
for i in range(len(arr) - 1):  # Only goes 0-3, misses index 4!
    print(arr[i])

# ✓ Correct
for i in range(len(arr)):  # Goes 0-4, includes all elements
    print(arr[i])
```

### 3. **Modifying Array While Iterating**
Changing array size during iteration causes confusion.
```python
arr = [1, 2, 3, 4, 5]

# ❌ Wrong - indices shift during deletion
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        arr.pop(i)  # This shifts elements, breaking iteration!

# ✓ Correct - iterate backwards
for i in range(len(arr) - 1, -1, -1):
    if arr[i] % 2 == 0:
        arr.pop(i)

# ✓ Alternative - create new array
arr = [x for x in arr if x % 2 != 0]
```

### 4. **Shallow Copy vs Deep Copy**
Copying references instead of values in nested arrays.
```python
# ❌ Wrong - both variables point to same array
arr1 = [1, 2, 3]
arr2 = arr1
arr2[0] = 99
print(arr1)  # [99, 2, 3] - oops! arr1 changed too!

# ✓ Correct - create actual copy
arr2 = arr1.copy()  # or arr1[:]
arr2[0] = 99
print(arr1)  # [1, 2, 3] - arr1 unchanged ✓
```

### 5. **Assuming Unsorted Search is Fast**
Linear search in unsorted arrays is O(n), not O(1).
```python
# If you need frequent searches, consider:
# 1. Sort the array once, then use binary search: O(log n)
# 2. Use a hash set for O(1) lookups
# 3. Use a hash map for key-value lookups

large_array = list(range(1000000))

# Slow for many searches
def slow_search(value):
    return value in large_array  # O(n) each time!

# Better if sorted
large_array.sort()  # One-time O(n log n) cost
def fast_search(value):
    # Binary search - O(log n)
    import bisect
    idx = bisect.bisect_left(large_array, value)
    return idx < len(large_array) and large_array[idx] == value
```

## Practice Problems
See the problem directories for practice challenges:
- [Problem 1](./problem-1/problem1.md) - Basic array operations
- [Problem 2](./problem-2/problem2.md) - Array searching
- [Problem 3](./problem-3/problem3.md) - Array manipulation
- [Problem 4](./problem-4/problem4.md) - Two-pointer techniques
- [Problem 5](./problem-5/problem5.md) - Array rotation and shifting
- [Problem 6](./problem-6/problem6.md) - Advanced array algorithms

## Additional Resources
- [Python List Documentation](https://docs.python.org/3/tutorial/datastructures.html) - Official Python list guide
- [Visualgo: Array Visualization](https://visualgo.net/en/array) - Interactive array operations visualizer
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/) - Complexity reference for all data structures
- [Python Tutor](http://pythontutor.com/) - Step through array operations visually
- [Module 00: Foundations](../00-foundations/) - Review Big-O notation and complexity analysis

---

**Next Steps:** Once you're comfortable with arrays, explore [Linked Lists](../linked-lists/) to see how dynamic data structures handle frequent insertions and deletions more efficiently!
