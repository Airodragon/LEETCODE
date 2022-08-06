# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        total_paths = []
        if not root:
            return total_paths
        def helper(root,path,total_paths):
            path+=str(root.val)
            if(root.left==None and root.right==None):
                total_paths.append(path)
                return
            if(root.left!=None):
                helper(root.left,path+"->",total_paths)
            if(root.right!=None):
                helper(root.right,path+"->",total_paths)
            return total_paths
        helper(root,"",total_paths)
        return total_paths