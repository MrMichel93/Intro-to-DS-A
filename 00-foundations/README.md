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

## What Are Data Structures?

### Definition

A **data structure** is a specialized way of organizing, storing, and managing data in a computer so that it can be accessed and modified efficiently. Think of data structures as different types of containers, each designed for specific purposes and operations.

Just like how you wouldn't store books the same way you store tools or kitchen utensils, different types of data need different organizational systems.

### Why Data Structures Matter

Choosing the right data structure can make the difference between a program that runs in seconds versus one that takes hours! Here are real-world examples:

1. **Social Media Friend Lists**: When you view someone's friend list, the system needs to quickly retrieve hundreds or thousands of names. A data structure optimized for fast lookup makes this instant.

2. **GPS Navigation**: Finding the shortest route between two locations requires analyzing thousands of possible paths. Graph data structures make this calculation possible in real-time.

3. **Autocomplete Search**: When you type in a search box, the system needs to suggest completions from millions of possibilities. Specialized tree structures (like tries) make this happen as you type.

4. **Undo/Redo in Applications**: Text editors and design tools need to track your history of changes. Stack data structures make it easy to go backward and forward through your actions.

### The Analogy: Physical Organization

Think about organizing physical objects in your life:

**Toolbox**: Tools are organized by type in different compartments. You know exactly where to find what you need. Similar to how **arrays** organize data by position.

**Library**: Books are cataloged and shelved by category, author, or ID number. You can look up a book in the catalog and go directly to it. Similar to how **hash tables** provide fast lookups by key.

**Kitchen**: Plates are **stacked** (you take from the top), while a line at the cafeteria is a **queue** (first person in line is served first). These physical arrangements mirror the stack and queue data structures.

The key insight: **The way you organize things affects how efficiently you can use them!**

## What Are Algorithms?

### Definition

An **algorithm** is a step-by-step set of instructions for solving a problem or completing a task. It's like a recipe that tells the computer exactly what to do, in what order, to achieve a specific goal.

Every time you write code to solve a problem, you're creating an algorithm!

### Algorithm vs Program

- **Algorithm**: The abstract idea or strategy (the steps to solve a problem)
- **Program**: The implementation of that algorithm in a specific programming language

**Example**: 
- Algorithm: "To find the largest number, check each number and keep track of the biggest one you've seen"
- Program: The actual Python code with loops and variables that implements this strategy

### The Recipe Analogy

Think of making chocolate chip cookies:

```
RECIPE (Algorithm):
1. Preheat oven to 350°F
2. Mix butter and sugar until creamy
3. Add eggs and vanilla, mix well
4. In separate bowl, combine flour, baking soda, salt
5. Gradually blend dry ingredients into wet mixture
6. Stir in chocolate chips
7. Drop spoonfuls onto baking sheet
8. Bake for 10-12 minutes
```

Notice how a recipe is:
- **Precise**: Each step is clearly defined
- **Ordered**: Steps must be done in sequence
- **Finite**: It eventually ends (with delicious cookies!)
- **Effective**: Following the steps produces the desired result

Just like how different recipes can make cookies (some faster, some tastier), different algorithms can solve the same problem in different ways!

### The Importance of Efficiency

Not all algorithms are created equal. Consider two ways to find a name in a phone book:

**Algorithm 1**: Start at the beginning and check every single name until you find the right one.
**Algorithm 2**: Open to the middle, determine if the name is in the first or second half, repeat until found.

Both algorithms work, but Algorithm 2 (binary search) is **much** faster for large phone books. For a phone book with 1,000 names:
- Algorithm 1: Might check all 1,000 names (worst case)
- Algorithm 2: Checks only about 10 names (worst case)

This is why studying algorithms matters – **efficiency scales**! The difference between good and bad algorithms becomes massive as data grows.

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

## 5. Big-O Notation (Time Complexity)

This is **crucial** for understanding data structures and algorithms!

### Why We Measure Efficiency

