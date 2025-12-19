"""
Solution: Lowest Common Ancestor (Challenge 4)

Problem: Find the lowest (deepest) common ancestor of two nodes in a binary tree.

Approach: Use recursive DFS. The LCA is the deepest node that has both p and q
in its subtrees. If current node is p or q, return it. If both subtrees return
non-null, current node is the LCA. Otherwise, return the non-null subtree.

Time Complexity: O(n) - may visit all nodes in worst case
Space Complexity: O(h) - recursion stack depth
                  O(n) worst case for skewed tree, O(log n) for balanced tree

Example:
    Tree:       3
               / \\
              5   1
             / \\ / \\
            6  2 0  8
              / \\
             7   4
    LCA(5, 1) = 3, LCA(5, 4) = 5
"""

def lowest_common_ancestor(root, p, q):
    """
    Find lowest common ancestor using recursive DFS.
    
    Args:
        root: TreeNode, root of binary tree
        p: TreeNode, first target node
        q: TreeNode, second target node
        
    Returns:
        TreeNode: lowest common ancestor of p and q
    """
    if not root or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left if left else right
