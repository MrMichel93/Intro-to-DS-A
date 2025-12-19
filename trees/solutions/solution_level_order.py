"""
Solution: Binary Tree Level Order Traversal (Challenge 3)

Problem: Traverse tree level by level, returning values at each level as separate lists.

Approach: Use breadth-first search (BFS) with a queue. Process all nodes at current
level before moving to next level. Queue tracks nodes to visit, and we process
exactly one level per outer iteration.

Time Complexity: O(n) - visit each node once
Space Complexity: O(w) - queue holds at most one level, where w is maximum width
                  O(n) worst case for complete binary tree (last level has n/2 nodes)

Example:
    Tree:       3
               / \\
              9   20
                 /  \\
                15   7
    Output: [[3], [9, 20], [15, 7]]
"""

from collections import deque

def level_order(root):
    """
    Perform level-order traversal using BFS with queue.
    
    Args:
        root: TreeNode, root of binary tree
        
    Returns:
        list[list[int]]: values grouped by level
    """
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
