# Trees

## What is a Tree?

A **tree** is a hierarchical data structure consisting of nodes connected by edges. It starts with a **root** node and branches out to child nodes, forming a tree-like structure.

```
        A          ← Root
       / \
      B   C        ← Children of A
     / \   \
    D   E   F      ← Leaf nodes (no children)
```

## Why Trees Matter

Trees model hierarchical relationships naturally:
- **File systems** - Folders and files
- **HTML DOM** - Web page structure
- **Organization charts** - Company hierarchy
- **Decision trees** - AI and machine learning
- **Game trees** - Chess, tic-tac-toe move analysis

## Tree Terminology

- **Root**: Top node (no parent)
- **Parent**: Node with children
- **Child**: Node connected below another node
- **Leaf**: Node with no children
- **Sibling**: Nodes with the same parent
- **Depth**: Distance from root to node
- **Height**: Maximum depth in tree
- **Subtree**: Tree formed by a node and its descendants

```
        1          Depth 0 (Height 3)
       / \
      2   3        Depth 1
     / \
    4   5          Depth 2
   /
  6                Depth 3
```

## Types of Trees

### 1. Binary Tree
Each node has at most 2 children (left and right).

```
      1
     / \
    2   3
   / \
  4   5
```

### 2. Binary Search Tree (BST)
Binary tree where left < parent < right.

```
      8
     / \
    3   10
   / \    \
  1   6   14
     / \
    4   7
```

### 3. Balanced Tree
Height is O(log n) - e.g., AVL, Red-Black trees.

### 4. Complete Binary Tree
All levels filled except possibly the last (filled left to right).

### 5. Full Binary Tree
Every node has 0 or 2 children.

## Basic Structure

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Creating a tree:
#       1
#      / \
#     2   3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
```

## Tree Traversals

### 1. Inorder (Left → Root → Right)
```python
def inorder(node):
    if node:
        inorder(node.left)
        print(node.value)
        inorder(node.right)

# For BST, gives sorted order: 4, 2, 5, 1, 3
```

### 2. Preorder (Root → Left → Right)
```python
def preorder(node):
    if node:
        print(node.value)
        preorder(node.left)
        preorder(node.right)

# Useful for copying trees: 1, 2, 4, 5, 3
```

### 3. Postorder (Left → Right → Root)
```python
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value)

# Useful for deleting trees: 4, 5, 2, 3, 1
```

### 4. Level Order (Breadth-First)
```python
from collections import deque

def level_order(root):
    if not root:
        return
    
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Processes level by level: 1, 2, 3, 4, 5
```

## Common Operations

### Finding Height
```python
def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))
```

### Counting Nodes
```python
def count_nodes(node):
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)
```

### Finding Maximum
```python
def find_max(node):
    if not node:
        return float('-inf')
    return max(node.value, 
               find_max(node.left), 
               find_max(node.right))
```

### Searching
```python
def search(node, target):
    if not node:
        return False
    if node.value == target:
        return True
    return search(node.left, target) or search(node.right, target)
```

## Time Complexity

| Operation | Balanced Tree | Unbalanced Tree |
|-----------|---------------|-----------------|
| Search    | O(log n)      | O(n)            |
| Insert    | O(log n)      | O(n)            |
| Delete    | O(log n)      | O(n)            |
| Traversal | O(n)          | O(n)            |

## Real-World Applications

### 1. Expression Trees
Mathematical expressions:
```
       +
      / \
     *   3
    / \
   2   5

Represents: (2 * 5) + 3
```

### 2. File System
```
    root/
    ├── home/
    │   ├── user/
    │   │   ├── documents/
    │   │   └── photos/
    └── etc/
        └── config/
```

### 3. HTML DOM
```
<html>
  <head>
    <title>Page</title>
  </head>
  <body>
    <h1>Hello</h1>
    <p>World</p>
  </body>
</html>
```

### 4. Decision Trees
```
        Outlook?
       /    |    \
    Sunny Rain  Cloudy
     /       |       \
  Humidity Windy?   Play
   /   \    / \
High  Low Yes No
  |    |   |   |
Don't Play Don't Play
Play      Play
```

## Tree Properties

**For a binary tree with n nodes:**
- Minimum height: log₂(n)
- Maximum height: n - 1
- Maximum nodes at level L: 2^L
- Maximum nodes with height h: 2^(h+1) - 1

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

After understanding trees, explore [Binary Search Trees](../binary-search-trees/) for ordered data!

---

💡 **Pro Tip**: Most tree problems can be solved elegantly using recursion. Think about the base case (null node) and what to do at each node, then trust the recursion!
