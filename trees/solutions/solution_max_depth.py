"""
Solution: Maximum Depth of Binary Tree (Challenge 1)

Problem: Find the maximum depth (longest path from root to leaf) of a binary tree.

Approach: Use recursive depth-first search. The depth of a tree is 1 + the maximum
depth of its subtrees. Base case: empty tree has depth 0.

Time Complexity: O(n) - visit each node once
Space Complexity: O(h) - recursion stack depth, where h is tree height
                  O(n) worst case for skewed tree, O(log n) for balanced tree

Example:
    Tree:     3
             / \
            9   20
               /  \
              15   7
    max_depth returns 3 (path 3 -> 20 -> 15 or 3 -> 20 -> 7)
"""

def max_depth(root):
    """
    Calculate maximum depth using recursive DFS.
    
    Args:
        root: TreeNode, root of binary tree
        
    Returns:
        int: maximum depth from root to deepest leaf
    """
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
