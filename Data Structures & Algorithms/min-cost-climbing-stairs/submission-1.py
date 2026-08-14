class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        dp = [-1 ] * len(cost)
        def climb(n):
            if n == 0:
                return cost[0]
            if n < 0:
                return 0
            if dp[n] != -1:
                return dp[n]
            
            minCost = cost[n] + min(climb(n-1), climb(n-2))
            dp[n] = minCost
            return minCost

        return min(climb(len(cost)-1),climb(len(cost)-2))