Imagine you write a program that works perfectly with 10 items. But what happens when your user has 1,000 items? Or 1,000,000? Will your program still run quickly, or will it grind to a halt?

Big-O notation helps us answer these questions by describing how an algorithm's performance scales with input size.

### Operations vs Seconds

Here's a critical insight: We don't measure algorithms in **seconds** or **milliseconds**. Why? Because:
- Different computers run at different speeds
- The same computer might be faster or slower depending on what else is running
- Future computers will be faster than today's computers

Instead, we count **operations** – the basic steps an algorithm performs. This gives us a measurement that works across all computers and all time periods.

**Example**: If an algorithm checks each item in a list once, that's **n operations** (where n is the list size), regardless of whether it takes 1 second or 0.001 seconds on your computer.

### What is Time Complexity?

Time complexity describes how the number of operations grows as the input size increases. Big-O notation expresses this growth rate, focusing on what happens with large inputs and ignoring constant factors.

### Common Time Complexities

From fastest to slowest:

#### **O(1) - Constant Time**

**The operation takes the same time regardless of input size.**

Example: Accessing an array element by index
```python
def get_first_element(arr):
    return arr[0]  # Always 1 operation

# Works the same for 10 items or 10 million items!
```

**Real-world analogy**: Looking up a word in a dictionary when someone tells you the exact page number.

#### **O(log n) - Logarithmic Time**

**The operation time increases slowly as input grows. Each step eliminates a large portion of remaining data.**

Example: Binary search in a sorted array
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# For 1,000 items: ~10 operations
# For 1,000,000 items: ~20 operations
```

**Real-world analogy**: Finding a word in a dictionary by opening to the middle, then middle of the correct half, etc.

#### **O(n) - Linear Time**

**The operation time grows directly proportional to input size.**

Example: Finding the maximum in an unsorted array
```python
def find_max(arr):
    max_val = arr[0]
    for num in arr:  # Must check every element
        if num > max_val:
            max_val = num
    return max_val

# For 1,000 items: 1,000 operations
# For 1,000,000 items: 1,000,000 operations
```

**Real-world analogy**: Reading every page of a book to find a specific quote.

#### **O(n log n) - Linearithmic Time**

**More than linear but less than quadratic. Common in efficient sorting algorithms.**

Example: Merge sort, quicksort (average case)
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])    # Divide
    right = merge_sort(arr[mid:])   # Divide
    
    return merge(left, right)       # Conquer

# Divides data log n times, processes n items at each level
```

**Real-world analogy**: Organizing a deck of cards by repeatedly splitting and merging piles.

#### **O(n²) - Quadratic Time**

**The operation time grows with the square of input size. Often involves nested loops.**

Example: Bubble sort, checking all pairs
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):           # Loop 1: n times
        for j in range(n - i - 1):  # Loop 2: n times
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# For 1,000 items: 1,000,000 operations
# For 1,000,000 items: 1,000,000,000,000 operations (1 trillion!)
```

**Real-world analogy**: Comparing every person in a room with every other person (handshakes problem).

#### **O(2ⁿ) - Exponential Time**

**The operation time doubles with each additional input element. Usually impractical for large inputs.**

Example: Recursive Fibonacci (naive implementation)
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# For n = 10: 1,024 operations
# For n = 20: 1,048,576 operations
# For n = 30: 1,073,741,824 operations (over 1 billion!)
```

**Real-world analogy**: Each decision branches into two more decisions, creating exponential growth.

⚠️ **Warning**: Exponential algorithms are rarely practical for n > 30!

### Growth Rate Comparison (ASCII Graph)

