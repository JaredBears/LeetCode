# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        answer = 0
        def helper(node):
            nonlocal answer
            if not node:
                return 0
            left_path = helper(node.left)
            right_path = helper(node.right)
            left_dir = right_dir = 0
            if node.left and node.val == node.left.val:
                left_dir = left_path + 1
            if node.right and node.val == node.right.val:
                right_dir = right_path + 1
            answer = max(answer, left_dir + right_dir)
            return max(left_dir, right_dir)
        helper(root)
        return answer