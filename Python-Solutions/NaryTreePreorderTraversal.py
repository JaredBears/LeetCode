"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return
        nodes = [root]
        answer = []
        while nodes:
            curr = nodes.pop()
            nodes.extend(reversed(curr.children))
            answer.append(curr.val)
        return answer
            
