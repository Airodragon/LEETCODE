# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==1:
            x = TreeNode(nums[0],None,None)
            return x
        nums.sort()
        def helper(nums,init,final):
            if len(nums)==0:
                return None
            mid = len(nums)//2
            temp = TreeNode(nums[mid],None,None)
            temp.left = helper(nums[:mid],0,len(nums[:mid])-1)
            temp.right = helper(nums[mid+1:],mid+1,len(nums[mid+1:])-1)
            return temp
        return helper(nums,0,len(nums)-1)
        
        
        