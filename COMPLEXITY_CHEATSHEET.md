# Time and Space Complexity Cheat Sheet

A quick reference guide for Big O notation, data structure complexities, and algorithm performance. Perfect for studying, interviews, and quick lookups!

---

## 📊 Big O Complexity Chart

### Growth Rates (Best to Worst)

```
Excellent    → O(1)         Constant
Good         → O(log n)     Logarithmic
Fair         → O(n)         Linear
Bad          → O(n log n)   Linearithmic
Horrible     → O(n²)        Quadratic
Terrible     → O(n³)        Cubic
Awful        → O(2ⁿ)        Exponential
Nightmare    → O(n!)        Factorial
```

### Visual Comparison

```
Operations for n = 1000:

O(1)        →           1 operation      ██
O(log n)    →          10 operations     ██
O(n)        →       1,000 operations     ████
O(n log n)  →      10,000 operations     ████████
O(n²)       →   1,000,000 operations     ████████████████████
O(2ⁿ)       → 1.07 × 10³⁰⁰ operations    💀 (impossible)
O(n!)       → 4.02 × 10²⁵⁶⁷ operations   💀💀💀 (universe killer)
```

---

## 📦 Data Structures

### Array / List

| Operation | Average | Worst Case | Space |
|-----------|---------|------------|-------|
| **Access** | O(1) | O(1) | O(n) |
| **Search** | O(n) | O(n) | - |
| **Insert (end)** | O(1) | O(n)* | - |
| **Insert (middle)** | O(n) | O(n) | - |
| **Delete (end)** | O(1) | O(1) | - |
| **Delete (middle)** | O(n) | O(n) | - |

*Amortized O(1) for dynamic arrays (Python lists)

**Best for:** Fast access by index, simple iteration  
**Avoid when:** Frequent insertions/deletions in middle

---

### Linked List

| Operation | Singly Linked | Doubly Linked | Space |
|-----------|---------------|---------------|-------|
| **Access** | O(n) | O(n) | O(n) |
| **Search** | O(n) | O(n) | - |
| **Insert (beginning)** | O(1) | O(1) | - |
| **Insert (end)** | O(n) / O(1)* | O(1) | - |
| **Insert (middle)** | O(n) | O(n) | - |
| **Delete (beginning)** | O(1) | O(1) | - |
| **Delete (end)** | O(n) / O(1)* | O(1) | - |
| **Delete (middle)** | O(n) | O(n) | - |

*O(1) if tail pointer is maintained

**Best for:** Frequent insertions/deletions at ends, unknown size  
**Avoid when:** Need random access by index

---

### Stack

| Operation | Time Complexity | Space |
|-----------|----------------|-------|
| **Push** | O(1) | O(n) |
| **Pop** | O(1) | - |
| **Peek/Top** | O(1) | - |
| **Search** | O(n) | - |

**Best for:** LIFO operations, recursion, undo/redo, parsing  
**Implementations:** Array-based, linked list-based

---

### Queue

| Operation | Time Complexity | Space |
|-----------|----------------|-------|
| **Enqueue** | O(1) | O(n) |
| **Dequeue** | O(1) | - |
| **Front** | O(1) | - |
| **Search** | O(n) | - |

**Best for:** FIFO operations, BFS, task scheduling  
**Implementations:** Array-based (circular), linked list-based

---

### Hash Table / Dictionary

| Operation | Average | Worst Case | Space |
|-----------|---------|------------|-------|
| **Search** | O(1) | O(n) | O(n) |
| **Insert** | O(1) | O(n) | - |
| **Delete** | O(1) | O(n) | - |

**Best for:** Fast lookups, counting, caching  
**Avoid when:** Need ordered data, memory is very limited  
**Worst case** occurs with many hash collisions

---

### Binary Search Tree (BST)

| Operation | Average | Worst Case | Balanced (AVL/Red-Black) | Space |
|-----------|---------|------------|--------------------------|-------|
| **Search** | O(log n) | O(n) | O(log n) | O(n) |
| **Insert** | O(log n) | O(n) | O(log n) | - |
| **Delete** | O(log n) | O(n) | O(log n) | - |
| **Min/Max** | O(log n) | O(n) | O(log n) | - |

