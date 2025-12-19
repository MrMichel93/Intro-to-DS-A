# Module 0: Foundations - Answer Key

**Total Points:** 100

---

## Part 1: Multiple Choice Questions (40 points, 4 points each)

### Question 1: **B**
What does Big O notation describe?
- **Answer: B) The upper bound of an algorithm's growth rate as input size increases**
- Explanation: Big O notation describes the worst-case growth rate of an algorithm's time or space requirements as the input size increases.

### Question 2: **D**
Which of the following represents the best time complexity?
- **Answer: D) O(1)**
- Explanation: O(1) is constant time - the best possible complexity. From best to worst: O(1) < O(log n) < O(n) < O(n log n) < O(n²)

### Question 3: **C**
An algorithm that checks every element in an array once has a time complexity of:
- **Answer: C) O(n)**
- Explanation: Checking each element once is linear time, proportional to the input size n.

### Question 4: **C**
What is the space complexity of an algorithm that creates a new array of size n?
- **Answer: C) O(n)**
- Explanation: Creating a new array of size n requires O(n) space.

### Question 5: **D**
Which growth rate is fastest for large values of n?
- **Answer: D) O(2^n)**
- Explanation: Exponential growth O(2^n) is the fastest (worst) among the options: O(log n) < O(n) < O(n log n) < O(2^n)

### Question 6: **B**
What does it mean when we say an algorithm has O(1) space complexity?
- **Answer: B) It uses a constant amount of memory regardless of input size**
- Explanation: O(1) space means the memory usage doesn't grow with input size.

### Question 7: **C**
If an algorithm has nested loops where each iterates n times, what is its time complexity?
- **Answer: C) O(n²)**
- Explanation: Nested loops multiply: n iterations × n iterations = n² operations.

### Question 8: **B**
Binary search on a sorted array has a time complexity of:
- **Answer: B) O(log n)**
- Explanation: Binary search halves the search space each iteration, resulting in logarithmic time.

### Question 9: **B**
Which of the following best describes a good problem-solving approach?
- **Answer: B) Understand the problem, plan your approach, then implement**
- Explanation: Always understand requirements, plan your solution, then code and test.

### Question 10: **A**
What is the time complexity of accessing an element in an array by index?
- **Answer: A) O(1)**
- Explanation: Array access by index is constant time due to direct memory addressing.

---

## Part 2: Code Analysis Questions (30 points, 10 points each)

### Question 11 (10 points)
```python
def find_duplicates(arr):
    duplicates = []
    seen = set()
    
    for num in arr:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)
    
    return duplicates
```

**Answer:**
- Time Complexity: **O(n)**
- Space Complexity: **O(n)**
- Explanation: The function iterates through the array once (O(n) time). Set lookups and insertions are O(1) on average. The `seen` set can grow to size n in the worst case, and the duplicates list can also be O(n), giving O(n) space complexity.

### Question 12 (10 points)
```python
def mystery_function(n):
    result = 0
    i = 1
    while i < n:
        result += i
        i = i * 2
    return result

print(mystery_function(10))
```

**Answer:**
- Output: **15**
- Trace of execution:
  - i = 1, result = 0 + 1 = 1, i becomes 2
  - i = 2, result = 1 + 2 = 3, i becomes 4
  - i = 4, result = 3 + 4 = 7, i becomes 8
  - i = 8, result = 7 + 8 = 15, i becomes 16
  - i = 16 >= 10, loop exits
  - The function sums powers of 2 less than n: 1 + 2 + 4 + 8 = 15

### Question 13 (10 points)
```python
def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return average
```

**Answer:**
- Issues: **The function will crash with a ZeroDivisionError if the input list is empty** (division by zero when len(numbers) == 0).
- Fixed code:
```python
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0  # or return None, or raise an exception
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return average
```

---

## Part 3: Short Answer Questions (30 points, 15 points each)

### Question 14 (15 points)
Explain the difference between time complexity and space complexity.

**Sample Answer:**
Time complexity measures how the number of operations grows as input size increases, while space complexity measures how memory usage grows. For example, an algorithm that creates a copy of an input array has O(n) space complexity but might have different time complexity depending on what it does. An algorithm that sorts an array in-place using bubble sort has O(1) space complexity (good) but O(n²) time complexity (poor). Conversely, merge sort has O(n log n) time complexity (good) but O(n) space complexity because it creates temporary arrays. The trade-off between time and space is common in algorithm design - sometimes we use more memory to achieve faster execution.

**Grading Rubric:**
- 5 points: Clear definition of time complexity
- 5 points: Clear definition of space complexity
- 5 points: Valid example showing the trade-off

### Question 15 (15 points)
You need to store user IDs and quickly check if a user ID exists. Which data structure to choose?

**Sample Answer:**
I would choose Option C: Store IDs in a hash table (set). Option A (unsorted array) requires O(n) lookup time because you must check every element. Option B (sorted array) allows binary search with O(log n) lookup, which is better but still not optimal. A hash table provides O(1) average-case lookup time, making it ideal for this use case. With millions of users, the difference is dramatic: for 1 million IDs, an unsorted array needs up to 1 million checks, binary search needs about 20 checks, but a hash table needs just 1 check on average. The hash table's constant-time lookup makes it the clear winner for this high-frequency operation, despite using slightly more memory.

**Grading Rubric:**
- 5 points: Correct choice (Option C) with reasoning
- 5 points: Accurate complexity analysis for each option
- 5 points: Explanation of why O(1) matters at scale

---

**End of Answer Key**
