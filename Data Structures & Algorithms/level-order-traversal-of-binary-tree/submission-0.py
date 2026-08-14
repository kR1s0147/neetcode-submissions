# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        levelnodes = {}
        Queue = []
        Queue.append((0,root))
        while Queue:
            level,node = Queue.pop(0)
            if level not in levelnodes.keys():
                levelnodes[level] = []
            levelnodes[level].append(node.val)
            if node.left:
                Queue.append((level+1,node.left))
            if node.right:
                Queue.append((level+1,node.right))
        return list(levelnodes.values())



         