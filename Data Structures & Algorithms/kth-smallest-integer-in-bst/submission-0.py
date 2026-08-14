# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.small = []

        def add(node):
            if not node:
                return 
            if node.left:
                add(node.left)
            self.small.append(node.val)
            if node.right:
                add(node.right)
            return
        add(root)
        return self.small[k-1]