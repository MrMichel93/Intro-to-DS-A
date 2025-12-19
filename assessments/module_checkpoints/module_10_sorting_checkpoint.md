# Module 10: Sorting Algorithms - Checkpoint Quiz

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
What is the time complexity of Bubble Sort in the worst case?
- A) O(n)
- B) O(n log n)
- C) O(n²)
- D) O(2^n)

### Question 2
Which sorting algorithm repeatedly finds the minimum element and places it at the beginning?
- A) Bubble Sort
- B) Selection Sort
- C) Insertion Sort
- D) Merge Sort

### Question 3
What is the time complexity of Merge Sort in all cases?
- A) O(n)
- B) O(n log n)
- C) O(n²)
- D) O(log n)

### Question 4
Which sorting algorithm uses a divide-and-conquer approach?
- A) Bubble Sort
- B) Selection Sort
- C) Insertion Sort
- D) Merge Sort

### Question 5
What is the space complexity of Merge Sort?
- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n²)

### Question 6
Which sorting algorithm is most efficient for nearly sorted arrays?
- A) Bubble Sort
- B) Insertion Sort
- C) Selection Sort
- D) Merge Sort

### Question 7
Quick Sort's worst-case time complexity is:
- A) O(n)
- B) O(n log n)
- C) O(n²)
- D) O(2^n)

### Question 8
A sorting algorithm is stable if:
- A) It always completes successfully
- B) It preserves the relative order of equal elements
- C) It uses O(1) space
- D) It's always O(n log n)

### Question 9
Which of these is NOT a comparison-based sorting algorithm?
- A) Bubble Sort
- B) Merge Sort
- C) Counting Sort
- D) Quick Sort

### Question 10
What is the best possible time complexity for a comparison-based sorting algorithm?
- A) O(n)
- B) O(n log n)
- C) O(n²)
- D) O(log n)

---

## Part 2: Code Analysis Questions (30 points, 10 points each)

### Question 11
Trace through this sorting algorithm with array [5, 2, 8, 1, 9]. Show the array after each pass.

```python
def mystery_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

**Your Answer:**
- What sorting algorithm is this? _______________
- After pass 1: _______________
- After pass 2: _______________
- After pass 3: _______________
- Time Complexity: _______________

### Question 12
What does this recursive sorting function do? Analyze its approach.

```python
def divide_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = divide_sort(arr[:mid])
    right = divide_sort(arr[mid:])
    
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result
```

**Your Answer:**
- What sorting algorithm is this? _______________
- Time Complexity: _______________
- Space Complexity: _______________
- Is it stable? _______________

### Question 13
Find the bug in this implementation of Selection Sort:

```python
def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap found minimum with first element
        arr[i], arr[j] = arr[j], arr[i]
    
    return arr
```

**Your Answer:**
- Bug: _______________________________________________
- Why this is incorrect: _______________________________________________
- Corrected code: _______________________________________________

---

## Part 3: Short Answer Questions (30 points, 15 points each)

### Question 14
Compare Merge Sort and Quick Sort. Discuss their time complexity (best, average, worst cases), space complexity, stability, and when you would choose one over the other. Why is Quick Sort often preferred in practice despite having a worse worst-case complexity? (5-7 sentences)

**Your Answer:**
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

### Question 15
You're working on a system that needs to sort student records by GPA, but when GPAs are equal, you must maintain the original order (by student ID). The dataset has 10,000 students. Which sorting algorithm would you choose and why? Consider time complexity, space requirements, and the stability requirement. (5-7 sentences)

**Your Answer:**
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

---

**End of Quiz**

Submit your completed quiz to your instructor. Good luck!
