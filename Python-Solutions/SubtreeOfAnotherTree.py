from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        while stack:
            curr = stack.pop()
            if not curr:
                continue
            if curr.val == subRoot.val and self.sameTree(curr, subRoot):
                return True
            stack.extend([curr.left, curr.right])
        return False
            
        
        
    def sameTree(self, root1, root2):
        stack1 = [root1]
        stack2 = [root2]
        while stack1 or stack2:
            if not stack1 or not stack2:
                return False
            curr1 = stack1.pop()
            curr2 = stack2.pop()
            if not curr1 and not curr2:
                continue
            elif not curr1 or not curr2:
                return False
            if curr1.val != curr2.val:
                return False
            stack1.extend([curr1.left, curr1.right])
            stack2.extend([curr2.left, curr2.right])
        return True