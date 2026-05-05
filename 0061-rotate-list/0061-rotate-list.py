# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Find length and last node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # Step 2: Make it circular
        tail.next = head
        
        # Step 3: Reduce k
        k = k % length
        
        # Step 4: Find new tail (length - k - 1 steps)
        steps_to_new_tail = length - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
        
        # Step 5: Set new head and break circle
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head