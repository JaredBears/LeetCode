from typing import List
class Solution:
    # First, we can find the maximum damage from each level and the total damage from all levels.
    # We then need to calculate how much armor we will have used.  This will either be the minimum
    # of the armor or the maximum damage.  We can then return the total damage minus the used armor
    # plus 1.
    # Time complexity: O(n) where n is the number of levels
    # Space complexity: O(1)
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        return 1 + sum(damage) - min(armor, max(damage))

# Broken down into multiple lines for each of understanding: 
    # def minimumHealth(self, damage: List[int], armor: int) -> int:
    #     max_damage = max(damage)
    #     total_damage = sum(damage)
    #     armor = min(armor, max_damage)
    #     return 1 + total_damage - armor