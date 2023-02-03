from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count_stones = Counter(stones)
        count_jewels = 0
        for ch in jewels:
            count_jewels += count_stones[ch]
        return count_jewels