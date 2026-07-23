# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
 #integers cant be passed by refrence , instead use a mutable structure like 
        #use array
        self.count(root,res)
        return res[0]
        
    def count(self,root,res):
        if not root:
            return 0
        left = self.count(root.left,res)
        right = self.count(root.right,res)
        res[0]  = max(res[0],left+right)
        return 1 + max(left,right)
        
