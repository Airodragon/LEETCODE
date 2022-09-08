# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        a = []
        def helper(a,root):
            if not root:
                return
            if root.left:
                helper(a,root.left)
            a.append(root.val)
            if root.right:
                helper(a,root.right)
            return
        helper(a,root)
        return a