'''Solution: Search in BST (Challenge 2)'''
def search_bst(root, val):
    if not root or root.val == val:
        return root
    return search_bst(root.left, val) if val < root.val else search_bst(root.right, val)
