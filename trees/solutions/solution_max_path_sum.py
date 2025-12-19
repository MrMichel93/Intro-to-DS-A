"""
Solution: Binary Tree Maximum Path Sum (Challenge 6)

Problem: Find the maximum sum of any path in a binary tree. A path can start
and end at any nodes, but must follow parent-child connections.

Approach: Use recursive DFS with global max tracker. For each node, calculate
max path sum that includes this node as the "highest" node in the path. This
sum is: left_max + right_max + node.val. Return to parent the max single-branch
sum: max(left_max, right_max) + node.val. Use max(0, child) to ignore negative paths.

Time Complexity: O(n) - visit each node once
Space Complexity: O(h) - recursion stack depth
                  O(n) worst case for skewed tree, O(log n) for balanced tree

Example:
    Tree:      -10
               /  \
              9   20
                 /  \
                15   7
    Max path: 15 -> 20 -> 7 = 42
"""

def max_path_sum(root):
    """
    Find maximum path sum using recursive DFS with global max tracking.
    
    Args:
        root: TreeNode, root of binary tree
        
    Returns:
        int: maximum path sum in tree
    """
    max_sum = float('-inf')
    
    def helper(node):
        nonlocal max_sum
        if not node:
            return 0
        # Ignore negative paths (take 0 instead)
        left = max(0, helper(node.left))
        right = max(0, helper(node.right))
        # Update global max with path through this node
        max_sum = max(max_sum, left + right + node.val)
        # Return max single-branch sum to parent
        return max(left, right) + node.val
    
    helper(root)
    return max_sum
