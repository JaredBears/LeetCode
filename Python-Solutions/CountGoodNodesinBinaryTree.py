# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node, maxValue):
            if not node:
                return 0
            if node.val >= maxValue:
                return 1 + helper(node.left, node.val) + helper(node.right, node.val)
            else:
                return 0 + helper(node.left, maxValue) + helper(node.right, maxValue)
        return 1 + helper(root.left, root.val) + helper(root.right, root.val)
