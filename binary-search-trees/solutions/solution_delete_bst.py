'''Solution: Delete Node in BST (Challenge 4)'''
def delete_node(root, key):
    if not root:
        return None
    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        min_node = find_min(root.right)
        root.val = min_node.val
        root.right = delete_node(root.right, min_node.val)
    return root

def find_min(node):
    while node.left:
        node = node.left
    return node
