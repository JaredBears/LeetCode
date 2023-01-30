from typing import List
class Solution:
    # If the rectangles overlap, we should be able to acquire the coordinates of the intersection
    # If the intersection is a rectangle, we can return True
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1 = max(rec1[0], rec2[0])
        x2 = min(rec1[2], rec2[2])
        y1 = max(rec1[1], rec2[1])
        y2 = min(rec1[3], rec2[3])
        return x1 < x2 and y1 < y2