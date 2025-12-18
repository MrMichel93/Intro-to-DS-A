# Binary Search Trees (BST)

## What is a Binary Search Tree?

A **Binary Search Tree** is a special type of binary tree that follows a specific ordering property:
- **Left subtree** contains only nodes with values **less than** the parent
- **Right subtree** contains only nodes with values **greater than** the parent
- Both left and right subtrees must also be BSTs

```
        8
       / \
      3   10
     / \    \
    1   6   14
       / \  /
      4  7 13

Left < Parent < Right (at every node!)
```

## Why BSTs Matter

BSTs combine the benefits of:
- **Binary search** - Fast lookups (O(log n) average)
- **Linked lists** - Dynamic sizing
- **Sorted order** - Inorder traversal gives sorted sequence

Used in:
- **Databases** - Indexing records
- **File systems** - Organizing files
- **Priority queues** - Efficient insert/extract-min
- **Auto-complete** - Prefix searching

## BST Property

For **every node**:
```
All values in LEFT subtree < Node value < All values in RIGHT subtree
```

### Valid BST:
```
    5
   / \
  3   7
 / \   \
1   4   9
```
✓ At node 5: left values (1,3,4) < 5 < right values (7,9)

### Invalid BST:
```
    5
   / \
  3   7
 / \   
1   6
```
✗ At node 5: 6 is in left subtree but 6 > 5!

## Implementation

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        """Insert a value into the BST"""
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_helper(self.root, value)
    
    def _insert_helper(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_helper(node.left, value)
        else:  # value >= node.value
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_helper(node.right, value)
    
    def search(self, value):
        """Search for a value in the BST"""
        return self._search_helper(self.root, value)
    
    def _search_helper(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_helper(node.left, value)
        else:
            return self._search_helper(node.right, value)
    
    def inorder(self, node):
        """Inorder traversal - gives sorted sequence"""
        if node:
            self.inorder(node.left)
            print(node.value, end=' ')
            self.inorder(node.right)
```

## Common Operations

### 1. Search
**Average: O(log n), Worst: O(n)**

```python
def search(node, target):
    if not node or node.value == target:
        return node
    
    if target < node.value:
        return search(node.left, target)
    return search(node.right, target)
```

### 2. Insert
**Average: O(log n), Worst: O(n)**

```python
def insert(node, value):
    if not node:
        return TreeNode(value)
    
    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    
    return node
```

### 3. Delete
**Average: O(log n), Worst: O(n)**

Three cases:
1. **Leaf node**: Simply remove
2. **One child**: Replace with child
3. **Two children**: Replace with inorder successor (or predecessor)

```python
def delete(node, value):
    if not node:
        return None
    
    if value < node.value:
        node.left = delete(node.left, value)
    elif value > node.value:
        node.right = delete(node.right, value)
    else:  # Found the node to delete
        # Case 1 & 2: Zero or one child
        if not node.left:
            return node.right
        if not node.right:
            return node.left
        
        # Case 3: Two children
        # Find inorder successor (min in right subtree)
        successor = find_min(node.right)
        node.value = successor.value
        node.right = delete(node.right, successor.value)
    
    return node

def find_min(node):
    while node.left:
        node = node.left
    return node
```

### 4. Find Min/Max
**O(h)** where h is height

```python
def find_min(node):
    while node.left:
        node = node.left
    return node.value

def find_max(node):
    while node.right:
        node = node.right
    return node.value
```

## Time Complexity

| Operation | Average | Worst Case |
|-----------|---------|------------|
| Search    | O(log n)| O(n)       |
| Insert    | O(log n)| O(n)       |
| Delete    | O(log n)| O(n)       |
| Find Min/Max | O(log n) | O(n)   |

**Worst case** occurs when tree becomes skewed (like a linked list).

## Balanced vs Unbalanced

### Balanced (Good! 🎉)
```
      4
     / \
    2   6
   / \ / \
  1  3 5  7
```
Height: O(log n)  
Operations: O(log n)

### Skewed (Bad! 😢)
```
1
 \
  2
   \
    3
     \
      4
```
Height: O(n)  
Operations: O(n) - No better than a linked list!

**Solution**: Self-balancing trees (AVL, Red-Black)

## Real-World Applications

### 1. Dictionary/Spell Checker
Fast word lookup and insertion.

### 2. Priority Queues
Efficiently get min/max element.

### 3. Range Queries
Find all values between X and Y:
```python
def range_query(node, low, high):
    if not node:
        return []
    
    result = []
    if low < node.value:
        result.extend(range_query(node.left, low, high))
    if low <= node.value <= high:
        result.append(node.value)
    if high > node.value:
        result.extend(range_query(node.right, low, high))
    
    return result
```

### 4. Databases
B-trees (generalized BSTs) for database indexing.

## BST vs Hash Table

| Feature | BST | Hash Table |
|---------|-----|------------|
| Lookup | O(log n) avg | O(1) avg |
| Sorted order | Yes | No |
| Range queries | Easy | Hard |
| Ordered traversal | O(n) | O(n log n) |

## Common Patterns

### Validate BST
```python
def is_valid_bst(node, min_val=float('-inf'), max_val=float('inf')):
    if not node:
        return True
    
    if not (min_val < node.value < max_val):
        return False
    
    return (is_valid_bst(node.left, min_val, node.value) and
            is_valid_bst(node.right, node.value, max_val))
```

### Kth Smallest Element
```python
def kth_smallest(root, k):
    stack = []
    current = root
    count = 0
    
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        count += 1
        if count == k:
            return current.value
        
        current = current.right
```

## Practice Problems

Each problem is organized in its own directory containing:
- `problemN.md` - Problem description and examples
- `problemN.py` - Python starter file with function stubs and comments
- `test_problemN.py` - Pytest test file for validation

Navigate to each Problem directory to access the files:

- [Problem 1](./Problem%201/problem1.md)
- [Problem 2](./Problem%202/problem2.md)
- [Problem 3](./Problem%203/problem3.md)
- [Problem 4](./Problem%204/problem4.md)
- [Problem 5](./Problem%205/problem5.md)
- [Problem 6](./Problem%206/problem6.md)

## Next Steps

After BSTs, explore [Graphs](../graphs/) for more complex relationships!

---

💡 **Pro Tip**: Remember the BST property applies to ENTIRE subtrees, not just immediate children. When validating a BST, track valid ranges for each node!
