# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        return dfs(root)

def dfs(tree):
    a = b = 0
    if tree.left is None and tree.right is None:
        return 1
    if tree.left:
        a = dfs(tree.left) + 1
    if tree.right:
        b = dfs(tree.right) + 1
    return max(a, b)