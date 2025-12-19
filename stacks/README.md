# Stacks

## Overview
A **stack** is a linear data structure that follows the **Last-In-First-Out (LIFO)** principle, meaning the most recently added element is the first one to be removed. Imagine a stack of plates: you can only add or remove plates from the top. This simple yet powerful concept is fundamental to computer science, enabling everything from function calls to undo operations. Stacks restrict access to one end only, making operations predictable and efficient.

## Why It Matters
Stacks are foundational to how computers work and power many everyday applications:

- **Text Editors (Word, Google Docs, VS Code)**: Every time you press Ctrl+Z to undo, you're using a stack! Each edit action is pushed onto an undo stack. When you undo, the most recent action is popped and reversed. Redo uses a separate stack. This is why undo always reverses your *most recent* action, not a random one.

- **Web Browsers (Chrome, Firefox, Safari)**: The back button uses a stack of visited pages. Each new page you visit is pushed onto the history stack. Clicking back pops the current page and takes you to the previous one. The forward button uses another stack. This is why back always goes to your *last* visited page.

- **Function Call Stack (All Programming Languages)**: When function A calls function B, which calls function C, the computer uses a stack to remember where to return. C finishes → return to B. B finishes → return to A. This is why recursive functions can cause "stack overflow" errors—too many function calls stack up!

- **Expression Evaluation (Calculators, Compilers)**: When you type `3 + 4 * 5`, the computer uses a stack to respect operator precedence. It evaluates `4 * 5` first, then adds 3. Compilers use stacks to parse code syntax and convert mathematical expressions into machine instructions.

- **Mobile App Navigation (iOS, Android)**: When you navigate through app screens, each screen is pushed onto a navigation stack. The back button/gesture pops the current screen and returns to the previous one. This is why apps remember your navigation path.

## Visual Representation
```
Stack Visualization (LIFO Principle):

        ┌─────┐
        │  5  │  ← Top (most recent)
        ├─────┤     Push/Pop happens here ONLY
        │  8  │     ↑
        ├─────┤     │
        │  3  │     │ Can only access top element
        ├─────┤     │
        │  1  │     │
        └─────┘  ← Bottom (oldest element)

Push Operation (Add to top):
Step 1: Stack is [1, 3, 8, 5]
Step 2: Push(9)
Step 3: Stack is [1, 3, 8, 5, 9]  ← 9 is now on top

        ┌─────┐
        │  9  │  ← New top
        ├─────┤
        │  5  │
        ├─────┤
        │  8  │
        ├─────┤
        │  3  │
        ├─────┤
        │  1  │
        └─────┘

Pop Operation (Remove from top):
Step 1: Stack is [1, 3, 8, 5, 9]
Step 2: Pop() → returns 9
Step 3: Stack is [1, 3, 8, 5]

        ┌─────┐
        │  5  │  ← New top (after 9 removed)
        ├─────┤
        │  8  │
        ├─────┤
        │  3  │
        ├─────┤
        │  1  │
        └─────┘

Peek Operation (View top without removing):
Stack: [1, 3, 8, 5]
Peek() → returns 5 (but 5 stays on stack)
Stack still: [1, 3, 8, 5]

Real-World Analogy - Stack of Dishes:
        
        ┌───────┐
        │   🍽️   │  ← Can only take the top dish
        ├───────┤
        │   🍽️   │
        ├───────┤
        │   🍽️   │     Can't pull a dish from the middle!
        └───────┘     Must take from top

Implementation Comparison:

Array-Based Stack:                  Linked List-Based Stack:
┌─────┬─────┬─────┬─────┐          top → [5|●] → [8|●] → [3|●] → [1|null]
│  1  │  3  │  8  │  5  │                  ↑
└─────┴─────┴─────┴─────┘                Push/Pop here
        top pointer →                     (at head of list)
        
Array: Fixed size (or resize)       Linked List: Dynamic size
Fast access, contiguous memory      Flexible, scattered memory
```

## Key Concepts

### 1. **LIFO (Last-In-First-Out) Principle**
The defining characteristic of stacks. The most recently added element is always the first to be removed. This creates a "reverse chronological order" effect.

