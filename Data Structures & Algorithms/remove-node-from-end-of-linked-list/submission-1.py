# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        n = n
        def rec(head):
            nonlocal n
            if not head:
                return None

            head.next = rec(head.next)
            n -= 1
            if n == 0:
                return head.next
            return head
        
        return rec(head)
            
            
                

        