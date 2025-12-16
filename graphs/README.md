# Graphs

## What is a Graph?

A **graph** is a data structure consisting of:
- **Vertices (V)**: Nodes or points
- **Edges (E)**: Connections between vertices

```
    A --- B
    |     |
    |     |
    C --- D --- E

Vertices: {A, B, C, D, E}
Edges: {(A,B), (A,C), (B,D), (C,D), (D,E)}
```

## Why Graphs Matter

Graphs model relationships and networks:
- **Social networks** - Friends, followers
- **Maps** - Cities and roads (GPS navigation)
- **Web** - Pages and links (search engines)
- **Computer networks** - Routers and connections
- **Recommendation systems** - Users and preferences

## Types of Graphs

### 1. Undirected Graph
Edges have no direction (bidirectional).

```
A --- B    Can go A→B or B→A
```

### 2. Directed Graph (Digraph)
Edges have direction.

```
A → B      Can only go A→B
```

### 3. Weighted Graph
Edges have weights/costs.

```
A --5-- B    Cost of 5 to travel A↔B
|       |
3       2
|       |
C --4-- D
```

### 4. Cyclic vs Acyclic
- **Cyclic**: Contains cycles (paths back to starting node)
- **Acyclic**: No cycles (e.g., trees are acyclic graphs)

## Graph Representations

### 1. Adjacency Matrix
2D array where matrix[i][j] = 1 if edge exists.

```
Graph:     A-B-C        Matrix:   A B C
           |   |                A[0 1 0]
           D---+                B[1 0 1]
                               C[0 1 0]
                               D[0 1 1]
```

**Pros**: O(1) edge lookup  
**Cons**: O(V²) space

```python
# Create adjacency matrix
graph = [
    [0, 1, 0],  # A connects to B
    [1, 0, 1],  # B connects to A and C
    [0, 1, 0]   # C connects to B
]
```

### 2. Adjacency List
Dictionary mapping vertices to lists of neighbors.

```
Graph:     A-B-C        List:  A → [B]
           |   |               B → [A, C]
           D---+               C → [B, D]
                              D → [C]
```

**Pros**: O(V + E) space, efficient for sparse graphs  
**Cons**: O(V) edge lookup

```python
# Create adjacency list
graph = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C']
}
```

## Graph Traversals

### 1. Breadth-First Search (BFS)
Explore level by level (use queue).

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Time: O(V + E), Space: O(V)
```

**Use BFS for:**
- Shortest path in unweighted graphs
- Level-order traversal
- Finding connected components

### 2. Depth-First Search (DFS)
Explore as far as possible before backtracking (use stack/recursion).

```python
def dfs(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(vertex)
    print(vertex, end=' ')
    
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return visited

# Time: O(V + E), Space: O(V)
```

**Use DFS for:**
- Detecting cycles
- Topological sorting
- Pathfinding with backtracking

## Common Algorithms

### 1. Shortest Path (Dijkstra's)
Find shortest path in weighted graph.

```python
import heapq

def dijkstra(graph, start):
    distances = {v: float('inf') for v in graph}
    distances[start] = 0
    pq = [(0, start)]  # (distance, vertex)
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        if current_dist > distances[current]:
            continue
        
        for neighbor, weight in graph[current]:
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Time: O((V + E) log V)
```

### 2. Detect Cycle
```python
def has_cycle(graph):
    visited = set()
    rec_stack = set()
    
    def dfs(v):
        visited.add(v)
        rec_stack.add(v)
        
        for neighbor in graph[v]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True  # Back edge found!
        
        rec_stack.remove(v)
        return False
    
    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex):
                return True
    return False
```

### 3. Topological Sort
Order vertices in directed acyclic graph (DAG).

```python
def topological_sort(graph):
    visited = set()
    stack = []
    
    def dfs(v):
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(v)
    
    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)
    
    return stack[::-1]

# Use for: Task scheduling, dependency resolution
```

## Time Complexity

| Algorithm | Time Complexity |
|-----------|-----------------|
| BFS | O(V + E) |
| DFS | O(V + E) |
| Dijkstra | O((V + E) log V) |
| Bellman-Ford | O(V × E) |
| Floyd-Warshall | O(V³) |

## Real-World Applications

### 1. Social Networks
```
Users = Vertices
Friendships = Edges

Find mutual friends, suggest connections
```

### 2. GPS Navigation
```
Intersections = Vertices
Roads = Weighted Edges

Find shortest route
```

### 3. Web Crawling
```
Pages = Vertices
Links = Directed Edges

Search engines use BFS/DFS to index web
```

### 4. Recommendation Systems
```
Users/Items = Vertices
Interactions = Edges

"Users who liked X also liked Y"
```

### 5. Dependency Resolution
```
Tasks = Vertices
Dependencies = Directed Edges

Build systems, package managers
```

## Graph Problems Patterns

### Connected Components
How many separate sub-graphs?
```python
def count_components(graph):
    visited = set()
    count = 0
    
    for vertex in graph:
        if vertex not in visited:
            dfs(graph, vertex, visited)
            count += 1
    
    return count
```

### Bipartite Check
Can graph be colored with 2 colors?
```python
def is_bipartite(graph):
    color = {}
    
    def bfs(start):
        queue = deque([start])
        color[start] = 0
        
        while queue:
            v = queue.popleft()
            for neighbor in graph[v]:
                if neighbor not in color:
                    color[neighbor] = 1 - color[v]
                    queue.append(neighbor)
                elif color[neighbor] == color[v]:
                    return False
        return True
    
    for vertex in graph:
        if vertex not in color:
            if not bfs(vertex):
                return False
    return True
```

## Practice Problems

Master graphs with these problems:

1. **[Problem 1: Number of Islands](./problem1.md)** - Easy 🟢
2. **[Problem 2: Clone Graph](./problem2.md)** - Easy 🟢
3. **[Problem 3: Course Schedule](./problem3.md)** - Medium 🟡
4. **[Problem 4: Pacific Atlantic](./problem4.md)** - Medium 🟡
5. **[Problem 5: Network Delay Time](./problem5.md)** - Medium 🟡
6. **[Problem 6: Word Ladder](./problem6.md)** - Hard 🔴

## Next Steps

After graphs, dive into [Sorting Algorithms](../sorting-algorithms/) to learn efficient data organization!

---

💡 **Pro Tip**: Many graph problems can be solved with BFS or DFS. BFS finds shortest paths in unweighted graphs, while DFS is great for exploring all possibilities and detecting cycles!
