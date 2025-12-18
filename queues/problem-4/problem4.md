# Problem 4: Design Circular Queue

**Difficulty:** Medium 🟡

## Problem Statement

Design a circular queue with a fixed size. Support enQueue, deQueue, Front, Rear, isEmpty, and isFull operations.

### Example:
```
MyCircularQueue queue = new MyCircularQueue(3)
queue.enQueue(1)  // returns true
queue.enQueue(2)  // returns true
queue.enQueue(3)  // returns true
queue.enQueue(4)  // returns false (queue is full)
queue.Rear()      // returns 3
queue.isFull()    // returns true
queue.deQueue()   // returns true
queue.enQueue(4)  // returns true
queue.Rear()      // returns 4
```

## Solution

<details>
<summary>Click to reveal solution</summary>

```python
class MyCircularQueue:
    def __init__(self, k):
        self.queue = [0] * k
        self.size = 0
        self.capacity = k
        self.front = 0
        self.rear = -1
    
    def enQueue(self, value):
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1
        return True
    
    def deQueue(self):
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True
    
    def Front(self):
        return -1 if self.isEmpty() else self.queue[self.front]
    
    def Rear(self):
        return -1 if self.isEmpty() else self.queue[self.rear]
    
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity

# All operations: O(1)
```

</details>

[← Previous Problem](./problem3.md) | [Back to Queues](./README.md) | [Next Problem →](./problem5.md)
