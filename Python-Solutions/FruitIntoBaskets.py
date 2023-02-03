from typing import List
from collections import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        N = len(fruits)
        if N <= 2:
            return N
        types = Counter(fruits)
        if len(types) <= 2:
            return N
        basket = {}
        left = 0
        
        for right, fruit in enumerate(fruits):
            basket[fruit] = basket.get(fruit, 0) + 1
            if len(basket) > 2:
                basket[fruits[left]] -= 1

                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
        return right - left + 1
            