from collections import deque
class Solution:
    # minKnightMoves is solved in O(max(|x|, |y|)^2) time and O(max(|x|, |y|)^2) space.  The idea is to use a BFS to find the shortest
    # path from (0, 0) to (x, y).  We use a queue to keep track of the current coordinates.  We then
    # iterate through the queue, and for each coordinate, we check if it is the target.  If it is, we
    # return the number of moves.  If it is not, we add all the possible moves to the queue and mark
    # them as visited.  We then increment the number of moves.

    def minKnightMoves(self, x: int, y: int) -> int:
        q = deque([(0, 0)])
        visited = set([(0, 0)])
        possibleMoves = [
            (-2, 1),
            (-1, 2),
            (1, 2),
            (2, 1),
            (2, -1),
            (1, -2),
            (-1, -2),
            (-2, -1)
        ]
        moves = 0
        while q:
            for i in range(len(q)):
                newX, newY = q.popleft()
                if newX == x and newY == y:
                    return moves
                for move in possibleMoves:
                    newCoord = (newX + move[0], newY + move[1])
                    if newCoord not in visited:
                        q.append(newCoord)
                        visited.add(newCoord)
            moves += 1