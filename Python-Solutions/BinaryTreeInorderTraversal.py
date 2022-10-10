class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversalRecurse(root: TreeNode) -> list[int]:
    answer = []
    def helper(root):
        if(not root or root == None): return
        if(root.left): helper(root.left)
        answer.append(root.val)
        if(root.right): helper(root.right)
    helper(root)
    return answer

testTreeOne = TreeNode(1, None, TreeNode(2, TreeNode(3)))
testTreeTwo = TreeNode()
testTreeThree = TreeNode(1)

print(inorderTraversalRecurse(testTreeOne))
print(inorderTraversalRecurse(testTreeTwo))
print(inorderTraversalRecurse(testTreeThree))
