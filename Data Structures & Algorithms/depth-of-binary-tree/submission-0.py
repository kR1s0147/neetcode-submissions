# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        if not root:
            return 0
        l = 1
        stack.append((1,root))
        while stack:
            level , curr = stack.pop()
            if curr.left:
                stack.append((level+1,curr.left))
            if curr.right:
                stack.append((level+1,curr.right))
            l = max(l,level)
        return l