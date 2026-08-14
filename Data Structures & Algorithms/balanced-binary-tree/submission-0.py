# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isbalanced = True
        def checkHeight(node):
            if not node:
                return 0
            leftnode = checkHeight(node.left)
            rightnode = checkHeight(node.right)
            if abs(leftnode - rightnode) > 1:
                self.isbalanced = False
            return 1 + max(leftnode,rightnode)
        checkHeight(root)
        return self.isbalanced