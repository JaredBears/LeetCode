from typing import List
class Solution:
    # For the basic solution, we can just check which node in the first edge is in the second edge.
    # If it is, then that is the center of the star graph.
    # This works because for the problem as given, the center node is the only node connected to 
    # more than one other node
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][1] in edges[1]:
            return edges[0][1]
        else:
            return edges[0][0]

    # For the advanced solution, we can use a dictionary to store the nodes that are connected to each
    # node. Then, we can iterate through the dictionary and find the node that is connected to every
    # other node.
    # This is needed if problem is not restricted to the center node being the only node
    # connected to more than one other node.
    # Time Complexity: O(n+k) where n is the number of edges and k is the number of nodes
    # Space Complexity: O(n+k)
    def findCenterAdvanced(self, edges: List[List[int]]) -> int:
        edgeMap = {}
        for edge in edges:
            edgeOne = edge[0]
            edgeTwo = edge[1]
            if edgeOne not in edgeMap:
                edgeMap[edgeOne] = set([edgeTwo])
            else:
                edgeMap[edgeOne].add(edgeTwo)
            if edgeTwo not in edgeMap:
                edgeMap[edgeTwo] = set([edgeOne])
            else:
                edgeMap[edgeTwo].add(edgeOne)
        for k, v in edgeMap.items():
            if len(v) == len(edgeMap) - 1:
                return k