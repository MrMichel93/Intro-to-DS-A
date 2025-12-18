# Problem 1: Implement Queue using Stacks

**Difficulty:** Easy 🟢

## Problem Statement

Implement a queue using only two stacks. Your queue should support enqueue, dequeue, peek, and isEmpty operations.

### Example:
```
MyQueue queue = new MyQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.peek()      // returns 1
queue.dequeue()   // returns 1
queue.isEmpty()   // returns false
```

## Hints

<details>
<summary>Hint</summary>
Use one stack for enqueue operations and transfer to another stack for dequeue operations.
</details>

## Solution

<details>
<summary>Click to reveal solution</summary>

```python
class MyQueue:
    def __init__(self):
        self.stack1 = []  # For enqueue
        self.stack2 = []  # For dequeue
    
    def enqueue(self, x):
        self.stack1.append(x)
    
    def dequeue(self):
        self._move()
        return self.stack2.pop()
    
    def peek(self):
        self._move()
        return self.stack2[-1]
    
    def _move(self):
        """Move elements from stack1 to stack2 if needed"""
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
    
    def isEmpty(self):
        return not self.stack1 and not self.stack2

# Enqueue: O(1), Dequeue: O(1) amortized
```

</details>

[← Back to Queues](./README.md) | [Next Problem →](./problem2.md)
