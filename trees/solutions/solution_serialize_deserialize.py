"""
Solution: Serialize and Deserialize Binary Tree (Challenge 5)

Problem: Design algorithm to serialize binary tree to string and deserialize back.

Approach: Use preorder traversal for serialization. Mark null nodes with '#'.
For deserialization, use iterator over split string and rebuild recursively
following same preorder pattern.

Serialization: "1,2,#,#,3,4,#,#,5,#,#" for tree:
       1
      / \
     2   3
        / \
       4   5

Time Complexity: O(n) for both serialize and deserialize
Space Complexity: O(n) - string storage and recursion stack

Key insight: Preorder traversal with null markers allows unique reconstruction.
"""

class Codec:
    """Codec to serialize/deserialize binary tree using preorder traversal."""
    
    def serialize(self, root):
        """
        Serialize tree to comma-separated string.
        
        Args:
            root: TreeNode, root of binary tree
            
        Returns:
            str: serialized representation
        """
        def helper(node):
            if not node:
                vals.append('#')
            else:
                vals.append(str(node.val))
                helper(node.left)
                helper(node.right)
        vals = []
        helper(root)
        return ','.join(vals)
    
    def deserialize(self, data):
        """
        Deserialize string back to binary tree.
        
        Args:
            data: str, serialized tree representation
            
        Returns:
            TreeNode: reconstructed tree root
        """
        def helper():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            return node
        vals = iter(data.split(','))
        return helper()
