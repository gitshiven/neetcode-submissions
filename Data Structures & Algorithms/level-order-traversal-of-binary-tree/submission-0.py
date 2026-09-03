# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Base Case: Agar tree khali hai toh khali list return karo
        if not root:
            # Question ki demand List[List[int]] hai, isiliye [] return kiya
            return []
        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_level_values = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level_values.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level_values)
        return result


        