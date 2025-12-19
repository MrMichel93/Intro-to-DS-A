# Linked Lists Module - Practice Challenges

These challenges will help you master linked list operations, including traversal, reversal, cycle detection, and two-pointer techniques.

## Challenge 1: Reverse Linked List (Beginner)

**Difficulty:** Beginner 🟢

**Objective**: Reverse a singly linked list iteratively or recursively.

**Expected Time Complexity**: O(n)
**Expected Space Complexity**: O(1) iterative, O(n) recursive

**Real-World Use Case**: Music streaming apps like Spotify use linked list reversal for the "Play Previous" functionality. When you play songs in a playlist and want to go backwards, the app reverses the playback order, implemented efficiently with linked list pointer manipulation.

### Problem Statement

Given the `head` of a singly linked list, reverse the list, and return the reversed list.

### Examples

**Example 1**:
```python
Input: head = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
```

**Example 2**:
```python
Input: head = [1, 2]
Output: [2, 1]
```

### Constraints

- 0 ≤ Number of nodes ≤ 5000
- -5000 ≤ Node.val ≤ 5000

### Hints

<details>
<summary>Hint 1</summary>
Use three pointers: previous, current, and next to reverse links iteratively.
</details>

<details>
<summary>Hint 2</summary>
For recursive approach, reverse the rest of the list first, then attach current node at the end.
</details>

---

## Challenge 2: Detect Cycle in Linked List (Beginner)

**Difficulty:** Beginner 🟢

**Objective**: Determine if a linked list has a cycle.

**Expected Time Complexity**: O(n)
**Expected Space Complexity**: O(1)

**Real-World Use Case**: Memory leak detection tools analyze object references in program memory. If objects form a cycle (A→B→C→A), they can't be garbage collected. Floyd's cycle detection algorithm helps identify these circular references, preventing memory leaks in applications.

### Problem Statement

Given `head`, the head of a linked list, determine if the linked list has a cycle. Return `true` if there is a cycle, `false` otherwise.

### Examples

**Example 1**:
```python
Input: head = [3, 2, 0, -4], pos = 1 (tail connects to node at index 1)
Output: True
```

**Example 2**:
```python
Input: head = [1, 2], pos = 0 (tail connects to head)
Output: True
```

### Constraints

- 0 ≤ Number of nodes ≤ 10⁴
- -10⁵ ≤ Node.val ≤ 10⁵
- pos is -1 or a valid index

### Hints

<details>
<summary>Hint 1</summary>
Use Floyd's Tortoise and Hare algorithm: two pointers moving at different speeds.
</details>

<details>
<summary>Hint 2</summary>
If slow and fast pointers meet, there's a cycle.
</details>

---

## Challenge 3: Merge Two Sorted Lists (Intermediate)

**Difficulty:** Intermediate 🟡

**Objective**: Merge two sorted linked lists into one sorted list.

**Expected Time Complexity**: O(n + m)
**Expected Space Complexity**: O(1)

**Real-World Use Case**: Database merge operations use linked list merging when combining sorted result sets from different indexes. For instance, when searching contacts by both name and company, the database merges two sorted lists efficiently without creating duplicate storage.

### Problem Statement

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

### Examples

**Example 1**:
```python
Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]
```

**Example 2**:
```python
Input: list1 = [], list2 = []
Output: []
```

### Constraints

- 0 ≤ Number of nodes ≤ 50
- -100 ≤ Node.val ≤ 100
- Both lists are sorted in non-decreasing order

### Hints

<details>
<summary>Hint 1</summary>
Use a dummy head node to simplify edge cases.
</details>

<details>
<summary>Hint 2</summary>
Compare heads of both lists and append smaller one to result.
</details>

---

## Challenge 4: Remove Nth Node From End (Intermediate)

**Difficulty:** Intermediate 🟡

**Objective**: Remove the nth node from the end of the list in one pass.

**Expected Time Complexity**: O(n)
**Expected Space Complexity**: O(1)

**Real-World Use Case**: Web browsers implement "Undo" functionality with linked lists. When you need to remove the nth most recent action (e.g., "undo the last 3 changes"), the browser efficiently removes the nth node from the end without traversing the entire history twice.

### Problem Statement

Given the head of a linked list, remove the nth node from the end and return its head.

### Examples

**Example 1**:
```python
Input: head = [1, 2, 3, 4, 5], n = 2
Output: [1, 2, 3, 5]
```