**Think Like a Programmer:** LIFO is perfect for "most recent first" scenarios: undo operations, navigation history, or tracking nested structures like parentheses.

### 2. **Push Operation**
Adding an element to the top of the stack. This is the only way to add elements—you can't insert in the middle.

**Think Like a Programmer:** Push is always O(1) because you're only touching the top. No shifting or traversing needed.

### 3. **Pop Operation**
Removing and returning the top element. This is the only way to remove elements—you can't delete from the middle without popping everything above it first.

**Think Like a Programmer:** Always check if the stack is empty before popping! Popping an empty stack is a common error.

### 4. **Peek (Top) Operation**
Viewing the top element without removing it. Useful when you need to check what's next without modifying the stack.

**Think Like a Programmer:** Peek is your "look before you leap" operation. Use it to make decisions about whether to pop or push.

### 5. **Stack Underflow and Overflow**
**Underflow**: Attempting to pop from an empty stack.
**Overflow**: Attempting to push onto a full stack (only relevant for fixed-size stacks).

**Think Like a Programmer:** Always validate stack state before operations. Use `is_empty()` checks to prevent underflow.

### 6. **Stack as Restricted Data Structure**
Stacks intentionally limit access to maintain the LIFO property. You can't randomly access elements in the middle—only the top.

**Think Like a Programmer:** This restriction is a feature, not a bug! It prevents bugs by enforcing a clear access pattern and makes operations predictable.

## How It Works

### Stack Operations Flow
Stacks can be implemented using arrays (Python lists) or linked lists. Both support O(1) push and pop operations.

**Array-based approach:**
- Use a list and track the "top" index
- Push: append to end
- Pop: remove from end
- Top is always at index -1 (last element)

**Linked list approach:**
- Push/pop at the head of the list
- Each node points to the node below it
- Top pointer references the head node

### Example Walkthrough

**Scenario:** Managing undo/redo in a text editor

```python
# User is typing a document
undo_stack = []  # Stores actions for undo
redo_stack = []  # Stores actions for redo
```

**Action 1: User types "Hello" (O(1))**
```python
action1 = ("INSERT", "Hello", position=0)
undo_stack.append(action1)  # Push onto undo stack

# Undo Stack: [("INSERT", "Hello", 0)]
# Redo Stack: []
```

**Action 2: User types " World" (O(1))**
```python
action2 = ("INSERT", " World", position=5)
undo_stack.append(action2)

# Undo Stack: [("INSERT", "Hello", 0), ("INSERT", " World", 5)]
# Redo Stack: []
```

**Action 3: User deletes " World" (O(1))**
```python
action3 = ("DELETE", " World", position=5)
undo_stack.append(action3)

# Undo Stack: [("INSERT", "Hello", 0), ("INSERT", " World", 5), ("DELETE", " World", 5)]
# Redo Stack: []
```

**User presses Undo (O(1))**
```python
# Pop most recent action from undo stack
last_action = undo_stack.pop()  # ("DELETE", " World", 5)

# Reverse the action
if last_action[0] == "DELETE":
    # Undo a delete means re-insert the text
    text = re_insert(last_action[1], last_action[2])

# Push onto redo stack in case user wants to redo
redo_stack.append(last_action)

# Undo Stack: [("INSERT", "Hello", 0), ("INSERT", " World", 5)]
# Redo Stack: [("DELETE", " World", 5)]
# Document: "Hello World" (delete was undone)
```

**User presses Undo again (O(1))**
```python
last_action = undo_stack.pop()  # ("INSERT", " World", 5)

if last_action[0] == "INSERT":
    # Undo an insert means delete the text
    text = delete(last_action[1], last_action[2])

redo_stack.append(last_action)

# Undo Stack: [("INSERT", "Hello", 0)]
# Redo Stack: [("DELETE", " World", 5), ("INSERT", " World", 5)]
# Document: "Hello" (second action undone)
```

