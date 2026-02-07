# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t = head
        cnt = 1
        while t.next != None:
            cnt += 1
            t = t.next
        if cnt == 1: return None
        t = head
        cnt = cnt // 2
        cnt -= 1
        for i in range (cnt):
            t = t.next
        t.next = t.next.next
        return head