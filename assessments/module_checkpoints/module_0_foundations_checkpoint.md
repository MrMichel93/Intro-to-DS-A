# Module 0: Foundations - Checkpoint Quiz

**Time Limit:** 45 minutes  
**Total Points:** 100

## Instructions
- Answer all questions to the best of your ability
- For multiple choice questions, select the single best answer
- For code analysis questions, write your answer clearly
- For short answer questions, provide concise but complete responses

---

## Part 1: Multiple Choice Questions (40 points, 4 points each)

### Question 1
What does Big O notation describe?
- A) The exact number of operations an algorithm performs
- B) The upper bound of an algorithm's growth rate as input size increases
- C) The average case performance of an algorithm
- D) The amount of memory an algorithm uses

### Question 2
Which of the following represents the best time complexity?
- A) O(n²)
- B) O(n log n)
- C) O(n)
- D) O(1)

### Question 3
An algorithm that checks every element in an array once has a time complexity of:
- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n²)

### Question 4
What is the space complexity of an algorithm that creates a new array of size n?
- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n²)

### Question 5
Which growth rate is fastest for large values of n?
- A) O(log n)
- B) O(n)
- C) O(n log n)
- D) O(2^n)

### Question 6
What does it mean when we say an algorithm has O(1) space complexity?
- A) It uses no memory
- B) It uses a constant amount of memory regardless of input size
- C) It uses one byte of memory
- D) It uses linear memory

### Question 7
If an algorithm has nested loops where each iterates n times, what is its time complexity?
- A) O(n)
- B) O(2n)
- C) O(n²)
- D) O(n + n)

### Question 8
Binary search on a sorted array has a time complexity of:
- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n log n)

### Question 9
Which of the following best describes a good problem-solving approach?
- A) Start coding immediately to save time
- B) Understand the problem, plan your approach, then implement
- C) Always use the most complex solution
- D) Avoid testing your code

### Question 10
What is the time complexity of accessing an element in an array by index?
- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n²)

---

## Part 2: Code Analysis Questions (30 points, 10 points each)

### Question 11
Analyze the following code and determine its time and space complexity. Explain your reasoning.

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

**Your Answer:**
- Time Complexity: _______________
- Space Complexity: _______________
- Explanation: _______________________________________________

### Question 12
What will be the output of this code? Trace through the execution.

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

**Your Answer:**
- Output: _______________
- Trace of execution: _______________________________________________

### Question 13
Identify any issues with this code and suggest how to fix them:

```python
def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return average
```

**Your Answer:**
- Issues: _______________________________________________
- Fixed code: _______________________________________________

---

## Part 3: Short Answer Questions (30 points, 15 points each)

### Question 14
Explain the difference between time complexity and space complexity. Provide an example where an algorithm might have good time complexity but poor space complexity, or vice versa. (5-7 sentences)

**Your Answer:**
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

### Question 15
You need to store user IDs and quickly check if a user ID exists in your system. Millions of users might access this data simultaneously. Consider the following options:
- Option A: Store IDs in an unsorted array
- Option B: Store IDs in a sorted array
- Option C: Store IDs in a hash table (set)

Which option would you choose and why? Discuss the time complexity of lookup operations for each option. (5-7 sentences)

**Your Answer:**
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

---

**End of Quiz**

Submit your completed quiz to your instructor. Good luck!
