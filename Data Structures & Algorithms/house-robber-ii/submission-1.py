class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        def rob_linear(arr: List[int]) -> int:
            if not arr: 
                return 0
            if len(arr) == 1:
                return arr[0]
            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                dp[i] = max(arr[i] + dp[i-2], dp[i-1])

            return dp[len(arr) - 1]

        max_if_first_robbed = rob_linear(nums[0 : n - 1])

        max_if_first_not_robbed = rob_linear(nums[1:])

        return max(max_if_first_robbed, max_if_first_not_robbed)