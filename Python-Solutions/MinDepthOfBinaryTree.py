class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def minDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    stack = [(1, root)]
    minDepth = float('inf')
    while stack:
        (depth, root) = stack.pop()
        children = [root.left, root.right]
        if not any(children):
            minDepth = min(depth, minDepth)
        for c in children:
            if c:
                stack.append((depth + 1, c))

    return minDepth

test = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
testTwo = TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6)))))

print(minDepth(test)==2)
print(minDepth(testTwo)==5)
