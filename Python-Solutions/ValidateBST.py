# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node, min=float('-inf'), max=float('inf')):
            if not node:
                return True
            if node.val <= min or node.val >= max:
                return False
            return helper(node.left, min, node.val) and helper(node.right, node.val, max)
        return helper(root)
