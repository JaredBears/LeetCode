from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # The solution is to use a queue to perform a level order traversal
    # We can use a queue to store the nodes in the tree and a count to keep track of the number of nodes
    # We can then iterate through the queue and pop the nodes and increment the count
    # We can then add the left and right children of the current node to the queue if they exist
    # We can then return the count
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        count = 0
        while q:
            curr = q.popleft()
            count += 1
            if curr.left: q.append(curr.left)
            if curr.right: q.append(curr.right)
        return count