from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        sc = defaultdict(int)
        fr = defaultdict(int)
        self.ans = 0
        def dfs(node):
            if node is None:
                return
            if sc[node] == 0:
                sc[node.left] = sc[node.right] = 1    
            elif fr[node] == 0:
                sc[node.left] = 1
                sc[node.right] = sc[node] + 1
            else:
                sc[node.right] = 1
                sc[node.left] = sc[node] + 1
            if sc[node] > self.ans:
                self.ans = sc[node]
            fr[node.left] = 0
            fr[node.right] = 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.ans