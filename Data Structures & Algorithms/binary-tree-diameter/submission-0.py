# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(root):
            if not root:
                return 0
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            res[0] = max(res[0], left_height + right_height) # updated diameter
            return max(left_height, right_height) + 1 # return height
        
        dfs(root)
        return res[0]