**User presses Redo (O(1))**
```python
# Pop from redo stack
action_to_redo = redo_stack.pop()  # ("INSERT", " World", 5)

# Perform the action again
if action_to_redo[0] == "INSERT":
    text = insert(action_to_redo[1], action_to_redo[2])

# Push back onto undo stack
undo_stack.append(action_to_redo)

# Undo Stack: [("INSERT", "Hello", 0), ("INSERT", " World", 5)]
# Redo Stack: [("DELETE", " World", 5)]
# Document: "Hello World" (redo applied)
```

**Key Insight:** The most recent action is always processed first (LIFO). This creates the intuitive undo/redo behavior users expect.

## Python Implementation

```python
# ============================================
# STACK IMPLEMENTATION USING ARRAY (LIST)
# ============================================

class ArrayStack:
    """
    Stack implementation using Python list (dynamic array).
    Most common and efficient implementation in Python.
    """
    
    def __init__(self, capacity=None):
        """
        Initialize empty stack.
        Time Complexity: O(1)
        Space Complexity: O(capacity) or O(1) if no capacity limit
        
        Args:
            capacity: Maximum stack size (None for unlimited)
        """
        self.items = []              # Store elements
        self.capacity = capacity     # Optional size limit
    
    def push(self, item):
        """
        Add item to top of stack.
        Time Complexity: O(1) amortized (occasional array resize)
        Space Complexity: O(1)
        
        Real-world: Adding a new page to browser history
        """
        # Check for stack overflow (if capacity set)
        if self.capacity and len(self.items) >= self.capacity:
            raise OverflowError("Stack is full")
        
        # Add to end of list (this is the "top")
        self.items.append(item)
    
    def pop(self):
        """
        Remove and return top item.
        Time Complexity: O(1)
        Space Complexity: O(1)
        
        Returns: Top element
        Raises: IndexError if stack is empty (underflow)
        
        Real-world: Pressing back button in browser
        """
        # Check for stack underflow
        if self.is_empty():
            raise IndexError("Cannot pop from empty stack (underflow)")
        
        # Remove and return last element
        return self.items.pop()
    
    def peek(self):
        """
        View top item without removing it.
        Time Complexity: O(1)
        Space Complexity: O(1)
        
        Returns: Top element
        Raises: IndexError if stack is empty
        
        Real-world: Checking current page without navigating
        """
        if self.is_empty():
            raise IndexError("Cannot peek at empty stack")
        
        # Return last element without removing
        return self.items[-1]
    
    def is_empty(self):
        """
        Check if stack has no elements.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return len(self.items) == 0
    
    def size(self):
        """
        Get number of elements in stack.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return len(self.items)
    
    def clear(self):
        """
        Remove all elements from stack.
        Time Complexity: O(1) in Python (reassignment)
        Space Complexity: O(1)
        """
        self.items = []
    
    def __repr__(self):
        """String representation showing top at right"""
        return f"Stack({self.items})"
    
    def __len__(self):
        """Allow len(stack) syntax"""
        return self.size()


# ============================================
# STACK IMPLEMENTATION USING LINKED LIST
# ============================================

class Node:
    """Node for linked list implementation"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    """
    Stack implementation using linked list.
    Useful when:
    - Stack size is highly unpredictable
    - Memory is fragmented
    - You want to avoid array resizing
    """
    
    def __init__(self):
        """
        Initialize empty stack.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.top = None    # Reference to top node
        self.count = 0     # Track size
    
    def push(self, data):
        """
        Add item to top of stack.
        Time Complexity: O(1) - always constant
        Space Complexity: O(1) per push
        
        Think Like a Programmer: Pushing is just inserting at
        head of linked list. Very efficient!
        """
        # Create new node
        new_node = Node(data)
        
        # Link new node to current top
        new_node.next = self.top
        
        # Update top to new node
        self.top = new_node
        
        self.count += 1
    
    def pop(self):
        """
        Remove and return top item.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot pop from empty stack")
        
        # Save data from top node
        data = self.top.data
        
        # Move top to next node
        self.top = self.top.next
        
        self.count -= 1
        
        return data
    
    def peek(self):
        """View top item without removing"""
        if self.is_empty():
            raise IndexError("Cannot peek at empty stack")
        
        return self.top.data
    
    def is_empty(self):
        """Check if stack is empty"""
        return self.top is None
    
    def size(self):
        """Get number of elements"""
        return self.count
    
    def __repr__(self):
        """String representation"""
        if self.is_empty():
            return "LinkedStack(empty)"
        
        # Traverse and collect elements
        elements = []
        current = self.top
        while current:
            elements.append(str(current.data))
            current = current.next
        
        return f"LinkedStack(top: {' -> '.join(elements)})"


# ============================================
# ADVANCED: MIN STACK
# ============================================

class MinStack:
    """
    Stack that supports O(1) retrieval of minimum element.
    
    Think Like a Programmer: Use two stacks:
    1. Main stack: stores all elements
    2. Min stack: tracks minimum at each level
    
    Real-world: Stock price tracking with "What was lowest price?"
    """
    
    def __init__(self):
        self.stack = []      # Main stack
        self.min_stack = []  # Tracks minimums
    
    def push(self, item):
        """
        Push item and update minimum.
        Time: O(1), Space: O(1)
        """
        self.stack.append(item)
        
        # Update min stack
        if not self.min_stack or item <= self.min_stack[-1]:
            self.min_stack.append(item)
    
    def pop(self):
        """
        Pop item and update minimum.
        Time: O(1), Space: O(1)
        """
        if not self.stack:
            raise IndexError("Stack is empty")
        
        item = self.stack.pop()
        
        # Remove from min stack if it was the minimum
        if item == self.min_stack[-1]:
            self.min_stack.pop()
        
        return item
    
    def get_min(self):
        """
        Get minimum element in O(1) time.
        Time: O(1), Space: O(1)
        """
        if not self.min_stack:
            raise IndexError("Stack is empty")
        
        return self.min_stack[-1]


# ============================================
# PRACTICAL APPLICATIONS
# ============================================

def is_balanced_parentheses(expression):
    """
    Check if parentheses/brackets are balanced.
    Time Complexity: O(n) - process each character once
    Space Complexity: O(n) worst case (all opening brackets)
    
    Real-world: Code editors checking syntax, compilers parsing code
    
    Examples:
    - "({[]})" → True (balanced)
    - "({[}])" → False (wrong order)
    - "(((" → False (unclosed)
    """
    stack = []
    
    # Matching pairs
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in '({[':
            # Opening bracket → push onto stack
            stack.append(char)
        elif char in ')}]':
            # Closing bracket → should match top of stack
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    
    # All brackets should be matched (stack empty)
    return len(stack) == 0


def reverse_string(text):
    """
    Reverse string using stack.
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Think Like a Programmer: Push all characters, then pop
    them out (LIFO gives reverse order)
    """
    stack = []
    
    # Push all characters
    for char in text:
        stack.append(char)
    
    # Pop all characters (reversed order)
    reversed_text = ''
    while stack:
        reversed_text += stack.pop()
    
    return reversed_text


def evaluate_postfix(expression):
    """
    Evaluate postfix (Reverse Polish Notation) expression.
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Example: "3 4 + 2 *" means (3 + 4) * 2 = 14
    
    Real-world: Calculators, compilers (easier to evaluate than infix)
    
    Think Like a Programmer:
    - See number → push onto stack
    - See operator → pop two operands, compute, push result
    """
    stack = []
    
    operators = {'+', '-', '*', '/'}
    
    for token in expression.split():
        if token in operators:
            # Pop two operands (note the order!)
            b = stack.pop()
            a = stack.pop()
            
            # Apply operator
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = a / b
            
            # Push result back
            stack.append(result)
        else:
            # It's a number, push it
            stack.append(float(token))
    
    # Final result is top of stack
    return stack.pop()


def next_greater_element(arr):
    """
    Find next greater element for each element in array.
    Time Complexity: O(n) - each element pushed/popped once
    Space Complexity: O(n) for stack and result
    
    Example: [4, 5, 2, 10] → [5, 10, 10, -1]
    (next greater than 4 is 5, than 5 is 10, than 2 is 10, no greater after 10)
    
    Real-world: Stock span problem, scheduling algorithms
    
    Think Like a Programmer: Monotonic stack technique
    Maintain stack of elements for which we haven't found greater element yet
    """
    result = [-1] * len(arr)
    stack = []  # Store indices
    
    # Traverse array from right to left
    for i in range(len(arr) - 1, -1, -1):
        # Pop elements smaller than or equal to current
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        
        # If stack not empty, top is next greater
        if stack:
            result[i] = arr[stack[-1]]
        
        # Push current index
        stack.append(i)
    
    return result


# ============================================
# DEMONSTRATION
# ============================================

def demo_undo_redo():
    """Demonstrate undo/redo functionality"""
    print("=== Undo/Redo Example ===")
    
    undo_stack = ArrayStack()
    redo_stack = ArrayStack()
    
    # User performs actions
    actions = ["Type 'Hello'", "Type ' World'", "Delete ' World'", "Type '!'"]
    
    for action in actions:
        print(f"Action: {action}")
        undo_stack.push(action)
    
    print(f"\nUndo stack: {undo_stack}")
    
    # Undo twice
    print("\n--- Pressing Undo ---")
    undo1 = undo_stack.pop()
    redo_stack.push(undo1)
    print(f"Undid: {undo1}")
    
    print("\n--- Pressing Undo again ---")
    undo2 = undo_stack.pop()
    redo_stack.push(undo2)
    print(f"Undid: {undo2}")
    
    print(f"\nUndo stack: {undo_stack}")
    print(f"Redo stack: {redo_stack}")
    
    # Redo once
    print("\n--- Pressing Redo ---")
    redo1 = redo_stack.pop()
    undo_stack.push(redo1)
    print(f"Redid: {redo1}")
    
    print(f"\nFinal undo stack: {undo_stack}")

def demo_balanced_brackets():
    """Demonstrate bracket matching"""
    print("\n=== Balanced Brackets Check ===")
    
    test_cases = [
        "({[]})",
        "({[}])",
        "((()))",
        "(((",
        ""
    ]
    
    for expr in test_cases:
        result = is_balanced_parentheses(expr)
        print(f"{expr:20} → {'✓ Balanced' if result else '✗ Unbalanced'}")


# Run demonstrations
if __name__ == "__main__":
    # Basic stack operations
    stack = ArrayStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Stack: {stack}")
    print(f"Pop: {stack.pop()}")
    print(f"Peek: {stack.peek()}")
    print(f"Size: {stack.size()}")
    
    # Run demos
    demo_undo_redo()
    demo_balanced_brackets()
    
    # Postfix evaluation
    print("\n=== Postfix Evaluation ===")
    expr = "3 4 + 2 *"
    result = evaluate_postfix(expr)
    print(f"'{expr}' = {result}")
```

