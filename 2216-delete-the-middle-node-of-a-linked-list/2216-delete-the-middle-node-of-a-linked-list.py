class Solution(object):
    def deleteMiddle(self, head):
        # Edge case: if there's only one node, return None
        if not head or not head.next:
            return None

        # Initialize slow and fast pointers
        slow = head
        fast = head
        prev = None

        # Move slow by 1 step and fast by 2 steps until fast reaches the end
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Delete the middle node by skipping the slow node
        prev.next = slow.next
        
        return head