# Linked Lists

## What is a Linked List?

A **linked list** is a linear data structure where elements are stored in nodes. Unlike arrays, elements are not stored in contiguous memory locations. Each node contains:
- **Data**: The value being stored
- **Next**: A reference (or pointer) to the next node

Think of it like a treasure hunt where each clue points you to the next location!

## Why Linked Lists Matter

Linked lists are useful when:
- You don't know how much data you'll need to store
- You frequently insert or delete elements
- You don't need random access to elements
- Memory is fragmented (non-contiguous allocation is okay)

## Types of Linked Lists

### 1. **Singly Linked List**
Each node points to the next node only.
```
[Data|Next] → [Data|Next] → [Data|Next] → null
```

### 2. **Doubly Linked List**
Each node points to both next and previous nodes.
```
null ← [Prev|Data|Next] ↔ [Prev|Data|Next] ↔ [Prev|Data|Next] → null
```

### 3. **Circular Linked List**
The last node points back to the first node.
```
[Data|Next] → [Data|Next] → [Data|Next] ⤴
     ↑___________________________________|
```

## Basic Structure

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
```

## Common Operations

### Traversal
Visit each node from head to end.

**Time Complexity: O(n)**

```python
def traverse(self):
    current = self.head
    while current:
        print(current.data)
        current = current.next
```

### Insertion at Beginning
**Time Complexity: O(1)**

```python
def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
```

### Insertion at End
**Time Complexity: O(n)** - Must traverse to end

```python
def insert_at_end(self, data):
    new_node = Node(data)
    if not self.head:
        self.head = new_node
        return
    
    current = self.head
    while current.next:
        current = current.next
    current.next = new_node
```

### Deletion
**Time Complexity: O(n)** - Must find the node

```python
def delete_node(self, key):
    current = self.head
    
    # If head needs to be deleted
    if current and current.data == key:
        self.head = current.next
        return
    
    # Find the node to delete
    prev = None
    while current and current.data != key:
        prev = current
        current = current.next
    
    # If not found
    if not current:
        return
    
    # Unlink the node
    prev.next = current.next
```

### Search
**Time Complexity: O(n)**

```python
def search(self, key):
    current = self.head
    while current:
        if current.data == key:
            return True
        current = current.next
    return False
```

## Linked Lists vs Arrays

| Feature | Array | Linked List |
|---------|-------|-------------|
| Memory | Contiguous | Scattered |
| Size | Fixed | Dynamic |
| Access Time | O(1) | O(n) |
| Insert at Start | O(n) | O(1) |
| Insert at End | O(1) | O(n)* |
| Memory Usage | Compact | Extra space for pointers |

\* O(1) if we keep a tail pointer

## Real-World Applications

1. **Music Playlists** - Next/previous song functionality
2. **Browser History** - Back/forward navigation
3. **Undo Functionality** - Sequence of actions
4. **Image Viewer** - Navigate through photos
5. **Blockchain** - Each block links to the next

## Common Techniques

### Two Pointer Technique
Use fast and slow pointers for problems like:
- Finding the middle of a list
- Detecting cycles
- Finding the nth node from the end

### Dummy Node
Use a dummy head node to simplify edge cases in insertion/deletion.

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

Once you master linked lists, move on to [Stacks](../stacks/), which can be implemented using linked lists!

---

💡 **Pro Tip**: Draw pictures! Linked list problems are much easier to solve when you visualize the pointer changes on paper first.
