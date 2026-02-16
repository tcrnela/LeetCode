# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        a = ListNode(head.val, None)
        while(head.next is not None):
            b = ListNode(head.next.val, a)
            a = b
            head = head.next
        return a