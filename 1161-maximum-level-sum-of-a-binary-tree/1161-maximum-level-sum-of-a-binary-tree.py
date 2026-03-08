from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sum = []
        q = deque()
        sum.append(root.val)
        q.append(root)
        while(q):
            k = len(q)
            s = 0
            f = 0
            for i in range (k):
                t = q.popleft()
                if t.left:
                    f = 1
                    q.append(t.left)
                    s += t.left.val
                if t.right:
                    f = 1
                    q.append(t.right)
                    s += t.right.val
            if f: sum.append(s)
            else: sum.append(float("-inf"))
        
        return sum.index(max(sum)) + 1
            