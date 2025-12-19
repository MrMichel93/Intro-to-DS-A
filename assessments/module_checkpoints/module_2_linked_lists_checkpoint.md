# Module 2: Linked Lists - Checkpoint Quiz

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
What is the main advantage of linked lists over arrays?
- A) Faster access by index
- B) Less memory usage
- C) Dynamic size and efficient insertion/deletion
- D) Better cache performance

### Question 2
In a singly linked list, each node contains:
- A) Only data
- B) Data and a pointer to the next node
- C) Data and pointers to both next and previous nodes
- D) Only a pointer to the next node

### Question 3
What is the time complexity of accessing the nth element in a linked list?
- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n²)

### Question 4
What is the time complexity of inserting a node at the beginning of a linked list?
- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n²)

### Question 5
Which pointer in a linked list always points to NULL/None?
- A) Head
- B) Middle node
- C) Last node's next pointer
- D) First node's next pointer

### Question 6
What distinguishes a doubly linked list from a singly linked list?
- A) It has two head pointers
- B) Each node has pointers to both next and previous nodes
- C) It can store two values per node
- D) It uses twice as much memory for data

### Question 7
What is the time complexity of deleting a node when you have a reference to the node before it?
- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n²)

### Question 8
In a circular linked list:
- A) All nodes point to themselves
- B) The last node points back to the first node
- C) Nodes form a circle in memory
- D) You cannot traverse the list

### Question 9
What is a common technique to detect a cycle in a linked list?
- A) Count all nodes
- B) Use two pointers moving at different speeds (Floyd's algorithm)
- C) Create a copy of the list
- D) Sort the list first

### Question 10
Compared to arrays, linked lists are better for:
- A) Random access by index
- B) Cache performance
- C) Frequent insertions and deletions in the middle
- D) Binary search

---

## Part 2: Code Analysis Questions (30 points, 10 points each)

### Question 11
Analyze this linked list code. What does it do and what is its time complexity?

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mystery_function(head):
    if head is None or head.next is None:
        return head
    
    current = head
    while current.next is not None:
        current = current.next
    
    return current.data
```

**Your Answer:**
- What does this function return? _______________
- Time Complexity: _______________
- Space Complexity: _______________
- Explanation: _______________________________________________

### Question 12
Trace through this code with the input list: 1 -> 2 -> 3 -> None. What will be the final state?

```python
def transform_list(head):
    prev = None
    current = head
    
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev
```

**Your Answer:**
- Final list structure: _______________
- What does this algorithm do? _______________
- Time Complexity: _______________

### Question 13
Find the bug in this code that attempts to insert a node at the end of a linked list:

```python
def insert_at_end(head, data):
    new_node = Node(data)
    
    if head is None:
        return new_node
    
    current = head
    while current.next is not None:
        current = current.next
    
    current = new_node
    return head
```

**Your Answer:**
- Bug: _______________________________________________
- Why this is wrong: _______________________________________________
- Corrected line: _______________________________________________

---

## Part 3: Short Answer Questions (30 points, 15 points each)

### Question 14
Compare and contrast arrays and linked lists. Discuss at least three key differences in terms of memory allocation, access patterns, and operation complexities. When would you choose one over the other? (5-7 sentences)

**Your Answer:**
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

### Question 15
Explain how you would find the middle element of a singly linked list in one pass (you don't know the length beforehand). Describe the algorithm and explain why it works. What is its time and space complexity? (5-7 sentences)

**Your Answer:**
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

---

**End of Quiz**

Submit your completed quiz to your instructor. Good luck!
