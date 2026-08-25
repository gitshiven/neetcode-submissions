# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Helper function - Yeh ek sath dono trees ke aamne-saamne wale nodes ko check karega
        def check(node1, node2):
            # Base Case 1: Agar dono nodes None hain, matlab yahan tak dono same hain
            if not node1 and not node2:
                return True
            
            # Base Case 2: Agar ek None hai aur dusra nahi, ya dono ki values alag hain
            # Matlab trees same nahi hain!
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            # Recursion: Ab dono ke Left children aur dono ke Right children ko sath mein check karo
            left_side  = check(node1.left, node2.left)
            right_side = check(node1.right, node2.right)
            
            # Agar left side bhi same hai AUR right side bhi same hai, toh hi True return hoga
            return left_side and right_side

        # Main Function se dono trees ke heads (roots) ko ek sath machine mein bhej diya
        return check(p, q)

        