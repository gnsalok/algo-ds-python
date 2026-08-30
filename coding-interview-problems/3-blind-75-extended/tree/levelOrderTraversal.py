import collections

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        if root is None:
            return []

        q = collections.deque([root])
        result = []

        while q:
            elementsAtEachLevel = []

            # Freeze the number of nodes in current level
            for _ in range(len(q)):
                curr = q.popleft()

                elementsAtEachLevel.append(curr.val)

                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)

            result.append(elementsAtEachLevel)

        return result