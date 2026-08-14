class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.maxl = 0
        def backtrack(index,path):
            self.maxl = max(self.maxl,len(path))
            for i in range(index,len(nums)):
                if not path or nums[i] > path[-1]:
                    path.append(nums[i])
                    backtrack(i+1,path)
                    path.pop()
        backtrack(0,[])
        return self.maxl