# Module 9: Searching Algorithms - Checkpoint Quiz

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
What is the time complexity of linear search?
- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n²)

### Question 2
Binary search requires the input array to be:
- A) Unsorted
- B) Sorted
- C) Reversed
- D) Empty

### Question 3
What is the time complexity of binary search?
- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n log n)

### Question 4
In binary search, what do you compare the target with?
- A) The first element
- B) The last element
- C) The middle element
- D) A random element

### Question 5
Why is binary search more efficient than linear search for large sorted arrays?
- A) It checks fewer elements by eliminating half the search space each iteration
- B) It's easier to implement
- C) It uses less memory
- D) It works on unsorted arrays

### Question 6
What happens in binary search when the target is not found?
- A) It returns -1 or None
- B) It crashes
- C) It returns 0
- D) It keeps searching forever

### Question 7
If you're searching an unsorted array, which search algorithm must you use?
- A) Binary search
- B) Linear search
- C) Jump search
- D) Exponential search

### Question 8
What is the space complexity of iterative binary search?
- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n²)

### Question 9
Which search algorithm divides the search space into three parts?
- A) Binary search
- B) Linear search
- C) Ternary search
- D) Jump search

### Question 10
For an array of 1000 elements, what's the maximum number of comparisons binary search needs?
- A) 1000
- B) 500
- C) About 10 (log₂ 1000)
- D) 100

---

## Part 2: Code Analysis Questions (30 points, 10 points each)

### Question 11
Trace through this binary search with array [1, 3, 5, 7, 9, 11, 13, 15] and target 7.

```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
```

**Your Answer:**
- Iteration 1: left=___, right=___, mid=___, arr[mid]=___
- Iteration 2: left=___, right=___, mid=___, arr[mid]=___
- Iteration 3: left=___, right=___, mid=___, arr[mid]=___
- Final return value: _______________

### Question 12
What's wrong with this modified binary search implementation?

```python
def broken_binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid
        else:
            right = mid
    
    return -1
```

**Your Answer:**
- Bug 1: _______________________________________________
- Bug 2: _______________________________________________
- Why these cause problems: _______________________________________________

### Question 13
Compare these two implementations of linear search. Which is better and why?

```python
# Implementation A
def linear_search_a(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Implementation B
def linear_search_b(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1
```

**Your Answer:**
- Which is better? _______________
- Why? _______________________________________________
- Are their time complexities different? _______________

---

## Part 3: Short Answer Questions (30 points, 15 points each)

### Question 14
Explain why binary search is O(log n) while linear search is O(n). Use an example with an array of 1000 elements to illustrate the difference in the number of operations each algorithm performs. (5-7 sentences)

**Your Answer:**
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

### Question 15
You're building a phone book application that needs to search for contacts by name. Users will search frequently, but add/remove contacts rarely. The contact list is maintained in sorted order by name. Which search algorithm would you use and why? What if the list wasn't sorted - would your answer change? Explain the trade-offs. (5-7 sentences)

**Your Answer:**
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

---

**End of Quiz**

Submit your completed quiz to your instructor. Good luck!
