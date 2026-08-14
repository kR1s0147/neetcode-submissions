class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(n):
            if n == 0:
                return 1
            elif n < 0:
                return 0
            return dp(n-1) + dp(n-2)

        return dp(n)