'''Solution: Maximum Depth of Binary Tree (Challenge 1)'''
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
