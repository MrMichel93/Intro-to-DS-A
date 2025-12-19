# Module 8: Graphs - Checkpoint Quiz

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
What is a graph?
- A) A linear data structure
- B) A collection of nodes connected by edges
- C) A sorted tree structure
- D) A type of hash table

### Question 2
In an undirected graph, if there's an edge between nodes A and B:
- A) You can only go from A to B
- B) You can only go from B to A
- C) You can go both from A to B and B to A
- D) Neither direction is allowed

### Question 3
What is the difference between a directed and undirected graph?
- A) Directed graphs have more nodes
- B) In directed graphs, edges have direction; in undirected graphs, they don't
- C) Directed graphs are faster
- D) There is no difference

### Question 4
What are two common ways to represent a graph?
- A) Array and linked list
- B) Adjacency matrix and adjacency list
- C) Stack and queue
- D) Tree and heap

### Question 5
What is the time complexity of checking if an edge exists between two nodes in an adjacency matrix?
- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n²)

### Question 6
Which traversal algorithm uses a queue?
- A) Depth-First Search (DFS)
- B) Breadth-First Search (BFS)
- C) Both DFS and BFS
- D) Neither DFS nor BFS

### Question 7
What data structure does DFS typically use?
- A) Queue
- B) Stack (or recursion)
- C) Array
- D) Hash table

### Question 8
In a weighted graph, edges have:
- A) Direction
- B) Colors
- C) Associated values (weights)
- D) Multiple connections

### Question 9
What is a cycle in a graph?
- A) A node that points to itself
- B) A path that starts and ends at the same node
- C) A disconnected component
- D) A weighted edge

### Question 10
Which algorithm is used to find the shortest path in an unweighted graph?
- A) DFS
- B) BFS
- C) Linear search
- D) Binary search

---

## Part 2: Code Analysis Questions (30 points, 10 points each)

### Question 11
What does this graph traversal do? Given graph: {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}, starting from node 0.

```python
from collections import deque

def traverse_graph(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result
```

**Your Answer:**
- What traversal algorithm is this? _______________
- Possible output for the given graph: _______________
- Time Complexity: _______________
- Space Complexity: _______________

### Question 12
Analyze this function. What does it detect?

```python
def detect_something(graph):
    visited = set()
    
    def dfs(node, parent):
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        
        return False
    
    for node in graph:
        if node not in visited:
            if dfs(node, -1):
                return True
    
    return False
```

**Your Answer:**
- What does this function detect? _______________
- Why does it check `neighbor != parent`? _______________________________________________
- Time Complexity: _______________

### Question 13
Find the issue in this adjacency list representation:

```python
def add_edge(graph, u, v, directed=False):
    if u not in graph:
        graph[u] = []
    graph[u].append(v)
    
    if not directed:
        if v not in graph:
            graph[v] = []
```

**Your Answer:**
- Bug: _______________________________________________
- When will this cause problems? _______________________________________________
- Corrected code: _______________________________________________

---

## Part 3: Short Answer Questions (30 points, 15 points each)

### Question 14
Compare and contrast Depth-First Search (DFS) and Breadth-First Search (BFS). Discuss their implementation, the order in which they explore nodes, and specific use cases where one is preferred over the other. (5-7 sentences)

**Your Answer:**
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

### Question 15
Explain how graphs can model real-world networks. Provide two specific examples (e.g., social networks, road maps) and describe what the nodes and edges represent in each case. What kind of graph operations would be useful for each application? (5-7 sentences)

**Your Answer:**
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________

---

**End of Quiz**

Submit your completed quiz to your instructor. Good luck!
