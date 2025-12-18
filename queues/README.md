# Queues

## What is a Queue?

A **queue** is a linear data structure that follows the **FIFO** (First-In-First-Out) principle. Think of it like a line at a store: the first person in line is the first to be served!

```
Front → [1] [2] [3] [4] ← Rear
       Remove   ↑    Add
       from    here   to
       here           here
```

## Why Queues Matter

Queues model many real-world scenarios:
- **Task scheduling** - Operating systems, print queues
- **Breadth-First Search** - Graph algorithms
- **Message queues** - Asynchronous communication
- **Call centers** - Customer service lines
- **Streaming** - Data buffers

## Key Operations

### 1. Enqueue
Add an element to the rear of the queue.
**Time Complexity: O(1)**

### 2. Dequeue
Remove and return the front element.
**Time Complexity: O(1)**

### 3. Peek (or Front)
View the front element without removing it.
**Time Complexity: O(1)**

### 4. isEmpty
Check if the queue is empty.
**Time Complexity: O(1)**

## Implementation

### Using Python List

```python
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Add item to rear"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return front item"""
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items.pop(0)  # O(n) operation!
    
    def peek(self):
        """Return front item without removing"""
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items[0]
    
    def is_empty(self):
        return len(self.items) == 0
```

### Using collections.deque (Better!)

```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        self.items.append(item)  # O(1)
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items.popleft()  # O(1)
    
    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items[0]
    
    def is_empty(self):
        return len(self.items) == 0
```

## Types of Queues

### 1. Simple Queue
Basic FIFO queue.

### 2. Circular Queue
Last position connects back to first position. Efficient use of space.

### 3. Priority Queue
Elements have priorities; highest priority dequeued first.

### 4. Double-Ended Queue (Deque)
Can add/remove from both ends.

## Real-World Applications

### 1. Operating Systems
- Process scheduling (CPU time allocation)
- Handling interrupts

### 2. Networks
- Packet routing
- Request handling in web servers

### 3. Breadth-First Search
```
Queue: [Start Node]
While queue not empty:
    Process front node
    Add neighbors to queue
```

### 4. Printer Queue
Multiple print jobs waiting in order.

## Queue vs Stack

| Feature | Stack | Queue |
|---------|-------|-------|
| Order | LIFO | FIFO |
| Add | Push (top) | Enqueue (rear) |
| Remove | Pop (top) | Dequeue (front) |
| Use Case | Undo/Redo | Task scheduling |

## Time Complexity Summary

| Operation | Time (List) | Time (Deque) |
|-----------|-------------|--------------|
| Enqueue   | O(1)        | O(1)         |
| Dequeue   | O(n)        | O(1)         |
| Peek      | O(1)        | O(1)         |
| Search    | O(n)        | O(n)         |

## Practice Problems

Each problem is organized in its own directory containing:
- `problemN.md` - Problem description and examples
- `problemN.py` - Python starter file with function stubs and comments
- `test_problemN.py` - Pytest test file for validation

Navigate to each Problem directory to access the files:

- [Problem 1](./problem-1/problem1.md)
- [Problem 2](./problem-2/problem2.md)
- [Problem 3](./problem-3/problem3.md)
- [Problem 4](./problem-4/problem4.md)
- [Problem 5](./problem-5/problem5.md)
- [Problem 6](./problem-6/problem6.md)

## Next Steps

Once you understand queues, explore [Hash Tables](../hash-tables/) for fast lookups!

---

💡 **Pro Tip**: Use Python's `collections.deque` for efficient queue operations instead of list!
