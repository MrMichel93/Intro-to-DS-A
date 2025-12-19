'''Solution: Clone Graph (Challenge 2)'''
def clone_graph(node):
    if not node:
        return None
    visited = {}
    
    def dfs(node):
        if node in visited:
            return visited[node]
        clone = Node(node.val)
        visited[node] = clone
        clone.neighbors = [dfs(n) for n in node.neighbors]
        return clone
    
    return dfs(node)
