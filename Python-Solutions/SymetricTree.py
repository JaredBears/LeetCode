from collections import deque
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
    # We can solve this problem either with dfs or bfs.  For this problem, I will use bfs.
    # We will use a queue to store the nodes.  We will append the root twice to the queue.
    # We will then pop the first two nodes from the queue.  If both nodes are None, we will continue.
    # If only one of the nodes is None, or if the values are different, we will return False.
    # Append the left child of the first node and the right child of the second node to the queue. (L R)
    # Append the right child of the first node and the left child of the second node to the queue. (R L)
    # If we reach the end of the queue, we will return True.
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque([root, root])
        while q:
            curr1 = q.popleft()
            curr2 = q.popleft()
            if not curr1 and not curr2:
                continue
            if not curr1 or not curr2 or curr1.val != curr2.val:
                return False
            q.append(curr1.left)
            q.append(curr2.right)
            q.append(curr1.right)
            q.append(curr2.left)
        return True