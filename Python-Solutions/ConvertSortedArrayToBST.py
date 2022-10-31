# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(start = 0, end = len(nums)-1):
            if start > end:
                return None
            mid = start + (end-start)//2
            node = TreeNode(nums[mid])
            node.left = helper(start, mid-1)
            node.right = helper(mid + 1, end)
            return node
        return helper()
