/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int s = 0;
    public int rangeSumBST(TreeNode r, int l, int h) {
        if (r==null) return s;
        if ((l<=r.val) && (h>=r.val)) s+=r.val;
        rangeSumBST(r.left,l,h);
        rangeSumBST(r.right,l,h);
        return s;
    }
}