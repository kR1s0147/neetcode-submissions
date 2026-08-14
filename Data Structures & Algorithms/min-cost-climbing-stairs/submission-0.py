class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        def climb(n):
            if n == 0:
                return cost[0]
            if n < 0:
                return 0
            return cost[n] + min(climb(n-1), climb(n-2))

        return min(climb(len(cost)-1),climb(len(cost)-2))