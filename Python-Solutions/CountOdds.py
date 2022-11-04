# Both solutions work in O(1) time, and both use the same arithmetic. The first
# is impressive because it's only in one line but the second is easier to read
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (((high - (high % 2)) - (low + (low % 2)))//2) + (high % 2) + (low % 2)

    def countOddsAlternate(self, low: int, high: int) -> int:
        answer = 0
        if low % 2 > 0:
            answer += 1
            low += 1
        if high % 2 > 0:
            answer += 1
            high -= 1
        answer = (high-low)//2
        return answer
