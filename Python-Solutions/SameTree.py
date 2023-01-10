# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # For this problem, we need to simultaneously traverse both trees.  Basically any traversal
    # method will work for this problem.
    # In this case, I chose to use preorder traversal.
    # I first initialized two stacks, one for each tree.  I then used iterative preorder traversal
    # on each tree.  At each step, I checked to see if the value is the same, and if not, I return False
    # Then, I check to see if they both have a right child and/or a left child.  If the structure
    # doesn't match, I return false.  If it does, I add the right and left children to their respective
    # stacks.  
    # Once I reach the end of the loop, if one stack still has children to process then I return False.
    # If not, I return because I reached the end without finding any differences.
    # Time Complexity: O(n) where n is the number of nodes in the smallest tree.
    # Space Complexity: O(n)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q or not p:
            if p or q:
                return False
            return True
        pstack = [p]
        qstack = [q]
        while pstack and qstack:
            currq = qstack.pop()
            currp = pstack.pop()
            if currp.val != currq.val:
                return False
            if currq.right or currp.right:
                if not currq.right or not currp.right:
                    return False
                qstack.append(currq.right)
                pstack.append(currp.right)
            if currq.left or currp.left:
                if not currq.left or not currp.left:
                    return False
                qstack.append(currq.left)
                pstack.append(currp.left)
        if pstack or qstack:
            return False
        return True