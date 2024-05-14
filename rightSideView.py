from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        q.append(root)

        while q:
            rightSide = None
            qlen = len(q)

            for i in range(qlen):
                node = q.popleft()
                if node:
                    rightSide = node.val
                    q.append(node.left)
                    q.append(node.right)

            if rightSide is not None:
                res.append(rightSide)
        return res
