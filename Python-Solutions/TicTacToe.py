from typing import List
class Solution:
    # Simulate the game
    # Time Complexity: O(1) because the game is always at most 9 moves long.
    # Technically it's θ(n) where n is the number of moves, but since n is always at most 9, it's O(1).
    # Space Complexity: O(1) because the grid is always 3x3.
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[None for _ in range(3)] for _ in range(3)]
        for i, move in enumerate(moves):
            row = move[0]
            column = move[1]
            if i % 2 == 0:
                grid[row][column] = "X"
            else:
                grid[row][column] = "O"
        for row in range(3):
            if grid[row][0] == grid[row][1] and grid[row][1] == grid[row][2]:
                if grid[row][0] == "X":
                    return "A"
                elif grid[row][0] == "O":
                    return "B"
        for column in range(3):
            if grid[0][column] == grid[1][column] and grid[1][column] == grid[2][column]:
                if grid[0][column] == "X":
                    return "A"
                elif grid[0][column] == "O":
                    return "B"
        if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]:
            if grid[0][0] == "X":
                return "A"
            elif grid[0][0] == "O":
                return "B"
        if grid[0][2] == grid[1][1] and grid[1][1] == grid [2][0]:
            if grid[0][2] == "X":
                return "A"
            elif grid[0][2] == "O":
                return "B"
        if len(moves) < 9:
            return "Pending"
        return "Draw"