**Example 2**:
```python
Input: head = [1], n = 1
Output: []
```

### Constraints

- 1 ≤ Number of nodes ≤ 30
- 0 ≤ Node.val ≤ 100
- 1 ≤ n ≤ Number of nodes

### Hints

<details>
<summary>Hint 1</summary>
Use two pointers with n nodes gap between them.
</details>

<details>
<summary>Hint 2</summary>
When fast pointer reaches end, slow pointer is at the node before the one to remove.
</details>

---

## Challenge 5: Reorder List (Advanced)

**Difficulty:** Advanced 🔴

**Objective**: Reorder list nodes: L₀ → Lₙ → L₁ → Lₙ₋₁ → L₂ → Lₙ₋₂ → ...

**Expected Time Complexity**: O(n)
**Expected Space Complexity**: O(1)

**Real-World Use Case**: Card shuffling algorithms in online gaming platforms use list reordering. The "riffle shuffle" technique interleaves cards from two halves of the deck, implemented by finding the middle, reversing the second half, and merging alternately—exactly this reorder pattern.

### Problem Statement

Reorder the list to be on the following form: L₀ → Lₙ → L₁ → Lₙ₋₁ → L₂ → Lₙ₋₂ → ...
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

### Examples

**Example 1**:
```python
Input: head = [1, 2, 3, 4]
Output: [1, 4, 2, 3]
```

**Example 2**:
```python
Input: head = [1, 2, 3, 4, 5]
Output: [1, 5, 2, 4, 3]
```

### Constraints

- 1 ≤ Number of nodes ≤ 5 × 10⁴
- 1 ≤ Node.val ≤ 1000

### Hints

<details>
<summary>Hint 1</summary>
Break problem into three steps: 1) Find middle 2) Reverse second half 3) Merge alternately
</details>

<details>
<summary>Hint 2</summary>
Use slow/fast pointers to find the middle efficiently.
</details>

---

## Challenge 6: Merge K Sorted Lists (Advanced)

**Difficulty:** Advanced 🔴

**Objective**: Merge k sorted linked lists into one sorted list.

**Expected Time Complexity**: O(n log k) where n is total nodes, k is number of lists
**Expected Space Complexity**: O(k) for min-heap

**Real-World Use Case**: Log aggregation systems merge sorted log files from multiple servers. Each server produces chronologically sorted logs. The aggregator uses a min-heap (priority queue) to efficiently merge k sorted streams into one master timeline without loading all logs into memory.

### Problem Statement

You are given an array of k linked-lists `lists`, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.

### Examples

**Example 1**:
```python
Input: lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
Output: [1, 1, 2, 3, 4, 4, 5, 6]
```

**Example 2**:
```python
Input: lists = []
Output: []
```

### Constraints

- k == lists.length
- 0 ≤ k ≤ 10⁴
- 0 ≤ lists[i].length ≤ 500
- -10⁴ ≤ lists[i][j] ≤ 10⁴

### Hints

<details>
<summary>Hint 1</summary>
Use a min-heap to track the smallest current element across all k lists.
</details>

<details>
<summary>Hint 2</summary>
Extract minimum from heap, add to result, push next node from that list.
</details>

---

## Summary and Next Steps

These challenges covered:
- ✅ Pointer manipulation for reversal (Challenge 1)
- ✅ Two-pointer cycle detection (Challenge 2)
- ✅ Merging sorted structures (Challenge 3)
- ✅ Two-pointer with gap for nth from end (Challenge 4)
- ✅ Multi-step list transformation (Challenge 5)
- ✅ Heap-based k-way merge (Challenge 6)

### Key Lessons

1. **Two pointers solve many linked list problems** - Cycle detection, finding middle, nth from end
2. **Dummy nodes simplify edge cases** - No special handling for head changes
3. **Linked lists enable O(1) insertion/deletion** - Unlike arrays which need shifting
4. **Watch for null pointer errors** - Always check before dereferencing
5. **Recursive solutions mirror iterative** - Often cleaner but use O(n) call stack

### Ready for More?

- **[Trees](../trees/)** - Linked structures in multiple dimensions
- **[Graphs](../graphs/)** - Generalized connected nodes
- **[Hash Tables](../hash-tables/)** - Fast lookups with chaining

---

💡 **Remember**: Linked lists trade array's O(1) random access for O(1) insertion/deletion!
