'''Solution: Serialize and Deserialize Tree (Challenge 5)'''
class Codec:
    def serialize(self, root):
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
