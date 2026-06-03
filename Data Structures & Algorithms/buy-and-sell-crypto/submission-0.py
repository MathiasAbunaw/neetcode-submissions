class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            for j in prices[i+1:]:
                if j > prices[i]:
                    cur = j - prices[i]
                    if cur > res:
                        res = cur
        return res
             