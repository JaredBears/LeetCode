from typing import List
from collections import Counter
from functools import cache

class Solution:
    # Use dynamic programming to find the maximum amount of money that can be earned
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = Counter()
        max_number = 0
        # Create a dictionary of the points for each number
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)

        # @cache the function so that it doesn't have to be recalculated
        @cache
        def max_points(num):
            if num == 0:
                return 0
            if num == 1:
                return points[1]
            # The maximum points is the maximum of the previous number or the previous number plus the
            # points for the current number
            return max(max_points(num - 1), max_points(num - 2) + points[num])
        
        return max_points(max_number)