## Time and Space Complexity

| Operation | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Push | O(1) | O(1) | Add to top |
| Pop | O(1) | O(1) | Remove from top |
| Peek/Top | O(1) | O(1) | View top without removing |
| Is Empty | O(1) | O(1) | Check if stack has elements |
| Size | O(1) | O(1) | If maintaining counter; O(n) if counting |
| Search | O(n) | O(1) | Must pop elements to search (not typical use) |
| Clear | O(1) | O(1) | Reset stack (Python list reassignment) |
| **Overall Space** | - | O(n) | Where n is number of elements in stack |

**Key Insight:** All primary stack operations (push, pop, peek) are O(1) constant time, making stacks extremely efficient for their intended use cases.

## When to Use

✅ **Use stacks when:**
- You need LIFO (Last-In-First-Out) access pattern
- Implementing undo/redo functionality
- Tracking function calls or recursion (call stack)
- Parsing nested structures (parentheses, HTML tags, expressions)
- Backtracking algorithms (maze solving, puzzle solving)
- Reversing data or order of operations
- Managing browser history (back/forward navigation)
- Depth-First Search (DFS) in graphs and trees
- Expression evaluation and conversion (infix, postfix, prefix)

❌ **Don't use stacks when:**
- You need random access to elements in the middle (use arrays)
- You need FIFO (First-In-First-Out) access (use queues instead)
- You need to access both ends frequently (use deque)
- You need to search elements frequently (use hash tables or trees)
- Order doesn't matter (use sets)

