class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def preorder(node):
            if not node:
                res.append('N')
            else:
                res.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        nodeValues = data.split(',')
        self.i = 0

        def construct():
            nodeVal = nodeValues[self.i]
            self.i += 1
            if nodeVal == 'N':
                return None
            node = TreeNode(int(nodeVal))
            node.left = construct()
            node.right = construct()
            return node
        
        return construct()