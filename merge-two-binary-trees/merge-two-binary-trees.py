# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        r1,r2 = root1, root2
        if r1 and r2:
            node = TreeNode(r1.val + r2.val)
            node.left = self.mergeTrees(r1.left, r2.left)
            node.right = self.mergeTrees(r1.right, r2.right)
            
            return node
        else:
            return r1 or r2