**Think Like a Programmer:** If your problem involves "most recent first," "nested structures," or "reversing," stacks are probably the right choice.

## Common Pitfalls

### 1. **Popping from Empty Stack (Underflow)**
Forgetting to check if stack is empty before popping causes runtime errors.
```python
# ❌ Wrong - crashes if stack is empty
def broken_pop(stack):
    return stack.pop()  # IndexError if empty!

# ✓ Correct - check first
def safe_pop(stack):
    if stack.is_empty():
        return None  # or raise meaningful error
    return stack.pop()
```

**Think Like a Programmer:** Always use `is_empty()` checks before pop or peek operations.

### 2. **Not Maintaining Stack Invariant**
Accidentally allowing access to middle elements breaks the stack abstraction.
```python
# ❌ Wrong - violates LIFO by accessing middle
stack.items[2] = 99  # Directly modifying internal array

# ✓ Correct - only use stack operations
stack.push(99)  # Add to top only
```

### 3. **Confusing Stack with Queue**
Using stack when you need FIFO behavior (or vice versa).
```python
# Problem: Process tasks in order received
tasks = Stack()
tasks.push("Task 1")
tasks.push("Task 2")
tasks.push("Task 3")

# ❌ Wrong - processes Task 3 first (LIFO)
while not tasks.is_empty():
    process(tasks.pop())  # Task 3, Task 2, Task 1

# ✓ Correct - use Queue for FIFO
from collections import deque
tasks = deque()
tasks.append("Task 1")
tasks.append("Task 2")
tasks.append("Task 3")
while tasks:
    process(tasks.popleft())  # Task 1, Task 2, Task 3
```

