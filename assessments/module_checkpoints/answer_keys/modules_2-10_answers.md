# Modules 2-10: Consolidated Answer Keys

This document provides answer keys for modules 2 through 10. For detailed explanations similar to modules 0 and 1, refer to those answer keys as examples.

---

## Module 2: Linked Lists - Answer Key

### Part 1: Multiple Choice (40 points)
1. **C** - Dynamic size and efficient insertion/deletion
2. **B** - Data and a pointer to the next node
3. **C** - O(n)
4. **A** - O(1)
5. **C** - Last node's next pointer
6. **B** - Each node has pointers to both next and previous nodes
7. **A** - O(1)
8. **B** - The last node points back to the first node
9. **B** - Use two pointers moving at different speeds (Floyd's algorithm)
10. **C** - Frequent insertions and deletions in the middle

### Part 2: Code Analysis (30 points)
11. Returns the data of the last node; O(n) time, O(1) space
12. Reverses the linked list; Final: 3 -> 2 -> 1 -> None; O(n) time
13. Bug: `current = new_node` should be `current.next = new_node`. Assignment doesn't link the node, just changes local variable.

### Part 3: Short Answer (30 points)
14. Key differences: Arrays use contiguous memory with O(1) access but O(n) insertion/deletion. Linked lists use scattered memory with O(n) access but O(1) insertion/deletion at known positions. Choose arrays for frequent random access; linked lists for frequent insertions/deletions.
15. Use two pointers: slow moves one step, fast moves two steps. When fast reaches end, slow is at middle. Time: O(n), Space: O(1).

---

## Module 3: Stacks - Answer Key

### Part 1: Multiple Choice (40 points)
1. **B** - LIFO (Last In, First Out)
2. **B** - push
3. **A** - O(1)
4. **C** - Raise an exception or error
5. **B** - Undo/Redo functionality in editors
6. **B** - Returns the top element without removing it
7. **C** - Both arrays and linked lists
8. **A** - Managing function calls and recursion
9. **C** - O(n)
10. **B** - Recursive function calls

### Part 2: Code Analysis (30 points)
11. Output: "olleh"; Reverses the string; O(n) time, O(n) space
12. Returns True; Returns False; Works by matching opening brackets with corresponding closing brackets using the stack.
13. Bug in peek(): Should be `return self.items[-1]` not `self.items[0]`. Peek should return the top (last element), not the bottom.

### Part 3: Short Answer (30 points)
14. When a function calls itself, the system pushes each call onto the call stack with its parameters and local variables. For factorial(3), it pushes factorial(3), factorial(2), factorial(1), then unwinds returning values. Too many recursive calls cause stack overflow.
15. Use two stacks: backStack and forwardStack. When clicking a link, push current page to backStack. Back button pops from backStack. Forward button pops from forwardStack and pushes to backStack.

---

## Module 4: Queues - Answer Key

### Part 1: Multiple Choice (40 points)
1. **A** - FIFO (First In, First Out)
2. **B** - enqueue
3. **A** - O(1)
4. **B** - Front
5. **C** - Print job scheduling
6. **B** - A queue where the rear wraps around to the beginning when space is available
7. **B** - Deques allow insertion and deletion at both ends
8. **A** - A queue where elements are served based on priority rather than arrival order
9. **B** - It requires shifting all remaining elements
10. **D** - Both arrays and linked lists

### Part 2: Code Analysis (30 points)
11. States: [1], [1,2], dequeue returns 1, queue=[2], [2,3]; dequeue() is O(n) due to pop(0)
12. Works by using two stacks to reverse order. Amortized O(1). Returns 1 (FIFO order).
13. Bug: self.size is never incremented in enqueue or decremented in dequeue. Add `self.size += 1` in enqueue and `self.size -= 1` in dequeue.

### Part 3: Short Answer (30 points)
14. Stacks use LIFO (undo/redo, function calls), queues use FIFO (task scheduling, BFS). Stacks push/pop from one end; queues enqueue at rear, dequeue from front. Both can be O(1) for main operations.
15. Use a priority queue with two priority levels: VIP calls get higher priority than regular calls. Within each priority level, maintain FIFO order using timestamps. Insert: O(log n), dequeue: O(log n) using a heap.

---

## Module 5: Hash Tables - Answer Key

### Part 1: Multiple Choice (40 points)
1. **A** - O(1)
2. **B** - A function that maps keys to array indices
3. **B** - When two different keys hash to the same index
4. **C** - Chaining
5. **B** - The ratio of stored elements to table capacity
6. **A** - A collision resolution technique that searches for the next available slot linearly
7. **B** - Distributes keys uniformly across the table
8. **C** - dict
9. **B** - More collisions occur, degrading performance
10. **B** - They must be hashable (immutable)

### Part 2: Code Analysis (30 points)
11. Output: {'apple': 3, 'banana': 2, 'cherry': 1}; Counts word frequency; O(n) time, O(n) space
12. Chaining (using lists at each index); Average: O(1), Worst: O(n); Uses separate chaining with linked lists.
13. Test: "aab" and "aba" returns True but should check if all counts are zero. Fix: Add check `return all(count == 0 for count in char_count.values())` after second loop.

### Part 3: Short Answer (30 points)
14. Hash tables achieve O(1) by directly computing the index using a hash function. Performance degrades to O(n) with poor hash functions causing many collisions, high load factors (>0.7), or when all keys hash to same location. Good hash functions distribute uniformly; appropriate load factors trigger resizing; efficient collision resolution maintains performance.
15. Combine a hash table for O(1) URL lookup with a doubly linked list to track access order (LRU). Hash table maps URL to list node; list maintains recency. When cache is full, remove least recently used (tail). Access moves node to head. All operations: O(1).

---

## Module 6: Trees - Answer Key

### Part 1: Multiple Choice (40 points)
1. **B** - Leaf
2. **B** - 0
3. **B** - 2
4. **B** - In-order
5. **A** - Pre-order
6. **B** - Queue
7. **D** - 2^(h+1) - 1
8. **B** - Full binary tree
9. **C** - O(n)
10. **B** - File system directories

### Part 2: Code Analysis (30 points)
11. Counts total nodes; Result: 3; O(n) time, O(h) space for recursion
12. Output: 1 2 3 4 5 6 7; In-order traversal; O(n) time
13. Bug: Should return `1 + max(left_height, right_height)`. Missing the +1 to count current node's level.

### Part 3: Short Answer (30 points)
14. Binary tree: no ordering constraint. BST: left < node < right for all nodes. BST ordering enables O(log n) search/insert/delete in balanced trees. Choose BST when you need ordered data or fast searches; regular tree for hierarchies without search requirements.
15. Pre-order (root, left, right): copying trees, serialization. In-order (left, root, right): BST traversal for sorted output. Post-order (left, right, root): deleting trees, postfix evaluation. Choice depends on whether you need to process node before, between, or after children.

---

## Module 7: Binary Search Trees - Answer Key

### Part 1: Multiple Choice (40 points)
1. **B** - Left child < node < right child
2. **B** - O(log n)
3. **B** - In-order
4. **C** - O(n)
5. **B** - At a leaf position
6. **B** - It degenerates into a linked list
7. **A** - The leftmost node in the right subtree or rightmost node in the left subtree
8. **B** - A self-balancing BST
9. **B** - The leftmost node
10. **D** - Finding all elements (traversal) is O(n)

### Part 2: Code Analysis (30 points)
11. Trace: root(5) -> left(3) -> right(4) -> returns True; O(log n) average, O(h) space
12. Tree structure: 5 at root, 3 left of 5, 7 right of 5, 1 left of 3, 4 right of 3, 6 left of 7, 9 right of 7; In-order: 1 3 4 5 6 7 9; Height: 2
13. Bug: `while root.right` should be `while root.left`. Minimum is in leftmost node, not rightmost.

### Part 3: Short Answer (30 points)
14. Unbalanced BSTs degrade to O(n) for all operations (like a linked list). Balance ensures height stays O(log n), maintaining efficient operations. AVL trees maintain balance through rotations after insertions/deletions, guaranteeing O(log n) performance. Self-balancing is crucial for consistent performance with arbitrary insertion orders.
15. Hash tables: O(1) average lookup but no ordering, no range queries. BSTs: O(log n) operations but maintain order, support range queries, enable min/max operations. Choose BST when you need sorted data, range queries, or predecessor/successor operations. Choose hash table for pure key-value lookup without ordering needs.

---

## Module 8: Graphs - Answer Key

### Part 1: Multiple Choice (40 points)
1. **B** - A collection of nodes connected by edges
2. **C** - You can go both from A to B and B to A
3. **B** - In directed graphs, edges have direction; in undirected graphs, they don't
4. **B** - Adjacency matrix and adjacency list
5. **A** - O(1)
6. **B** - Breadth-First Search (BFS)
7. **B** - Stack (or recursion)
8. **C** - Associated values (weights)
9. **B** - A path that starts and ends at the same node
10. **B** - BFS

### Part 2: Code Analysis (30 points)
11. BFS traversal; Possible output: [0, 1, 2, 3] or [0, 2, 1, 3]; O(V+E) time, O(V) space
12. Detects cycles in undirected graph; Checks to avoid going back to parent (which would falsely detect cycle); O(V+E) time
13. Bug: When not directed, after adding v to graph, should add `graph[v].append(u)` to complete the bidirectional edge.

### Part 3: Short Answer (30 points)
14. DFS uses stack/recursion, explores deeply before backtracking. BFS uses queue, explores level by level. DFS: better for topological sort, cycle detection, path finding. BFS: better for shortest path in unweighted graphs, level-order traversal. Space: DFS O(h), BFS O(w) where h=height, w=width.
15. Social networks: nodes=users, edges=friendships; operations include finding mutual friends (graph intersection), suggesting friends (finding nodes at distance 2). Road maps: nodes=intersections, edges=roads with weights=distance; operations include shortest path (Dijkstra's), finding all reachable locations (DFS/BFS).

---

## Module 9: Searching Algorithms - Answer Key

### Part 1: Multiple Choice (40 points)
1. **C** - O(n)
2. **B** - Sorted
3. **B** - O(log n)
4. **C** - The middle element
5. **A** - It checks fewer elements by eliminating half the search space each iteration
6. **A** - It returns -1 or None
7. **B** - Linear search
8. **A** - O(1)
9. **C** - Ternary search
10. **C** - About 10 (log₂ 1000 ≈ 10)

### Part 2: Code Analysis (30 points)
11. Iteration 1: left=0, right=7, mid=3, arr[3]=7 - Found! Return 3
12. Bug 1: Condition should be `left <= right` not `left < right` (misses single element case). Bug 2: Should be `left = mid + 1` not `left = mid` (infinite loop). These cause infinite loops or missing valid targets.
13. Both are equivalent and correct. Implementation B is slightly more Pythonic using enumerate. Time complexity is identical: O(n) for both.

### Part 3: Short Answer (30 points)
14. Binary search is O(log n) because it halves the search space each iteration. Linear search is O(n) because it checks each element once. For 1000 elements: binary search needs at most 10 comparisons (log₂ 1000 ≈ 10), linear search needs up to 1000 comparisons. For 1 million elements, binary search needs only 20 comparisons vs 1 million for linear search - exponential difference.
15. Use binary search since the list is sorted - O(log n) lookup is optimal. If unsorted, must use linear search O(n) unless you first sort the list. Trade-off: sorting takes O(n log n) one-time cost, then all searches are O(log n). For frequent searches, sorting once is worth it. For rare searches on unsorted data, linear search is simpler.

---

## Module 10: Sorting Algorithms - Answer Key

### Part 1: Multiple Choice (40 points)
1. **C** - O(n²)
2. **B** - Selection Sort
3. **B** - O(n log n)
4. **D** - Merge Sort
5. **C** - O(n)
6. **B** - Insertion Sort
7. **C** - O(n²)
8. **B** - It preserves the relative order of equal elements
9. **C** - Counting Sort
10. **B** - O(n log n)

### Part 2: Code Analysis (30 points)
11. Bubble Sort; After pass 1: [2,5,1,8,9], pass 2: [2,1,5,8,9], pass 3: [1,2,5,8,9]; O(n²)
12. Merge Sort; O(n log n) time, O(n) space; Yes, it's stable
13. Bug: Should be `arr[i], arr[min_idx] = arr[min_idx], arr[i]` not using j. The variable j is from inner loop and has wrong value.

### Part 3: Short Answer (30 points)
14. Merge Sort: O(n log n) all cases, O(n) space, stable. Quick Sort: O(n log n) average, O(n²) worst, O(log n) space, not stable. Quick Sort preferred because: better cache locality, in-place sorting, smaller constant factors. Choose Merge Sort when stability is required or guaranteed O(n log n) needed.
15. Choose Merge Sort because: (1) stability requirement - must preserve student ID order for equal GPAs, (2) O(n log n) guaranteed performance for 10,000 records, (3) O(n) space is acceptable for this size. Alternative: Timsort (Python's default) combines merge sort stability with insertion sort efficiency for partially sorted data.

---

**End of Consolidated Answer Keys**

## Notes for Instructors

- These answer keys provide correct answers and brief explanations
- For detailed grading rubrics, see modules 0 and 1 answer keys as examples
- Adjust point allocation based on your course requirements
- Consider the depth of explanation when grading short answer questions
- Code analysis questions should show understanding of both the code and complexity analysis

## Notes for Students

- Use these to check your understanding after completing quizzes
- Don't just memorize answers - understand the reasoning
- If your answer differs slightly but covers key concepts, it may still be correct
- Focus on understanding time/space complexity analysis principles
- Practice explaining concepts in your own words
