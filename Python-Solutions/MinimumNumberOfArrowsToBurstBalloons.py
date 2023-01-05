from typing import List
class Solution:
    # First sort the points by their end points using a lambda function.
    # Then, initialize the number of arrows to 1 and the first end point.
    # Iterate through the points starting with the second point and if the
    # start point is greater than the first end point, increment the arrows
    # and set the first end point to the current end point.
    # Return the number of arrows.
    # Time complexity: O(nlogn)
    # Space complexity: O(1)
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sorting the points by their end points, time complexity: O(nlogn)
        points.sort(key = lambda x : x[1])
        arrows = 1
        first_end = points[0][1]
        # iteration through the points, time complexity: O(n)
        for i in range(1, len(points)):
            if points[i][0] > first_end:
                arrows += 1
                first_end = points[i][1]
        return arrows