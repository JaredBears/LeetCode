class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = float('inf')

        for curPrice in prices:
            profit = curPrice - minPrice
            maxProfit = max(maxProfit, profit)
            minPrice = min(minPrice, curPrice)

        return maxProfit
