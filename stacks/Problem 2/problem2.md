# Problem 2: Min Stack

**Difficulty:** Easy 🟢

## Problem Statement

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Operations:
- push(x) -- Push element x onto stack
- pop() -- Remove element on top
- top() -- Get the top element
- getMin() -- Retrieve the minimum element

### Example:
```
MinStack minStack = new MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()   → Returns -3
minStack.pop()
minStack.top()      → Returns 0
minStack.getMin()   → Returns -2
```

## Solution

<details>
<summary>Click to reveal solution</summary>

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # Tracks minimums
    
    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
    
    def pop(self):
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.min_stack[-1]

# All operations: O(1) time, O(n) space
```

</details>

[← Previous Problem](./problem1.md) | [Back to Stacks](./README.md) | [Next Problem →](./problem3.md)
