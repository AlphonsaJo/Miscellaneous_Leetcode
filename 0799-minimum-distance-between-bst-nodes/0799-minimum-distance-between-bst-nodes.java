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
    int min_val = Integer.MAX_VALUE;
    TreeNode prev = null;  

    public int minDiffInBST(TreeNode root) {
        find_min(root);
        return min_val;
    }

    private void find_min(TreeNode root) {
        if (root == null) return;

        find_min(root.left);

        
        if (prev != null) {
            min_val = Math.min(min_val, root.val - prev.val);
        }
        prev = root; 

        find_min(root.right);
    }
}
