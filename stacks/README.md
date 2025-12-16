# Stacks

## What is a Stack?

A **stack** is a linear data structure that follows the **LIFO** (Last-In-First-Out) principle. Think of it like a stack of plates: you can only add or remove plates from the top!

```
    Top → [5]  ← Most recently added
          [3]
          [8]
          [1]  ← First added
```

## Why Stacks Matter

Stacks are everywhere in computing:
- **Function call stack** - How programs track function calls
- **Undo/Redo** - Text editors, graphics programs
- **Browser history** - Back button functionality
- **Expression evaluation** - Calculators, compilers
- **Backtracking algorithms** - Maze solving, puzzles

## Key Operations

### 1. Push
Add an element to the top of the stack.
**Time Complexity: O(1)**

### 2. Pop
Remove and return the top element.
**Time Complexity: O(1)**

### 3. Peek (or Top)
View the top element without removing it.
**Time Complexity: O(1)**

### 4. isEmpty
Check if the stack is empty.
**Time Complexity: O(1)**

## Implementation

### Using Python List

```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add item to top of stack"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return top item"""
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        """Return top item without removing"""
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[-1]
    
    def is_empty(self):
        """Check if stack is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return number of items"""
        return len(self.items)
```

### Using Linked List

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.count += 1
    
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        data = self.top.data
        self.top = self.top.next
        self.count -= 1
        return data
    
    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.top.data
    
    def is_empty(self):
        return self.top is None
```

## Real-World Applications

### 1. Expression Evaluation
Convert infix expressions to postfix and evaluate them.
```
Infix: 2 + 3 * 4
Postfix: 2 3 4 * +
```

### 2. Balanced Parentheses
Check if brackets are properly matched.
```
Valid: ({[]})
Invalid: ({[}])
```

### 3. Function Call Stack
```
def a():
    b()

def b():
    c()

def c():
    return

# Stack: [a, b, c] → [a, b] → [a] → []
```

### 4. Undo Mechanism
```
Actions: [Type "H", Type "i", Delete, Type "o"]
Undo: Removes last action from stack
```

## Time Complexity Summary

| Operation | Time Complexity |
|-----------|----------------|
| Push      | O(1)           |
| Pop       | O(1)           |
| Peek      | O(1)           |
| Search    | O(n)           |

## Space Complexity

O(n) where n is the number of elements in the stack.

## Common Patterns

### Monotonic Stack
Maintain elements in increasing or decreasing order. Useful for:
- Next greater element
- Stock span problems
- Histogram problems

### Two Stacks
Use two stacks to implement:
- Queue
- Special data structures with min/max queries

## Practice Problems

Test your understanding with these problems:

1. **[Problem 1: Valid Parentheses](./problem1.md)** - Easy 🟢
2. **[Problem 2: Min Stack](./problem2.md)** - Easy 🟢
3. **[Problem 3: Evaluate Postfix](./problem3.md)** - Medium 🟡
4. **[Problem 4: Next Greater Element](./problem4.md)** - Medium 🟡
5. **[Problem 5: Daily Temperatures](./problem5.md)** - Medium 🟡
6. **[Problem 6: Largest Rectangle](./problem6.md)** - Hard 🔴

## Next Steps

After mastering stacks, check out [Queues](../queues/), which follow a different ordering principle (FIFO)!

---

💡 **Pro Tip**: When you see problems involving matching pairs, recent history, or reversing order, think STACK!
