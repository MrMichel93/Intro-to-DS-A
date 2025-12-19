# Module 4: Queues - Checkpoint Quiz

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
What principle do queues follow?
- A) FIFO (First In, First Out)
- B) LIFO (Last In, First Out)
- C) Random access
- D) Priority-based

### Question 2
Which operation adds an element to a queue?
- A) push
- B) enqueue
- C) insert
- D) add_back

### Question 3
What is the time complexity of enqueue and dequeue operations in a well-implemented queue?
- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n²)

### Question 4
In a queue, where is the next element to be removed located?
- A) Back/rear
- B) Front
- C) Middle
- D) Random position

### Question 5
Which is a real-world application of queues?
- A) Undo functionality
- B) Function call management
- C) Print job scheduling
- D) Expression evaluation

### Question 6
What is a circular queue?
- A) A queue arranged in a circle physically
- B) A queue where the rear wraps around to the beginning when space is available
- C) A queue that only stores circular data
- D) A queue with no front or back

### Question 7
What distinguishes a deque from a regular queue?
- A) Deques are slower
- B) Deques allow insertion and deletion at both ends
- C) Deques use more memory
- D) Deques are sorted

### Question 8
What is a priority queue?
- A) A queue where elements are served based on priority rather than arrival order
- B) A queue that processes elements faster
- C) A queue with limited capacity
- D) A queue sorted alphabetically

### Question 9
If you implement a queue using an array, what is the challenge with the dequeue operation?
- A) It takes O(n²) time
- B) It requires shifting all remaining elements
- C) It uses too much memory
- D) It's impossible to implement

### Question 10
Which data structure can efficiently implement a queue?
- A) Stack only
- B) Array only
- C) Linked list only
- D) Both arrays and linked lists

---

## Part 2: Code Analysis Questions (30 points, 10 points each)

### Question 11
What does this code do? Trace through it with operations: enqueue(1), enqueue(2), dequeue(), enqueue(3)

```python
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.items:
            return self.items.pop(0)
        return None
    
    def size(self):
        return len(self.items)
```

**Your Answer:**
- After enqueue(1), queue state: _______________
- After enqueue(2), queue state: _______________
- After dequeue(), returned value and queue state: _______________
- After enqueue(3), queue state: _______________
- What's the time complexity of dequeue()? _______________

### Question 12
Analyze this implementation of a queue using two stacks:

```python
class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, item):
        self.stack1.append(item)
    
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else None
```

**Your Answer:**
- Why does this work? _______________________________________________
- What is the amortized time complexity of dequeue? _______________
- Trace: enqueue(1), enqueue(2), dequeue(), what is returned? _______________

### Question 13
Find the bug in this circular queue implementation:

```python
class CircularQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0
        self.capacity = capacity
    
    def enqueue(self, item):
        if self.size == self.capacity:
            return False
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        return True
    
    def dequeue(self):
        if self.size == 0:
            return None
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        return item
```

**Your Answer:**
- Bug: _______________________________________________
- Why this causes problems: _______________________________________________
- How to fix it: _______________________________________________

---

## Part 3: Short Answer Questions (30 points, 15 points each)

### Question 14
Compare and contrast stacks and queues. Discuss their ordering principles, typical use cases, and implementation considerations. Why is each data structure suited to its respective applications? (5-7 sentences)

**Your Answer:**
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

### Question 15
You're designing a customer service call center system where calls need to be handled in the order they arrive, but VIP customers should be prioritized. How would you implement this using queue-based data structures? Describe your approach and the time complexity of key operations. (5-7 sentences)

**Your Answer:**
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

---

**End of Quiz**

Submit your completed quiz to your instructor. Good luck!
