# Module 3: Stacks - Checkpoint Quiz

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
What principle do stacks follow?
- A) FIFO (First In, First Out)
- B) LIFO (Last In, First Out)
- C) Random access
- D) Sorted order

### Question 2
Which operation adds an element to a stack?
- A) enqueue
- B) push
- C) insert
- D) append

### Question 3
What is the time complexity of push and pop operations on a stack?
- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n²)

### Question 4
When you pop from an empty stack, what should happen?
- A) Return 0
- B) Return None
- C) Raise an exception or error
- D) Return the last element

### Question 5
Which of these is a real-world application of stacks?
- A) Printer queue
- B) Undo/Redo functionality in editors
- C) Breadth-first search
- D) Round-robin scheduling

### Question 6
What does the peek/top operation do?
- A) Removes and returns the top element
- B) Returns the top element without removing it
- C) Returns the bottom element
- D) Clears the stack

### Question 7
Which data structure can be used to implement a stack?
- A) Only arrays
- B) Only linked lists
- C) Both arrays and linked lists
- D) Neither arrays nor linked lists

### Question 8
In which scenario is a stack particularly useful?
- A) Managing function calls and recursion
- B) Maintaining sorted data
- C) Finding the shortest path
- D) Random access to elements

### Question 9
What is the space complexity of a stack with n elements?
- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n²)

### Question 10
Which of the following uses a stack internally?
- A) Iterative loops
- B) Recursive function calls
- C) Hash table lookups
- D) Array sorting

---

## Part 2: Code Analysis Questions (30 points, 10 points each)

### Question 11
What does this function do? Trace through it with input: "hello"

```python
def process_string(s):
    stack = []
    for char in s:
        stack.append(char)
    
    result = ""
    while stack:
        result += stack.pop()
    
    return result
```

**Your Answer:**
- Output for "hello": _______________
- What does this function do? _______________
- Time Complexity: _______________
- Space Complexity: _______________

### Question 12
Analyze this code that checks balanced parentheses:

```python
def is_balanced(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != pairs[char]:
                return False
    
    return len(stack) == 0
```

**Your Answer:**
- What does is_balanced("({[]})") return? _______________
- What does is_balanced("({[}])") return? _______________
- Why does this algorithm work? _______________________________________________

### Question 13
Find the issue in this stack implementation:

```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[0]
    
    def is_empty(self):
        return len(self.items) == 0
```

**Your Answer:**
- Which method has a bug? _______________
- What's wrong with it? _______________________________________________
- Corrected code: _______________________________________________

---

## Part 3: Short Answer Questions (30 points, 15 points each)

### Question 14
Explain how stacks are used in the execution of recursive functions. Use a specific example (like calculating factorial) to illustrate how the call stack works. What happens when you have too many recursive calls? (5-7 sentences)

**Your Answer:**
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

### Question 15
You're building a web browser and need to implement the "Back" and "Forward" button functionality. How would you use stacks to implement this feature? Describe the algorithm and what happens when a user clicks a link, clicks Back, or clicks Forward. (5-7 sentences)

**Your Answer:**
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

---

**End of Quiz**

Submit your completed quiz to your instructor. Good luck!