```
Operations
    |
10⁹ |                                                            * O(2ⁿ)
    |                                                        *
    |                                                    *
10⁶ |                                               *    |
    |                                           *        |
    |                                       *            * O(n²)
10³ |                                  *                /
    |                              *               *   /
    |                          *               *   | /
    |                      *              *    | / * O(n log n)
100 |                  *             *      |/  *
    |              *            *       * / * O(n)
    |          *           *       *  /  *
10  |      *          *        * /   *
    |  *        *  *       *  / * O(log n)
1   |*____*__*___*___*__*_*_O(1)
    |___|____|____|____|____|____|____|____|____|____
      1   5   10   20   50  100  200  500  1K  10K  (Input Size n)

Legend:
* O(1)       - Flat line (best!)
* O(log n)   - Grows very slowly
* O(n)       - Straight diagonal line
* O(n log n) - Slightly curved
* O(n²)      - Steep curve (avoid for large n!)
* O(2ⁿ)      - Shoots up vertically (rarely practical!)
```

### Practical Impact: Real Numbers

Let's say 1 operation = 1 microsecond (1/1,000,000 second):

| Algorithm | n=10 | n=100 | n=1,000 | n=10,000 | n=100,000 |
|-----------|------|-------|---------|----------|-----------|
| O(1)      | 1 μs | 1 μs  | 1 μs    | 1 μs     | 1 μs      |
| O(log n)  | 3 μs | 7 μs  | 10 μs   | 13 μs    | 17 μs     |
| O(n)      | 10 μs | 100 μs | 1 ms   | 10 ms    | 100 ms    |
| O(n log n)| 30 μs | 700 μs | 10 ms  | 130 ms   | 1.7 s     |
| O(n²)     | 100 μs | 10 ms | 1 s    | 1.7 min  | 2.8 hours |
| O(2ⁿ)     | 1 ms | **∞** | **∞**  | **∞**    | **∞**     |

**∞** = Would take longer than the age of the universe!

### Key Takeaways

1. **Constants don't matter**: O(5n) = O(n), O(100) = O(1)
2. **Smaller terms are dropped**: O(n² + n) = O(n²)
3. **Focus on worst case**: Usually what we analyze
4. **Scale matters**: O(n²) is fine for n=100, terrible for n=100,000

## 6. Space Complexity

Time isn't the only resource that matters – **memory usage** is also critical!

### Why Memory Usage Matters

Imagine you're processing data on a smartphone with limited RAM, or handling millions of records in a web application. An algorithm that uses too much memory might:
- Crash your program (out of memory error)
- Slow down your computer (swapping to disk)
- Cost more money (cloud computing charges for memory)
- Prevent your app from running on lower-end devices

### What is Space Complexity?

Space complexity measures how much memory an algorithm uses relative to the input size. Like time complexity, we use Big-O notation.

### Common Space Complexities

#### **O(1) - Constant Space**

Uses a fixed amount of memory regardless of input size.

```python
def sum_array(arr):
    total = 0  # Only one variable
    for num in arr:
        total += num
    return total

# Memory used: One integer variable
# Same memory for 10 items or 10 million items!
```

#### **O(n) - Linear Space**

Memory usage grows proportionally with input size.

```python
def copy_array(arr):
    result = []
    for num in arr:
        result.append(num)
    return result

# Memory used: New array of size n
# 1,000 items → 1,000 units of memory
# 1,000,000 items → 1,000,000 units of memory
```

#### **O(log n) - Logarithmic Space**

Common in divide-and-conquer algorithms (recursion depth).

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

# Each recursive call adds to the call stack
# Maximum depth: log n levels
```

#### **O(n²) - Quadratic Space**

Memory grows with the square of input size (often 2D arrays).

```python
def create_multiplication_table(n):
    table = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(i * j)
        table.append(row)
    return table

# Creates n × n grid
# n=100 → 10,000 cells
# n=1,000 → 1,000,000 cells
```

### Time vs Space Trade-offs

Often, you can trade memory for speed (or vice versa). There's rarely a perfect solution – just different trade-offs!

#### Example: Fibonacci Sequence

**Approach 1: Recursive (Simple but Slow and Redundant)**
```python
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# Time: O(2ⁿ) - exponential!
# Space: O(n) - recursion depth
# Problem: Recalculates same values many times
```

**Approach 2: Memoization (Faster, Uses More Memory)**
```python
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

