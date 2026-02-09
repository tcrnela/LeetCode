from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return list()
        q = deque()
        ans = []
        depth = 0
        q.append((root, 0))
        ans.append(root.val)

        while q:
            t, d = q.popleft()
            if t.right is not None:
                if d+1 > depth: 
                    ans.append(t.right.val)
                    depth += 1
                q.append((t.right, d+1))
                if t.left is not None:
                    q.append((t.left, d+1))

            elif t.left is not None:
                if d+1 > depth: 
                    ans.append(t.left.val)
                    depth += 1
                q.append((t.left, d+1))
        
        return ans