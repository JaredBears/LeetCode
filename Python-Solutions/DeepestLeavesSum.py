from collections import defaultdict
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # We will use a dictionary to store the leaves.  We will use dfs to traverse the tree.
    # If the node is None, we will return.
    # If the node is a leaf, we will append the value to the leaves dictionary at the current level.
    # We will then update the max level if the current level is greater than the max level.
    # We will call dfs on the children with the current level + 1.
    # We will return the sum of the leaves at the max level.
    max_level = 1
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        leaves = defaultdict(list)
        def dfs(node, level):
            if not node: 
                return
            if not node.left and not node.right:
                leaves[level].append(node.val)
                self.max_level = max(level, self.max_level)
            if node.right: 
                dfs(node.right, level + 1)
            if node.left:
                dfs(node.left, level + 1)
            pass
        dfs(root, 1)
        return sum(leaves[self.max_level])