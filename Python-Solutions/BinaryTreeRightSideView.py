from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # We will use a breadth-first search to traverse the tree and keep track of the last node
    # we see on each level. We will use a queue to keep track of the nodes we have seen but not
    # yet visited. We will use a None value to mark the end of each level.
    # When we reach the end of the level, we will add the value of the last node we saw to our
    # answer list.
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q = deque([root, None])
        curr = root
        answer = []
        while q:
            prev, curr = curr, q.popleft()
            while curr:
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
                prev, curr = curr, q.popleft()
            answer.append(prev.val)
            if q: q.append(None)
        return answer