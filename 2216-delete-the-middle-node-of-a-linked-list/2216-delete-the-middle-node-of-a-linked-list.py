class Solution(object):
    def deleteMiddle(self, head):
        # Edge case: if there's only one node, return None
        if not head or not head.next:
            return None
        
        # First, find the length of the list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Find the middle index
        middle_index = length // 2
        
        # Now, delete the middle node
        current = head
        prev = None
        for _ in range(middle_index):
            prev = current
            current = current.next
        
        # Remove the middle node by linking the previous node to the next node
        if prev:
            prev.next = current.next
        
        return head