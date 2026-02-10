# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.t = []
        self.dfs(root1)
        self.a = self.t
        self.t = []
        self.dfs(root2)
        if self.a == self.t: return True
        return False

    def dfs(self, root):
        if root.left:
            self.dfs(root.left)
        
        if root.right:
            self.dfs(root.right)

        if root.left is None and root.right is None:
            self.t.append(root.val)
            return