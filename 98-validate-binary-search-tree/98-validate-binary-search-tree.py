class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.pred = -float('inf')
        def recur(node):
            if not node:
                return True
            if not recur(node.left):
                return False
                
            if self.pred >= node.val:
                return False
            self.pred = node.val
            
            if not recur(node.right):
                return False
            
            return True
        
        return recur(root)