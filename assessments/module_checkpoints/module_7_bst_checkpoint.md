# Module 7: Binary Search Trees - Checkpoint Quiz

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
In a binary search tree, for any node:
- A) Left child > node > right child
- B) Left child < node < right child
- C) All children are equal to the node
- D) Children are randomly arranged

### Question 2
What is the time complexity of searching in a balanced BST?
- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n²)

### Question 3
What traversal of a BST gives elements in sorted order?
- A) Pre-order
- B) In-order
- C) Post-order
- D) Level-order

### Question 4
What is the worst-case time complexity of searching in an unbalanced BST?
- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n log n)

### Question 5
When inserting into a BST, where do you always insert?
- A) At the root
- B) At a leaf position
- C) In the middle
- D) Randomly

### Question 6
What happens to a BST if you insert elements in sorted order?
- A) It becomes perfectly balanced
- B) It degenerates into a linked list
- C) It becomes a complete tree
- D) Nothing special

### Question 7
To delete a node with two children in a BST, you typically replace it with:
- A) The leftmost node in the right subtree or rightmost node in the left subtree
- B) The root node
- C) Any random node
- D) A null value

### Question 8
What is an AVL tree?
- A) A binary tree
- B) A self-balancing BST
- C) An unbalanced BST
- D) A hash table variant

### Question 9
The minimum value in a BST is always found in:
- A) The root
- B) The leftmost node
- C) The rightmost node
- D) Any leaf node

### Question 10
Which operation is NOT typically O(log n) in a balanced BST?
- A) Search
- B) Insertion
- C) Deletion
- D) Finding all elements (traversal)

---

## Part 2: Code Analysis Questions (30 points, 10 points each)

### Question 11
What does this function do? Trace it with BST: 5 -> (3, 8) where 3 -> (1, 4) and 8 -> (None, 9), searching for 4.

```python
def search_bst(root, target):
    if root is None:
        return False
    
    if root.val == target:
        return True
    elif target < root.val:
        return search_bst(root.left, target)
    else:
        return search_bst(root.right, target)
```

**Your Answer:**
- Trace through the recursive calls: _______________________________________________
- What does search_bst(root, 4) return? _______________
- Time Complexity (average case): _______________
- Space Complexity: _______________

### Question 12
What will be the resulting BST after these operations?

```python
bst = None
values = [5, 3, 7, 1, 4, 6, 9]

for val in values:
    bst = insert_bst(bst, val)
```

Assuming standard BST insertion.

**Your Answer:**
- Draw or describe the tree structure: _______________________________________________
- What would in-order traversal print? _______________
- What is the height of this tree? _______________

### Question 13
Find the bug in this function that finds the minimum value in a BST:

```python
def find_min(root):
    if root is None:
        return None
    
    while root.right is not None:
        root = root.right
    
    return root.val
```

**Your Answer:**
- Bug: _______________________________________________
- Why this is wrong: _______________________________________________
- Corrected code: _______________________________________________

---

## Part 3: Short Answer Questions (30 points, 15 points each)

### Question 14
Explain why maintaining balance is important in a BST. What happens to the time complexity of operations when a BST becomes unbalanced? How do self-balancing trees like AVL trees address this issue? (5-7 sentences)

**Your Answer:**
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

### Question 15
Compare hash tables and binary search trees for storing and retrieving data. Discuss the advantages and disadvantages of each in terms of time complexity, ordering, and range queries. When would you choose a BST over a hash table? (5-7 sentences)

**Your Answer:**
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

---

**End of Quiz**

Submit your completed quiz to your instructor. Good luck!
