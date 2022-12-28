from collections import List
import heapq
class Solution:
    # minStoneSum is solved in O(n+k log n) time and O(n) space.  The idea is to use a heap to keep track
    # of the largest piles.  We then iterate through k times, removing the largest pile, dividing it
    # by 2, and adding it back to the heap.  We then return the sum of the heap.
    # Since python does not have a max heap, we use a min heap and negate all the values.  This way,
    # the 'largest' value is at the top of the heap.
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-num for num in piles]
        heapq.heapify(heap)
        for i in range(k):
            curr = -heapq.heappop(heap)
            curr -= curr//2
            heapq.heappush(heap, -curr)
        return -sum(heap)