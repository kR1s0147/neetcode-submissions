class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        n = len(nums)
        prefix = subfix = 0
        for i in range(len(nums)):
            prefix = nums[i] * (prefix or 1)
            subfix = nums[n -1 -i] * (subfix or 1)
            res = max(res,max(prefix , subfix))
        return res