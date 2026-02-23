# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return head
        even = ListNode()
        turn = -1
        b = even
        a = head
        while(a.next):
            t = a.next
            if t:
                a.next = t.next
                b.val = t.val
                b.next = ListNode()
                b = b.next
                if a.next:
                    a = a.next
        b = even
        while(b.next.next):
            b = b.next
        b.next = None
        a.next = even
        return head