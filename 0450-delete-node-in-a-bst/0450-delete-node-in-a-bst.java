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
    public TreeNode deleteNode(TreeNode root, int key) {
        
        if(root == null){
            return null;
        }

        if(root.val > key){
            root.left = deleteNode(root.left, key);
        }
        else if(root.val < key){
            root.right = deleteNode(root.right, key);
        }
        else{
            // Found a key
            // Found no children
            if(root.left == null && root.right == null){
                return null;
            }

            // Found one child
            if(root.left ==null){
                return root.right;
            }
            else if(root.right == null){
                return root.left;
            }

            // Found two children
            if(root.left != null && root.right != null){
                TreeNode Successor = findMin(root.right);
                root.val = Successor.val;
                root.right = deleteNode(root.right, Successor.val);
            }
        }

        return root;
    }

    // Helper Function
    TreeNode findMin(TreeNode node){
            while(node.left != null){
                node = node.left;
            }
            return node;
    }
}