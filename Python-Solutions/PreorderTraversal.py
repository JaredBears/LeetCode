from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # For preorder traversal, we visit the root, then the left subtree, then the right subtree.
    # We can do this recursively or iteratively.  For this problem, we will do it iteratively.
    # We will first declare two arrays, one to serve as the answer and one to serve as the stack.
    # If there is not a root, we return an empty array.  If there is a root, we initialize the stack
    # with the root.  We then loop through the stack until it is empty.  We pop the last element
    # from the stack and append it's value to the answer array.  We then check if the right child exists,
    # and if it does, we append it to the stack.  We then check if the left child exists, and if it does,
    # we append it to the stack.  We then return the answer array.
    # For pre-order traversal, we must add the right tree to the stack first, since we access the last
    # element.
    # Time complexity: O(n) where n is the number of nodes in the tree
    # Space complexity: O(n)
    def preorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        answer = []
        stack = [root]
        while stack:
            curr = stack.pop()
            answer.append(curr.val)
            if curr.right: stack.append(curr.right)
            if curr.left: stack.append(curr.left)
        return answer

    # For the recursive solution, we create a helper function that takes in a node.  We append the node's
    # value to the answer array.  We then check if the left child exists, and if it does, we call the
    # helper function on the left child.  We then check if the right child exists, and if it does, we
    # call the helper function on the right child.  We then return the answer array.
    # Unlike with the iterative approach, this time we will need to process the left child before the
    # right child.
    # Time complexity: O(n) where n is the number of nodes in the tree
    # Space complexity: O(n)
    def preorderTraversalRecursive(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def preorder(node: TreeNode) -> None:
            answer.append(node.val)
            if node.left: preorder(node.left)
            if node.right: preorder(node.right)
        if not root:
            return []
        preorder(root)
        return answer