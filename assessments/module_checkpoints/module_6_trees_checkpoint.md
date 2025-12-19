# Module 6: Trees - Checkpoint Quiz

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
In a tree data structure, what is a node with no children called?
- A) Root
- B) Leaf
- C) Branch
- D) Parent

### Question 2
What is the height of a tree with only a root node?
- A) -1
- B) 0
- C) 1
- D) Undefined

### Question 3
In a binary tree, each node can have at most how many children?
- A) 1
- B) 2
- C) 3
- D) Unlimited

### Question 4
What traversal visits nodes in this order: left subtree, root, right subtree?
- A) Pre-order
- B) In-order
- C) Post-order
- D) Level-order

### Question 5
What traversal visits nodes in this order: root, left subtree, right subtree?
- A) Pre-order
- B) In-order
- C) Post-order
- D) Level-order

### Question 6
Level-order traversal of a tree uses which data structure?
- A) Stack
- B) Queue
- C) Array
- D) Hash table

### Question 7
What is the maximum number of nodes in a binary tree of height h?
- A) h
- B) 2h
- C) 2^h
- D) 2^(h+1) - 1

### Question 8
A tree where every node has either 0 or 2 children is called:
- A) Complete binary tree
- B) Full binary tree
- C) Perfect binary tree
- D) Balanced binary tree

### Question 9
What is the time complexity of searching for a value in an unordered binary tree?
- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n²)

### Question 10
Which real-world structure is best modeled by a tree?
- A) Shopping cart
- B) File system directories
- C) Waiting line
- D) Social network connections

---

## Part 2: Code Analysis Questions (30 points, 10 points each)

### Question 11
What does this recursive function do? Trace it with a tree: 5 -> (3, 7) where 3 has no children and 7 has no children.

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def mystery_function(root):
    if root is None:
        return 0
    return 1 + mystery_function(root.left) + mystery_function(root.right)
```

**Your Answer:**
- What does this function calculate? _______________
- Result for the given tree: _______________
- Time Complexity: _______________
- Space Complexity (considering recursion stack): _______________

### Question 12
What order will nodes be printed? Given tree: 4 -> (2, 6) where 2 -> (1, 3) and 6 -> (5, 7)

```python
def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.val)
        print_tree(root.right)
```

**Your Answer:**
- Output sequence: _______________________________________________
- What traversal is this? _______________
- Time Complexity: _______________

### Question 13
Find the bug in this function that calculates tree height:

```python
def tree_height(root):
    if root is None:
        return 0
    
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    
    return max(left_height, right_height)
```

**Your Answer:**
- Bug: _______________________________________________
- Why this is incorrect: _______________________________________________
- Corrected code: _______________________________________________

---

## Part 3: Short Answer Questions (30 points, 15 points each)

### Question 14
Explain the difference between a binary tree and a binary search tree. Why is the ordering property of BSTs important? What advantage does it provide? Give an example of when you would choose a BST over a regular binary tree. (5-7 sentences)

**Your Answer:**
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

### Question 15
Describe the three main depth-first traversal methods (pre-order, in-order, post-order) and explain a practical use case for each. For example, when would you choose pre-order over in-order? (5-7 sentences)

**Your Answer:**
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

---

**End of Quiz**

Submit your completed quiz to your instructor. Good luck!
