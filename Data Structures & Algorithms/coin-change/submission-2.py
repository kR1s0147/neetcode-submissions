class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def numcoins(s):
            if s == amount:
                return 0
            if s > amount:
                return float('inf')
            minCoins = float('inf')
            if s in dp:
                return dp[s]
            for coin in coins:
                c = numcoins(s+coin)
                if c!= float('inf'):
                    minCoins = min(c +1 ,minCoins)
            dp[s] = minCoins
            return minCoins
        res= numcoins(0)
        if res != float('inf'):
            return res
        return -1
        