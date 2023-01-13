from typing import List
from collections import defaultdict
class Solution:
    # This is a graph problem.  We will create an adjacency list, and then we will traverse the graph.
    # We will use DFS to traverse the graph.  We will keep track of the total time and the time for each child.
    # Time Complexity: O(n) where n is the number of nodes to traverse the tree
    # Space Complexity: O(n) to hold the adjacency list.
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjacency = defaultdict(set)
        # This function will traverse the graph and find the apples using DFS.
        # For each call, we will pass the node and it's parent node.  
        # We will need to keep track of the total time and the time for each child.
        def findApples(node: int, parent: int) -> int:
            child_time = total_time = 0
            if node not in adjacency:
                return 0
            for child in adjacency[node]:
                if child == parent:
                    continue
                child_time = findApples(child, node)
                if child_time > 0 or hasApple[child]:
                    total_time += child_time + 2
            return total_time
        for x, y in edges: 
            adjacency[x].add(y)
            adjacency[y].add(x)
        return findApples(0, -1)