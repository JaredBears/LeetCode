from  typing import List
class Solution:
    # This is essentially a sliding window problem that slides horizontally and vertically.
    # We will have four pointers, one for the start of the row, one for the end of the row, 
    # one for the start of the column, and one for the end of the column.
    # We will also create a return array "answer" and set it's length, as well as an idx 0.
    # While the idx is less than the length of the answer, we will run through four "for loops" - 
    # One for each direction.  After every single operation, we will increment the idx value.
    # After the right loop, we will increment the row_start
    # After the down loop, we will decrement the col_end
    # After the right loop, we will decrement the row_end
    # After the up loop, we will increment the col_start
    # If at any point we reach the end of the matrix (idx >= len(answer)) then we will break early.
    # Once we've reached the end of the while loop, we will return the answer array.
    # Time Complexity: O(n) where n is the total number of items.
    # Space Complexity: O(n)
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_start = 0
        col_start = 0
        row_end = len(matrix)
        col_end = len(matrix[0])
        answer = [0] * (row_end * col_end)
        idx = 0
        while idx < len(answer):
            # RIGHT LOOP
            for col in range(col_start, col_end):
                answer[idx] = matrix[row_start][col]
                idx += 1
            if idx >= len(answer): break
            row_start += 1
            # DOWN LOOP
            for row in range(row_start, row_end):
                answer[idx] =  matrix[row][col_end-1]
                idx += 1
            if idx >= len(answer): break
            col_end -= 1
            # LEFT LOOP
            for col in range(col_end - 1, col_start - 1, -1):
                answer[idx] = matrix[row_end-1][col]
                idx += 1
            if idx >= len(answer): break
            row_end -= 1
            # UP LOOP
            for row in range(row_end - 1, row_start - 1, -1):
                answer[idx] = matrix[row][col_start]
                idx += 1
            col_start += 1
        return answer   