**Best for:** Sorted data, range queries  
**Avoid when:** Data isn't comparable, need O(1) lookup  
**Note:** Worst case O(n) when tree becomes unbalanced (like a linked list)

---

### Heap (Binary Heap)

| Operation | Time Complexity | Space |
|-----------|----------------|-------|
| **Find Min/Max** | O(1) | O(n) |
| **Insert** | O(log n) | - |
| **Delete Min/Max** | O(log n) | - |
| **Build Heap** | O(n) | - |
| **Heapify** | O(log n) | - |

**Best for:** Priority queues, finding k smallest/largest elements  
**Types:** Min heap, max heap

---

### Graph

**Representation:**

| Representation | Space | Add Edge | Remove Edge | Check Edge | List Neighbors |
|----------------|-------|----------|-------------|------------|----------------|
| **Adjacency Matrix** | O(V²) | O(1) | O(1) | O(1) | O(V) |
| **Adjacency List** | O(V + E) | O(1) | O(E) | O(degree) | O(degree) |

**V** = vertices, **E** = edges

**Best for:**
- **Matrix:** Dense graphs, frequent edge checks
- **List:** Sparse graphs, memory efficiency

---

### Trie (Prefix Tree)

| Operation | Time Complexity | Space |
|-----------|----------------|-------|
| **Search** | O(m) | O(ALPHABET_SIZE × m × n) |
| **Insert** | O(m) | - |
| **Delete** | O(m) | - |
| **Prefix Search** | O(m) | - |

**m** = length of word/key, **n** = number of words

**Best for:** Autocomplete, spell check, IP routing  
**Avoid when:** Memory is limited (can be space-intensive)

---

## 🔍 Searching Algorithms

| Algorithm | Best Case | Average | Worst Case | Space | Notes |
|-----------|-----------|---------|------------|-------|-------|
| **Linear Search** | O(1) | O(n) | O(n) | O(1) | Works on unsorted data |
| **Binary Search** | O(1) | O(log n) | O(log n) | O(1) | Requires sorted data |
| **Jump Search** | O(1) | O(√n) | O(√n) | O(1) | Sorted data, better than linear |
| **Interpolation Search** | O(1) | O(log log n) | O(n) | O(1) | Uniformly distributed sorted data |
| **Exponential Search** | O(1) | O(log n) | O(log n) | O(1) | Unbounded/infinite lists |

**Quick Guide:**
- **Unsorted data** → Linear search
- **Sorted data, any size** → Binary search
- **Sorted, large dataset** → Jump/Interpolation search

---

## 🔄 Sorting Algorithms

### Comparison Sorts

| Algorithm | Best Case | Average | Worst Case | Space | Stable | Notes |
|-----------|-----------|---------|------------|-------|--------|-------|
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) | ✅ | Simple, rarely used in practice |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) | ❌ | Simple, rarely used |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | ✅ | Good for small/nearly sorted |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ | Consistent performance |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ | Fast average, used widely |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ | Good worst-case guarantee |
| **Tim Sort** | O(n) | O(n log n) | O(n log n) | O(n) | ✅ | Python/Java default |

### Non-Comparison Sorts

| Algorithm | Best Case | Average | Worst Case | Space | Notes |
|-----------|-----------|---------|------------|-------|-------|
| **Counting Sort** | O(n + k) | O(n + k) | O(n + k) | O(k) | Small range of integers |
| **Radix Sort** | O(nk) | O(nk) | O(nk) | O(n + k) | Fixed-length keys |
| **Bucket Sort** | O(n + k) | O(n + k) | O(n²) | O(n) | Uniformly distributed data |

**k** = range of input

**Quick Selection Guide:**

```
Small dataset (n < 50)          → Insertion Sort
Nearly sorted                   → Insertion Sort
Guaranteed O(n log n)           → Merge Sort or Heap Sort
Average case performance        → Quick Sort
Integers with small range       → Counting Sort
Need stable sort                → Merge Sort or Tim Sort
Memory constrained              → Heap Sort or Quick Sort
```

---

## 🌲 Tree Traversal Algorithms

