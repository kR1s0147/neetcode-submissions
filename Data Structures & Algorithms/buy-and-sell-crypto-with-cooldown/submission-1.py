class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def trade(i,b):
            if  b >= len(prices) or i >= len(prices):
                return 0
            if b == -1:
                return trade(i+1,i)
            t = 0
            if prices[i] > prices[b]:
                t = prices[i] - prices[b]
            return max(trade(i+1,b),t + trade(i+2,-1))
        m = 0
        for i in range(len(prices)):
            m = max(m,trade(i,-1))
        return m