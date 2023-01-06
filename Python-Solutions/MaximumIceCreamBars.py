from typing import List
import heapq
class Solution:
    # In order to solve for maximum number of ice cream bars, we need to take a greedy approach
    # First, we can convert the costs array to a min heap.  Then, iteratively pop off the smallest
    # cost.  If the cost is less than or equal to the number of coins, we can buy the ice cream bar
    # and subtract the cost from the number of coins.  If the cost is greater than the number of coins,
    # we can return the number of ice cream bars we have bought so far.  If we have iterated through 
    # the entire heap, we can return the number of ice cream bars we have bought.
    # Time Complexity: O(nlogn) where n is the length of the costs array
    # Space Complexity: O(1)
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        heapq.heapify(costs)
        answer = 0
        while costs:
            cost = heapq.heappop(costs)
            if cost <= coins:
                coins -= cost
                answer += 1
            else:
                return answer
        return answer