| Algorithm | Time | Space | Use Case |
|-----------|------|-------|----------|
| **Pre-order (DLR)** | O(n) | O(h) | Copy tree, prefix expression |
| **In-order (LDR)** | O(n) | O(h) | BST sorted output |
| **Post-order (LRD)** | O(n) | O(h) | Delete tree, postfix expression |
| **Level-order (BFS)** | O(n) | O(w) | Level-by-level processing |

**h** = height of tree, **w** = maximum width

---

## 🗺️ Graph Algorithms

### Traversal Algorithms

| Algorithm | Time | Space | Use Case |
|-----------|------|-------|----------|
| **DFS (Depth-First Search)** | O(V + E) | O(V) | Path finding, topological sort, cycle detection |
| **BFS (Breadth-First Search)** | O(V + E) | O(V) | Shortest path (unweighted), level-order |

### Shortest Path Algorithms

| Algorithm | Time | Space | Graph Type | Notes |
|-----------|------|-------|------------|-------|
| **Dijkstra's** | O((V + E) log V) | O(V) | Weighted, non-negative | Single source shortest path |
| **Bellman-Ford** | O(V × E) | O(V) | Weighted, can have negative | Detects negative cycles |
| **Floyd-Warshall** | O(V³) | O(V²) | Weighted | All-pairs shortest path |
| **A*** | O(E) | O(V) | Weighted | Heuristic-based, optimal if admissible |

### Other Graph Algorithms

| Algorithm | Time | Space | Purpose |
|-----------|------|-------|---------|
| **Topological Sort** | O(V + E) | O(V) | DAG ordering |
| **Kruskal's MST** | O(E log E) | O(V) | Minimum spanning tree |
| **Prim's MST** | O((V + E) log V) | O(V) | Minimum spanning tree |
| **Union-Find** | O(α(n))* | O(n) | Connected components, cycle detection |

*α(n) = inverse Ackermann function (nearly constant)

---

## 💡 Quick Reference Rules

### When to Use What Data Structure

```
Need fast access by index?           → Array
Need fast insert/delete at ends?     → Linked List or Deque
Need LIFO (Last In First Out)?       → Stack
Need FIFO (First In First Out)?      → Queue
Need O(1) lookup by key?             → Hash Table
Need sorted data?                    → BST or Heap
Need hierarchical data?              → Tree
Need relationships/networks?         → Graph
Need prefix matching?                → Trie
Need priority-based access?          → Heap (Priority Queue)
```

### Common Complexity Patterns

**O(1) - Constant:**
- Array access by index
- Hash table operations (average)
- Stack push/pop
- Queue enqueue/dequeue

**O(log n) - Logarithmic:**
- Binary search
- Balanced BST operations
- Heap insert/delete

**O(n) - Linear:**
- Array/list traversal
- Linear search
- Best-case some sorting algorithms

**O(n log n) - Linearithmic:**
- Efficient sorting (merge, quick, heap)
- Building balanced BST

**O(n²) - Quadratic:**
- Simple sorting (bubble, selection, insertion)
- Nested loops over data

**O(2ⁿ) - Exponential:**
- Recursive fibonacci (naive)
- Subset generation
- Traveling salesman (brute force)

---

## 🎯 Interview Quick Tips

### Time Complexity Questions

**Can you improve this O(n²) solution?**
- Try using a hash table → O(n)
- Try sorting first → O(n log n)
- Try two pointers → O(n)

**Can you improve this O(n) solution?**
- Usually not, but check if O(log n) is possible with binary search
- Sometimes preprocessing can help

**Which is better: O(n log n) or O(n²)?**
- O(n log n) is always better for large n
- For very small n (< 10), O(n²) might be fine and simpler

### Space Complexity Questions

**Can you do it in O(1) space instead of O(n)?**
- Try modifying input in-place
- Use constant extra variables
- Consider iterative instead of recursive

**Is O(n) space acceptable here?**
- Usually yes for hash tables and arrays
- Sometimes you can trade time for space

### Red Flags in Interviews

