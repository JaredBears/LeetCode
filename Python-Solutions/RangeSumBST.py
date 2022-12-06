# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        answer = 0
        q = deque([root])
        while q:
            curr = q.popleft()
            if curr.val >= low and curr.val <= high:
                answer += curr.val
            if curr.left and curr.val >= low:
                q.append(curr.left)
            if curr.right and curr.val <= high:
                q.append(curr.right)
        return answer
