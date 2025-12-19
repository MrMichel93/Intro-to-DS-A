"""
Solution: Symmetric Tree (Challenge 2)

Problem: Check if a binary tree is symmetric around its center (mirror image).

Approach: Use recursive helper function to compare left and right subtrees.
Two trees are mirrors if: roots have same value, left subtree of one mirrors
right subtree of other, and vice versa.

Time Complexity: O(n) - visit each node once
Space Complexity: O(h) - recursion stack depth
                  O(n) worst case for skewed tree, O(log n) for balanced tree

Example:
    Symmetric:      1          Not Symmetric:    1
                   / \                          / \
                  2   2                        2   2
                 / \ / \                        \   \
                3  4 4  3                        3   3
"""

def is_symmetric(root):
    """
    Check if tree is symmetric using recursive mirror comparison.
    
    Args:
        root: TreeNode, root of binary tree
        
    Returns:
        bool: True if tree is symmetric, False otherwise
    """
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and 
                is_mirror(left.left, right.right) and 
                is_mirror(left.right, right.left))
    return is_mirror(root, root) if root else True