**🚩 Bad Signs:**
- O(n³) or worse (there's usually a better way)
- O(2ⁿ) for small n might be okay, but mention it
- Not considering edge cases

**✅ Good Signs:**
- Starting with brute force, then optimizing
- Explaining trade-offs
- Analyzing both time and space
- Testing with examples

---

## 📈 Amortized Analysis

Some operations have different costs occasionally but average out to better complexity:

| Operation | Individual | Amortized |
|-----------|-----------|-----------|
| **Dynamic Array Append** | O(n) worst | O(1) average |
| **Hash Table Insert** | O(n) worst | O(1) average |
| **Union-Find** | O(log n) | O(α(n)) ≈ O(1) |

**When it matters:** 
- Discussing dynamic arrays (Python lists)
- Hash table performance
- Competitive programming

---

## 🖨️ Printable Quick Reference

### Big O Cheat Sheet (Summary)

```
┌──────────────────────────────────────────────────────────┐
│              DATA STRUCTURE COMPLEXITIES                 │
├─────────────┬─────────┬────────┬──────────┬─────────────┤
│ Structure   │ Access  │ Search │ Insert   │ Delete      │
├─────────────┼─────────┼────────┼──────────┼─────────────┤
│ Array       │ O(1)    │ O(n)   │ O(n)     │ O(n)        │
│ Stack       │ O(n)    │ O(n)   │ O(1)     │ O(1)        │
│ Queue       │ O(n)    │ O(n)   │ O(1)     │ O(1)        │
│ Hash Table  │ -       │ O(1)   │ O(1)     │ O(1)        │
│ BST (avg)   │ O(log n)│O(log n)│O(log n)  │ O(log n)    │
│ BST (worst) │ O(n)    │ O(n)   │ O(n)     │ O(n)        │
└─────────────┴─────────┴────────┴──────────┴─────────────┘

┌──────────────────────────────────────────────────────────┐
│                 SORTING ALGORITHMS                       │
├─────────────┬─────────┬──────────┬───────────┬──────────┤
│ Algorithm   │ Best    │ Average  │ Worst     │ Space    │
├─────────────┼─────────┼──────────┼───────────┼──────────┤
│ Bubble      │ O(n)      │ O(n²)      │ O(n²)       │ O(1)     │
│ Insertion   │ O(n)      │ O(n²)      │ O(n²)       │ O(1)     │
│ Selection   │ O(n²)     │ O(n²)      │ O(n²)       │ O(1)     │
│ Quick       │ O(n log n)│ O(n log n) │ O(n²)       │ O(log n) │
│ Merge       │ O(n log n)│ O(n log n) │ O(n log n)  │ O(n)     │
│ Heap        │ O(n log n)│ O(n log n) │ O(n log n)  │ O(1)     │
└─────────────┴─────────┴──────────┴───────────┴──────────┘

┌──────────────────────────────────────────────────────────┐
│                 GROWTH RATES                             │
├──────────┬────────────────────────────────────────────┬──┤
│ Notation │ Name                    │ Example           │
├──────────┼────────────────────────────────────────────┼──┤
│ O(1)       │ Constant               │ Array access      │
│ O(log n)   │ Logarithmic            │ Binary search     │
│ O(n)       │ Linear                 │ Array traversal   │
│ O(n log n) │ Linearithmic           │ Merge sort        │
│ O(n²)      │ Quadratic              │ Nested loops      │
│ O(2ⁿ)      │ Exponential            │ Fibonacci         │
│ O(n!)      │ Factorial              │ Permutations      │
└──────────┴────────────────────────────────────────────┴──┘
```

---

## 🔗 Related Resources

- [README.md](./README.md) - Course overview
- [LEARNING_PATH.md](./LEARNING_PATH.md) - Learning paths guide
- [INTERVIEW_PREP.md](./INTERVIEW_PREP.md) - Interview preparation
- [RESOURCES.md](./RESOURCES.md) - External resources
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/) - Interactive online version

---

## 📝 Notes

**Remember:**
1. **Big O describes upper bound** - worst case scenario
2. **Constants are dropped** - O(2n) becomes O(n)
3. **Smaller terms dropped** - O(n² + n) becomes O(n²)
4. **Consider both time AND space** complexity
5. **Average case often matters more** than worst case in practice

**For interviews:**
- Always state your assumptions
- Mention space complexity even if not asked
- Explain trade-offs between solutions
- Start with brute force, then optimize

**Pro tip:** Print this page and keep it handy while practicing problems! 🎯

---

*Last updated: 2024 | For the most current information, visit [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)*
