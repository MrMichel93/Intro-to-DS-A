'''Solution: Shortest Path in Binary Matrix (Challenge 6)
BFS to find shortest path in grid.'''

from collections import deque

def shortest_path_binary_matrix(grid):
    n = len(grid)
    if grid[0][0] or grid[n-1][n-1]:
        return -1
    
    queue = deque([(0, 0, 1)])
    grid[0][0] = 1
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    
    while queue:
        x, y, dist = queue.popleft()
        if x == n-1 and y == n-1:
            return dist
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                grid[nx][ny] = 1
                queue.append((nx, ny, dist + 1))
    return -1
