from typing import List
class Solution:
    # This is a dynamic programming problem. We can solve it by using a bottom-up approach.
    # We can use two variables to keep track of the minimum cost to reach the two most recent steps.
    # We can then use these two variables to calculate the minimum cost to reach the next step.
    # We can then update the two variables to keep track of the minimum cost to reach the two most recent steps.
    # We can repeat this process until we reach the top of the staircase.
    # Time Complexity: O(n) where n is the number of steps in the staircase
    # Space Complexity: O(n)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        first = 0
        second = 0
        for i in range(2, N + 1):
            first, second = second, min((cost[i-1] + second), (cost[i-2] + first))
        return second