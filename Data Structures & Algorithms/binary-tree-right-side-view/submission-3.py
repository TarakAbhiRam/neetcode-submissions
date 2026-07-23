# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q=  deque()
        q.append(root)

        ans = []

        while q:
            rightmost = None #almost like level order traversal
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    rightmost = node #after each iteration, it points rightmost one
                    q.append(node.left)
                    q.append(node.right)
            if rightmost:
                ans.append(rightmost.val)
        return ans
            
                