# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t = head
        cnt = 0

        while(t != None):
            t = t.next
            cnt += 1

        cnt //= 2
        t = head
        for i in range (cnt):
            t = t.next
        return t