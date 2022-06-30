# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.s = set()
        self.recover(root,0,self.s)

    #DFS O(N) time and O(N) space
    def recover(self,root,x,s):
        if root:
            root.val = x
            s.add(root.val)
            if root.left == None and root.right == None:
                return 

            if root.left:
                self.recover(root.left,2*x+1,s)

            if root.right:
                self.recover(root.right,2*x+2,s)

            return 

    #Searching in set is O(1) time and O(N) space
    def find(self, target: int) -> bool:
        return target in self.s


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)