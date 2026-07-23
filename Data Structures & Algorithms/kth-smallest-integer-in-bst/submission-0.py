# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        def dfs(root,ans):
            if not root:
                return 
            dfs(root.left, ans)
            ans.append(root.val)
            dfs(root.right, ans)

        dfs(root,ans)
        return ans[k-1]
            
