class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        max_val = 0

        for price in prices:
            min_val = min(min_val, price)
            max_val = max(max_val, price - min_val)
        return max_val
             