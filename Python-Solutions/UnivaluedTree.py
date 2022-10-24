# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def helper(node):
            if not node:
                return True
            if node.val == root.val:
                return True and helper(node.left) and helper(node.right)
            else:
                return False
        return helper(root.left) and helper(root.right)
