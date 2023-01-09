from typing import List
from collections import Counter
from math import atan2

class Solution:
    # Base case: If there is only one point, return 1.
    # If there are more than two points, it is guaranteed or minimum will be 2, so initialize result to 2.
    # We can then iterate through the points.  For each point, we compare it to every other point.  We can
    # calculate the slope between the two points using the atan2 function.  We can then increment the counter
    # for that slope.  We can then update the result by taking the maximum of the result and the maximum of
    # the counter plus 1.
    # Time complexity: O(n^2) where n is the number of points
    # Space complexity: O(n)
    def maxPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        if N == 1:
            return 1
        result = 2
        for i in range(N):
            count = Counter()
            for j in range(N):
                if j != i:
                    count[atan2(points[j][1] - points[i][1],
                                   points[j][0] - points[i][0])] += 1
            result = max(result, max(count.values()) + 1)
        return result