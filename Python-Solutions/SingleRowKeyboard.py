class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        map = {}
        for i, c in enumerate(keyboard):
            map[c] = i
        moves = 0
        prev = 0
        for i, c in enumerate(word):
            moves += abs(map[c] - prev)
            prev = map[c]
        return moves