### 4. **Forgetting to Handle Edge Cases in Bracket Matching**
Not checking all bracket types or missing edge cases.
```python
# ❌ Wrong - only checks if counts match
def broken_balance(s):
    return s.count('(') == s.count(')')  # ")(" passes but is wrong!

# ✓ Correct - use stack to track order
def correct_balance(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return len(stack) == 0
```

### 5. **Inefficient Deep Copy**
Copying entire stack when you only need to preserve state.
```python
# ❌ Inefficient - copies all elements
def backup_stack(stack):
    backup = []
    for item in stack.items:  # O(n) copy
        backup.append(item)
    return backup

# ✓ Better - use list slicing or copy()
def backup_stack(stack):
    return stack.items.copy()  # O(n) but optimized in C

# ✓ Best - consider if you really need a copy
# Often you can just track operations instead
```

### 6. **Stack Overflow in Recursion**
Excessive recursive calls fill up the call stack.
```python
# ❌ Wrong - infinite recursion causes stack overflow
def broken_factorial(n):
    return n * broken_factorial(n - 1)  # No base case!

# ✓ Correct - always have base case
def factorial(n):
    if n <= 1:  # Base case prevents infinite recursion
        return 1
    return n * factorial(n - 1)

# ✓ Better for large n - use iteration instead
def iterative_factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result  # No call stack growth
```

## Practice Problems
Work through these problems to master stack operations:
- [Problem 1](./problem-1/problem1.md) - Basic stack implementation
- [Problem 2](./problem-2/problem2.md) - Balanced parentheses
- [Problem 3](./problem-3/problem3.md) - Stack reversal and manipulation
- [Problem 4](./problem-4/problem4.md) - Expression evaluation
- [Problem 5](./problem-5/problem5.md) - Monotonic stack problems
- [Problem 6](./problem-6/problem6.md) - Advanced stack applications

## Additional Resources
- [Visualgo: Stack Visualization](https://visualgo.net/en/list) - Interactive stack operations (select "Stack" mode)
- [Python Tutor](http://pythontutor.com/) - Step through stack code and see call stack
- [Stack vs Queue](https://www.youtube.com/watch?v=wjI1WNcIntg) - Understanding the differences
- [Module 00: Foundations](../00-foundations/) - Review Big-O notation
- [Linked Lists](../linked-lists/) - Alternative stack implementation using linked lists

---

**Next Steps:** After mastering stacks (LIFO), explore [Queues](../queues/) to understand the opposite principle: FIFO (First-In-First-Out)!
