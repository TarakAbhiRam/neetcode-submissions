# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxval):
            res = 0
            if not node:
                return 0

            if node.val >= maxval:
                res= 1
                maxval = node.val
            
            res += dfs(node.right, maxval)
            res += dfs(node.left , maxval)
            
            return res
        return dfs(root, root.val)