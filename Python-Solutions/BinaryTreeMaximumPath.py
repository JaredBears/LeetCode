# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum=float('-inf')
        def maxGain(node):
            nonlocal max_sum
            if not node:
                return 0
            left_gain = max(maxGain(node.left), 0)
            right_gain = max(maxGain(node.right), 0)
            newpath = node.val + left_gain + right_gain
            max_sum = max(max_sum, newpath)
            return node.val + max(left_gain, right_gain)
        maxGain(root)
        return max_sum
