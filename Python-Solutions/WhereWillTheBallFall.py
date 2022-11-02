class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        answers = []
        def traverse(x, y, direction):
            if x < 0 or x >= len(grid[0]):
                return -1
            if y >= len(grid):
                return x
            yx = grid[y][x]
            if direction == 0:
                return traverse(x + yx, y, yx)
            if direction == yx:
                return traverse(x, y + 1, 0)
            return -1


        for i in range(len(grid[0])):
            answers.append(traverse(i, 0, 0))
        return answers
