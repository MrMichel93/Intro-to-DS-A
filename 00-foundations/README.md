# Module 0: Foundations

Welcome to the foundation module! Before diving into data structures and algorithms, let's make sure we have a solid understanding of the fundamental programming concepts you'll need.

## What You'll Learn

This module covers the essential programming concepts that will help you succeed in this course:

- **Variables and Data Types** - Understanding how computers store and manage data
- **Functions** - Breaking down problems into reusable pieces
- **Loops and Iteration** - Repeating actions efficiently
- **Conditional Logic** - Making decisions in code
- **Time and Space Complexity** - Understanding algorithm efficiency
- **Problem-Solving Approach** - Breaking down complex problems

## Prerequisites

Before starting this course, you should be comfortable with:
- ✅ Basic Python syntax (or willingness to learn)
- ✅ Running Python programs on your computer
- ✅ Using a text editor or IDE
- ✅ Basic command line navigation

**Don't worry if you're not an expert!** This module will review the essentials.

## 1. Variables and Data Types

### What are Variables?

Variables are named containers that store data. Think of them as labeled boxes where you can put different types of information.

```python
# Numbers
age = 18
price = 19.99

# Strings (text)
name = "Alice"
message = "Hello, World!"

# Booleans (True/False)
is_student = True
has_license = False

# Collections
scores = [95, 87, 92, 88]  # List
coordinates = (10, 20)      # Tuple
student_info = {"name": "Bob", "age": 19}  # Dictionary
```

### Why This Matters for Data Structures

Different data types have different performance characteristics:
- Accessing an item in a list: Fast
- Checking if an item exists in a list: Slow
- Checking if a key exists in a dictionary: Fast

Understanding these differences is the foundation of choosing the right data structure!

## 2. Functions

Functions are reusable blocks of code that perform specific tasks.

```python
def greet(name):
    """Returns a greeting message"""
    return f"Hello, {name}!"

def add_numbers(a, b):
    """Adds two numbers and returns the result"""
    return a + b

# Using functions
message = greet("Alice")
sum_result = add_numbers(5, 3)
```

### Why This Matters

Throughout this course, you'll implement functions that work with data structures:
```python
def find_max(array):
    """Find the maximum value in an array"""
    # Your implementation here
    pass
```

## 3. Loops and Iteration

Loops let you repeat actions without writing the same code multiple times.

### For Loops
```python
# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop with range
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# Loop with index and value
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

### While Loops
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### Why This Matters

Most algorithms involve iterating through data structures:
- Searching for an element
- Sorting items
- Processing each node in a tree

## 4. Conditional Logic

Conditionals let your program make decisions.

```python
def check_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def is_even(number):
    return number % 2 == 0
```

### Common Patterns
```python
# Check if variable exists and has value
if data and len(data) > 0:
    process(data)

# Guard clauses (early returns)
def divide(a, b):
    if b == 0:
        return None  # Handle error case first
    return a / b
```

## 5. Time and Space Complexity (Big O Notation)

This is **crucial** for understanding data structures and algorithms!

### What is Time Complexity?

Time complexity describes how the runtime of an algorithm grows as the input size increases.

#### Common Complexities (from fastest to slowest):

**O(1) - Constant Time**
```
Runtime doesn't depend on input size
Example: Accessing array[5]

Time
  |     _______________
  |    /
  |___/
      Input Size →
```

**O(log n) - Logarithmic Time**
```
Runtime grows slowly, even with large inputs
Example: Binary search

Time
  |         ___---
  |     __--
  |  __/
  |_/
      Input Size →
```

**O(n) - Linear Time**
```
Runtime grows directly with input size
Example: Finding max in unsorted array

Time
  |        /
  |      /
  |    /
  |  /
  |/
      Input Size →
```

**O(n log n) - Linearithmic Time**
```
Example: Efficient sorting algorithms (merge sort, quicksort)

Time
  |         __---
  |      _-/
  |   _-/
  | _/
  |/
      Input Size →
```

**O(n²) - Quadratic Time**
```
Runtime grows with square of input
Example: Nested loops, bubble sort

