# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # 1. Find the middle
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 2. Split the list
        second = slow.next
        slow.next = None
        
        # 3. Reverse the second half (FIXED: cur init to second)
        cur = second
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        second = prev  # Head of the reversed second half
        
        # 4. Merge the halves alternatingly
        first = head
        while second:
            tmp1 = first.next
            tmp2 = second.next
            
            first.next = second
            second.next = tmp1
            
            first = tmp1
            second = tmp2
