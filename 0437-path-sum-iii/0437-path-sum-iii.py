class Solution:

    def pathSum(self, root, targetSum):

        self.ans = 0

        # Counts all valid paths starting from the current node.
        def dfs(node, cur):

            if not node:
                return

            cur += node.val

            if cur == targetSum:
                self.ans += 1

            dfs(node.left, cur)
            dfs(node.right, cur)

        if not root:
            return 0

        stack = [root]

        # Every node becomes a starting point.
        while stack:

            node = stack.pop()

            dfs(node, 0)

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return self.ans