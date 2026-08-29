# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSametree(s,t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            if s.val != t.val:
                return False
            
            return isSametree(s.left, t.left) and isSametree(s.right, t.right)

        def check(node):
            if not node:
                return False
            
            if isSametree(node, subRoot):
                return True
            
            return check(node.left) or check(node.right)
        return check(root)