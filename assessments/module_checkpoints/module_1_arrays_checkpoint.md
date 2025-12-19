# Module 1: Arrays - Checkpoint Quiz

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
What is the main advantage of arrays over other data structures?
- A) Dynamic size
- B) O(1) access time by index
- C) Easy insertion in the middle
- D) Unlimited capacity

### Question 2
In a zero-indexed array of size 10, what is the index of the last element?
- A) 10
- B) 9
- C) 8
- D) 11

### Question 3
What is the time complexity of inserting an element at the beginning of an array?
- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n²)

### Question 4
Arrays store elements in:
- A) Random memory locations
- B) Contiguous memory locations
- C) Linked memory locations
- D) Distributed memory locations

### Question 5
What is the time complexity of accessing the middle element of an array?
- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n/2)

### Question 6
Which operation is most efficient on arrays?
- A) Insertion at the beginning
- B) Deletion from the middle
- C) Random access by index
- D) Expanding the size

### Question 7
In a 2D array declared as `matrix[3][4]`, how many total elements are there?
- A) 7
- B) 12
- C) 3
- D) 4

### Question 8
What is the space complexity of creating a new array to store n elements?
- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n²)

### Question 9
The two-pointer technique is commonly used for:
- A) Increasing array size
- B) Finding pairs or processing arrays from both ends
- C) Sorting arrays
- D) Creating 2D arrays

### Question 10
What is the time complexity of finding the maximum element in an unsorted array?
- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n²)

---

## Part 2: Code Analysis Questions (30 points, 10 points each)

### Question 11
Analyze this code and determine what it does. Also provide its time and space complexity.

```python
def process_array(arr):
    n = len(arr)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= arr[j]
        result.append(product)
    return result
```

**Your Answer:**
- What does this function do? _______________
- Time Complexity: _______________
- Space Complexity: _______________
- Explanation: _______________________________________________

### Question 12
What will be the output of this code? Trace through the execution step by step.

```python
arr = [1, 2, 3, 4, 5]
left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print(arr)
```

**Your Answer:**
- Output: _______________
- What does this algorithm do? _______________
- Time Complexity: _______________

### Question 13
Identify the bug in this code and explain how to fix it:

```python
def find_element(arr, target):
    for i in range(len(arr)):
        if arr[i] = target:
            return i
    return -1
```

**Your Answer:**
- Bug: _______________________________________________
- Fixed code: _______________________________________________
- Explanation: _______________________________________________

---

## Part 3: Short Answer Questions (30 points, 15 points each)

### Question 14
Explain the difference between static arrays and dynamic arrays (like Python lists). What happens internally when a dynamic array needs to grow beyond its current capacity? Why is this important to understand? (5-7 sentences)

**Your Answer:**
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

### Question 15
You are building a photo gallery application that needs to store and display images. Images are frequently accessed by their position (e.g., "show image 5"), but users also need to add new images to the end of the gallery. Would you use an array for this? Explain your reasoning, considering both the advantages and potential limitations. What would be the time complexity of the key operations? (5-7 sentences)

**Your Answer:**
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

---

**End of Quiz**

Submit your completed quiz to your instructor. Good luck!
