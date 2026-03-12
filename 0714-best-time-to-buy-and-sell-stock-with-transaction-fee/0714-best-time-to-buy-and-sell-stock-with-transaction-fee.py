class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold = -prices[0]
        free = 0

        for i in range (1, len(prices)):
            hold = max(hold, free - prices[i])
            free = max(free, hold + prices[i] - fee)
        return max(hold, free)