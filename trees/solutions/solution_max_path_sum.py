'''Solution: Maximum Path Sum (Challenge 6)'''
def max_path_sum(root):
    max_sum = float('-inf')
    
    def helper(node):
        nonlocal max_sum
        if not node:
            return 0
        left = max(0, helper(node.left))
        right = max(0, helper(node.right))
        max_sum = max(max_sum, left + right + node.val)
        return max(left, right) + node.val
    
    helper(root)
    return max_sum