Time
  |         |
  |        /
  |      /
  |    /
  |  /
  |/
      Input Size →
```

**O(2ⁿ) - Exponential Time**
```
Runtime doubles with each input increase
Example: Recursive fibonacci (naive)
⚠️ Usually too slow for large inputs!

Time
  |         |
  |        |
  |       |
  |     /
  |   /
  |__/
      Input Size →
```

### Space Complexity

Space complexity describes how much memory an algorithm uses.

```python
# O(1) space - uses fixed amount of memory
def sum_array(arr):
    total = 0  # Only one variable
    for num in arr:
        total += num
    return total

# O(n) space - creates new array of size n
def double_array(arr):
    result = []  # New array grows with input
    for num in arr:
        result.append(num * 2)
    return result
```

### Why This Matters

When comparing algorithms, we need a way to measure efficiency:
- Which sorting algorithm is faster?
- Does this use too much memory?
- Will this work with 1 million items?

Big O notation gives us the answer!

## 6. Problem-Solving Approach

Here's a systematic approach to solving coding problems:

### Step 1: Understand the Problem
- Read carefully
- Identify inputs and outputs
- Ask clarifying questions
- Consider edge cases

### Step 2: Plan Your Solution
- Think before coding!
- Draw diagrams
- Consider different approaches
- Think about time/space complexity

### Step 3: Write Pseudocode
```
FUNCTION find_max(array):
    IF array is empty:
        RETURN None
    
    SET max to first element
    FOR EACH element in array:
        IF element > max:
            SET max to element
    
    RETURN max
```

### Step 4: Implement
- Start with a simple solution that works
- Test with examples
- Handle edge cases

### Step 5: Optimize
- Can you make it faster?
- Can you use less memory?
- Is the code readable?

### Example: Two Sum Problem

**Problem**: Given an array of integers, find two numbers that add up to a target.

**Approach 1: Brute Force** - O(n²)
```python
def two_sum_slow(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None
```

**Approach 2: Using Hash Table** - O(n)
```python
def two_sum_fast(nums, target):
    seen = {}  # Store: number -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None
```

**Key Insight**: By using a hash table (dictionary), we trade space for time!

## 7. Common Patterns You'll See

### Pattern 1: Two Pointers
```python
def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
```

### Pattern 2: Sliding Window
```python
def max_sum_subarray(arr, k):
    """Find max sum of k consecutive elements"""
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

### Pattern 3: Frequency Counter
```python
def find_duplicates(arr):
    """Find duplicate elements"""
    counts = {}
    for num in arr:
        counts[num] = counts.get(num, 0) + 1
    
    return [num for num, count in counts.items() if count > 1]
```

## Visual Learning

Throughout this course, you'll see ASCII diagrams like these to help visualize concepts:

```
Array visualization:
Index: 0   1   2   3   4
Value: [10][20][30][40][50]
        ↑
     Element at index 0

Linked List visualization:
[10|•]→[20|•]→[30|•]→[40|null]
  ↑                      ↑
 head                   tail

Stack visualization (LIFO):
  push(5) →  [5]
  push(3) →  [3]
             [5]
  pop() →    [5]  (removed 3)
```

See the [visualizations](./visualizations/) folder for more examples!

## Practice Before Moving On

Before diving into the main modules, make sure you can:

✅ Write a function that takes parameters and returns a value  
✅ Use for loops to iterate through a list  
✅ Use if/else statements to make decisions  
✅ Understand what O(n) vs O(n²) means  
✅ Use a dictionary to store key-value pairs  
✅ Debug your code when something goes wrong  

## Next Steps

Once you're comfortable with these concepts, you're ready to start with **Module 1: [Arrays](../arrays/)**!

Arrays are the simplest data structure and a perfect place to begin applying what you've learned here.

## Additional Resources

- [Python Official Tutorial](https://docs.python.org/3/tutorial/) - Comprehensive Python guide
- [Python Tutor](http://pythontutor.com/) - Visualize code execution step-by-step
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/) - Quick reference for complexity

---

💡 **Remember**: Everyone starts as a beginner. The key is consistent practice and not being afraid to make mistakes. That's how we learn!
