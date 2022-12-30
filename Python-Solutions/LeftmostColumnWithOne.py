from collections import List
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
class BinaryMatrix(object):
    def get(self, row: int, col: int) -> int:
        pass
    def dimensions(self) -> List[int]:
        pass

class Solution:
    # This problem is solved by performing a binary search on each row.
    # Since we're only worried about the leftmost column, we can use a
    # variable to keep track of the leftmost column we've found so far.
    # If we find a 1, we can perform a binary search on the row to see
    # if there's a 1 to the left of the current leftmost column. If there
    # is, we update the leftmost column. If there isn't, we can stop
    # searching that row.
    # We also keep track of whether or not we've found a 1 at all. If we
    # haven't, we return -1.
    # Time Complexity: O(nlogm) where n is the number of rows and m is the number of columns
    # Space Complexity: O(1)

    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        found = False
        def binarySearch(row, leftMost) -> int:
            nonlocal found
            if binaryMatrix.get(row, leftMost) == 1:
                found = True
                i = 0
                while i < leftMost:
                    mid = i + (leftMost - i)//2
                    if binaryMatrix.get(row, mid) == 1:
                        leftMost = mid
                    else:
                        i = mid + 1
            return leftMost
        dimensions = binaryMatrix.dimensions()
        rows, columns = dimensions[0], dimensions[1]
        leftMost = columns - 1
        for i in range(rows):
            leftMost = binarySearch(i, leftMost)
        if found: return leftMost
        return -1