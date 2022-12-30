from typing import List
import heapq
class Solution:
    # For this problem, we can use a heap to keep track of the sticks we have
    # We can then merge the two smallest sticks and add the cost to the total
    # We can then add the merged stick back to the heap and repeat until we have one stick left
    # Time Complexity: O(nlogn) where n is the number of sticks
    def connectSticks(self, sticks: List[int]) -> int:
        cost = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            merged = heapq.heappop(sticks) + heapq.heappop(sticks)
            cost += merged
            heapq.heappush(sticks, merged)
        return cost