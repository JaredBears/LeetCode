# Runtime: 57 ms, faster than 49.20% of Python3 online submissions for Pascal's
# Triangle.
# Memory Usage: 13.9 MB, less than 19.11% of Python3 online submissions for
# Pascal's Triangle.

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]] 
        numRows -= 1
        currentRow = 1
        while numRows > 0:
            currentRow += 1
            triangle.append([1] * currentRow)
            numRows -= 1

        for i in range(2, len(triangle)):
            for j in range(1, len(triangle[i]) - 1):
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
        return triangle
