# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    m = float("-inf")
    ans = 0
    def goodNodes(self, root: TreeNode) -> int:
        if root is not None:
            t = self.m
            if self.m <= root.val:
                self.m = root.val
                self.ans += 1

            self.goodNodes(root.left)
            self.goodNodes(root.right)
            self.m = t
            return self.ans