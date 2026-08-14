class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.ways = 0
        def backtrack(i,s):
            if s == target and i == len(nums):
                self.ways+=1
            if i >= len(nums):
                return
            backtrack(i+1,s + nums[i])
            backtrack(i+1,s-nums[i])
        backtrack(0,0)
        return self.ways