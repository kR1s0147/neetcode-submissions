# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.isSame = True
        def checkTrees(node1,node2):
            if (not node1 and node2) or (node1 and not node2) :
                self.isSame = False
                return
            if node1 and node2 and node1.val != node2.val:
                self.isSame = False
            if node1 and node2:    
                checkTrees(node1.left,node2.left)
                checkTrees(node1.right,node2.right)
        checkTrees(p,q)
        return self.isSame