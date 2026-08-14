class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [-1] * len(nums)

        def rob(n):
            if n == 0:
                return nums[0]
            if n < 0:
                return 0
            if dp[n]!= -1:
                return dp[n]
            y= max(nums[n] + rob(n-2) , rob(n-1))
            dp[n] = y
            return y

        return rob(len(nums)-1)
