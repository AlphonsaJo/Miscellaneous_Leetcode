/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null || head.next == null) {
            return false;
        }

        ListNode slow = head;  // Moves one step at a time
        ListNode fast = head;  // Moves two steps at a time

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) {  // If they meet, there's a cycle
                return true;
            }
        }
        return false;  // If fast reaches the end, no cycle exists
    }
}
