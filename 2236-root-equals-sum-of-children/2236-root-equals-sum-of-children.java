class Solution {
    public boolean checkTree(TreeNode r) {
        return r.left.val+r.right.val==r.val;
    }
}