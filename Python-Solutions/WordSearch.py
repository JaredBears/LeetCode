from typing import List

class Solution:
    # Time Complexity: O(nm) where n is the size of the grid and m is the length of the word
    # Space Complexity: O(m) where for the set which will grow up to the length of the word and
    # the recursive stack which will also grow up to the length of the word
    # Backtracking Recursive Solution, DFS
    # First, we will iterate through the grid and find the first letter of the word
    # Then, we will call a helper function to check if the word exists starting from that letter
    # The helper function will check if the current letter is the next letter in the word
    # If it is, we will add the current position to the visited set and call the helper function
    # on the next adjacent letters in the grid
    # If the current letter is not the next letter in the word, or we have already visited the
    # current position, we will return False
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(i, j, visited = set()):
            if len(visited) == len(word):
                return True
            if board[i][j] != word[len(visited)] or (i, j) in visited:
                return False
            visited.add((i, j))
            up = down = left = right = False
            if i > 0:
                up = helper(i - 1, j, visited) # up
            if i < len(board) - 1:
                down = helper(i + 1, j, visited) # down
            if j > 0:
                left = helper(i, j - 1, visited) # left
            if j < len(board[i]) - 1:
                right = helper(i, j + 1, visited) # right
            visited.remove((i, j))
            return up or down or left or right
        for i, row in enumerate(board):
            for j, letter in enumerate(row):
                if letter == word[0]:
                    if len(word) == 1 or helper(i, j): return True
        return False