# Time: O(n) - each value calculated once
# Space: O(n) - stores all values
# Trade-off: Uses more memory for much better speed
```

**Approach 3: Iterative (Fast and Memory Efficient)**
```python
def fib_iterative(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

# Time: O(n) - single loop
# Space: O(1) - only two variables
# Best of both worlds!
```

### Making the Right Choice

Consider both time AND space when choosing an algorithm:

| Scenario | Priority | Example |
|----------|----------|---------|
| Mobile app | Space (limited RAM) | Choose O(1) space when possible |
| Real-time system | Time (must be fast) | Accept O(n) space for O(1) time |
| Big data processing | Both matter | Look for O(n log n) time, O(log n) space |
| Small datasets | Neither matters much | Prioritize code clarity |

**Remember**: Premature optimization is the root of all evil! Write clear code first, optimize only if needed.

## 7. How to Analyze Algorithms

Let's develop a systematic approach to analyzing any algorithm's complexity.

### Step 1: Count Operations

Look at your code and count how many basic operations it performs:
- Arithmetic (+, -, *, /)
- Comparisons (<, >, ==)
- Array access (arr[i])
- Variable assignments

### Step 2: Express in Terms of Input Size

Use **n** to represent input size. Count operations as a function of n.

### Step 3: Focus on Dominant Terms

Drop constants and lower-order terms. Keep only the term that grows fastest.

### Detailed Example 1: Simple Search

```python
def find_max(arr):
    """Find the maximum value in an array"""
    if len(arr) == 0:           # 1 comparison
        return None             # 1 return
    
    max_val = arr[0]            # 1 array access, 1 assignment
    
    for i in range(1, len(arr)): # Loop: (n-1) times
        if arr[i] > max_val:     # 2 operations per iteration
            max_val = arr[i]     # 1 operation per update (worst case)
    
    return max_val              # 1 return
```

**Analysis**:
- Setup: 3 operations (constant)
- Loop: runs (n-1) times
- Per iteration: ~3 operations
- Total: 3 + 3(n-1) = 3 + 3n - 3 = 3n

**Big-O**: Drop constant → **O(n)**

### Detailed Example 2: Nested Loops

```python
def print_pairs(arr):
    """Print all pairs of elements"""
    for i in range(len(arr)):      # Outer loop: n times
        for j in range(len(arr)):  # Inner loop: n times
            print(arr[i], arr[j])  # 2 accesses + 1 print = 3 operations
```

**Analysis**:
- Outer loop: n iterations
- For each outer iteration, inner loop: n iterations
- Total iterations: n × n = n²
- Operations per iteration: 3
- Total: 3n²

**Big-O**: Drop constant → **O(n²)**

### Detailed Example 3: Logarithmic Algorithm

```python
def binary_search(arr, target):
    """Search sorted array by repeatedly halving search space"""
    left, right = 0, len(arr) - 1   # 2 assignments
    
    while left <= right:             # Loop: ? times
        mid = (left + right) // 2    # 3 operations
        if arr[mid] == target:       # 2 operations
            return mid
        elif arr[mid] < target:      # 1 operation
            left = mid + 1           # 2 operations
        else:
            right = mid - 1          # 2 operations
    
    return -1
```

**Analysis**:
- Each iteration cuts search space in half
- Start: n elements
- After 1 iteration: n/2 elements
- After 2 iterations: n/4 elements
- After k iterations: n/(2^k) elements
- Stop when: n/(2^k) = 1 → k = log₂(n)

**Big-O**: **O(log n)**

### Best, Average, and Worst Case

The same algorithm can have different performance depending on the input!

#### Example: Linear Search

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

**Best Case**: Target is first element → **O(1)**
- Only 1 comparison needed
- Example: searching for 5 in [5, 3, 7, 1]

**Average Case**: Target is somewhere in the middle → **O(n/2) = O(n)**
- On average, check half the elements
- Example: searching for 7 in [5, 3, 7, 1]

**Worst Case**: Target is last element or not present → **O(n)**
- Must check every element
- Example: searching for 1 in [5, 3, 7, 1] or searching for 9 (not present)

**Convention**: When we say "time complexity" without qualification, we usually mean **worst case**.

### Step-by-Step Analysis Checklist

When analyzing any algorithm:

1. ✅ **Identify the input size** - What is n? (array length, number of nodes, etc.)
2. ✅ **Count loop iterations** - How many times does each loop run?
3. ✅ **Check for nested loops** - Multiply iterations of nested loops
4. ✅ **Look for recursive calls** - Each call adds to complexity
5. ✅ **Check for early exits** - Can the algorithm stop early?
6. ✅ **Consider space usage** - What data structures are created?
7. ✅ **Express as formula** - Write total operations as function of n
8. ✅ **Simplify to Big-O** - Drop constants and lower-order terms

### Practice Analysis

Let's analyze this together:

```python
def has_duplicates(arr):
    """Check if array has any duplicate values"""
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False
```

**Your turn to analyze**:
- How many times does the outer loop run?
- How many times does the inner loop run?
- Best case scenario?
- Worst case scenario?

**Answer**:
- Outer loop: n times
- Inner loop: (n-1) + (n-2) + ... + 1 = n(n-1)/2 times total
- Best case: O(1) - first two elements are duplicates
- Worst case: O(n²) - no duplicates, checks all pairs
- Time complexity: **O(n²)**

## 8. Problem-Solving Framework

This systematic approach will help you tackle any coding problem. **Reference this framework in every module** – it's your roadmap to success!

### Step 1: Understand the Problem

Don't rush to code! Make sure you fully understand what's being asked.

**Ask yourself**:
- What are the inputs? What are their types and constraints?
- What is the expected output?
- What should happen with edge cases (empty input, single element, very large input)?
- Are there any special conditions or requirements?

**Example Questions**:
- "Can the array be empty?"
- "Are the numbers always positive?"
- "What should I return if no solution exists?"
- "Does order matter in the output?"

**Technique**: Restate the problem in your own words. Work through 2-3 examples by hand.

### Step 2: Plan Your Approach

Think before you type! Consider multiple approaches.

**Planning techniques**:
- **Draw it out**: Visualize the problem with diagrams or examples
- **Identify patterns**: Does this remind you of a problem you've seen?
- **Break it down**: Can you split this into smaller sub-problems?
- **Consider data structures**: Would an array, hash table, stack, or queue help?
- **Think about complexity**: What time/space complexity can you achieve?

**Example - Finding Duplicates**:
```
Input: [1, 3, 2, 1, 4]
Output: True (1 appears twice)

Approach 1: Compare each pair - O(n²) time, O(1) space
Approach 2: Sort then check adjacent - O(n log n) time, O(1) space
Approach 3: Use hash set to track seen values - O(n) time, O(n) space
```

### Step 3: Write Pseudocode (Optional but Recommended)

Before writing actual code, sketch out the logic in plain English or simplified syntax.

```
FUNCTION find_duplicates(array):
    CREATE empty set called 'seen'
    
    FOR EACH number in array:
        IF number is in 'seen':
            RETURN True
        ADD number to 'seen'
    
    RETURN False
```

**Benefits**:
- Clarifies your thinking
- Easier to spot logic errors
- Language-agnostic (works in any programming language)

### Step 4: Implement

Now write the actual code! Start simple.

**Implementation tips**:
- **Start with a brute force solution** that works, even if it's slow
- **Write clean, readable code** - you can optimize later
- **Add comments** for complex logic
- **Use meaningful variable names** (not just `x`, `y`, `z`)
- **Handle edge cases** from the start

```python
def find_duplicates(arr):
    """
    Check if array contains any duplicate values.
    
    Args:
        arr: List of integers
        
    Returns:
        Boolean: True if duplicates exist, False otherwise
    """
    # Edge case: empty or single-element array
    if len(arr) <= 1:
        return False
    
    seen = set()
    
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    
    return False
```

### Step 5: Test

Test your solution with various inputs before declaring victory!

**Test categories**:
1. **Normal cases**: Typical expected inputs
2. **Edge cases**: Empty, single element, very large inputs
3. **Corner cases**: Special conditions specific to the problem
4. **Invalid inputs**: What if assumptions are violated?

**Example test cases for find_duplicates**:
```python
# Normal cases
assert find_duplicates([1, 2, 3, 1]) == True
assert find_duplicates([1, 2, 3, 4]) == False

# Edge cases
assert find_duplicates([]) == False      # Empty array
assert find_duplicates([1]) == False    # Single element
assert find_duplicates([1, 1]) == True  # Two elements, duplicate

# Corner cases
assert find_duplicates([1, 2, 3, 4, 5, 1]) == True  # Duplicate at end
assert find_duplicates([0, 0]) == True              # Zero values
```

### Step 6: Optimize

Only after your solution works should you consider optimization.

**Questions to ask**:
- ✅ Can I reduce time complexity? (fewer operations)
- ✅ Can I reduce space complexity? (less memory)
- ✅ Can I simplify the code? (more readable)
- ✅ Are there redundant operations?
- ✅ Can I exit early in some cases?

**Optimization example - Two Sum**:

**Approach 1: Brute Force - O(n²) time, O(1) space**
```python
def two_sum_v1(nums, target):
    """Check every pair of numbers"""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None
```

**Approach 2: Hash Table - O(n) time, O(n) space**
```python
def two_sum_v2(nums, target):
    """Store seen numbers for instant lookup"""
    seen = {}  # number -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None
```

**Key Insight**: We traded O(n) space for O(n) time improvement – went from O(n²) to O(n)!

### Complete Example: Problem-Solving Framework in Action

**Problem**: Given an array of integers, return the indices of two numbers that sum to a specific target.

**Step 1: Understand**
- Input: Array of integers + target sum
- Output: Two indices [i, j] where nums[i] + nums[j] = target
- Assumptions: Exactly one solution exists, can't use same element twice

**Step 2: Plan**
```
Example: nums = [2, 7, 11, 15], target = 9
Answer: [0, 1] because nums[0] + nums[1] = 2 + 7 = 9

Approach ideas:
1. Brute force: Try all pairs → O(n²)
2. Hash table: Store complements as we go → O(n)
Let's go with approach 2!
```

**Step 3: Pseudocode**
```
FUNCTION two_sum(nums, target):
    CREATE hash table 'seen'
    
    FOR index, number in nums:
        complement = target - number
        IF complement exists in 'seen':
            RETURN [seen[complement], index]
        STORE number->index in 'seen'
    
    RETURN None
```

**Step 4: Implement**
```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None
```

**Step 5: Test**
```python
assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 2, 4], 6) == [1, 2]
assert two_sum([3, 3], 6) == [0, 1]
```

**Step 6: Optimize**
- Time: O(n) - already optimal!
- Space: O(n) - necessary for hash table
- Code is clean and readable ✓

### The Framework in Practice

**Throughout this course**, you'll see problems that reference this framework:

```
💡 Problem-Solving Tip: Start by understanding the problem. 
   What are the inputs and outputs? What edge cases exist?
```

```
💡 Problem-Solving Tip: Before coding, plan your approach. 
   Can you draw this out? What data structure would help?
```

```
💡 Problem-Solving Tip: Test with edge cases!
   What happens with an empty array? A single element?
```

**Remember**: This framework isn't bureaucracy – it's a tool to help you think clearly and avoid mistakes. Use it every time you solve a problem, and it will become second nature!

## 9. Common Patterns You'll See

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
