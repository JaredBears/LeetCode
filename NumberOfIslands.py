# Runtime: 808 ms, faster than 47.66% of Python3 online submissions for Number
# of Islands.
# Memory Usage: 16.4 MB, less than 66.14% of Python3 online submissions for
# Number of Islands.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0
        # directions:
        # 0 : Right 0, +1
        # 1 : Down +1, 0
        # 2 : Left 0, -1
        # 3 : Up -1, 0
        def fill(r, c, direction):
            if grid[r][c] == "1":
                grid[r][c] = "0"
            else:
                return
            if r > 0 and direction != 1:
                fill(r - 1, c, 0)
            if r < len(grid) - 1 and direction != 0:
                fill(r + 1, c, 1)
            if c > 0 and direction != 3:
                fill(r, c - 1, 2)
            if c < len(grid[r]) - 1 and direction != 2:
                fill(r, c + 1, 3)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    answer += 1
                    fill(i, j, None)
        return answer
