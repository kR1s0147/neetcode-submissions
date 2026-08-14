class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.u = []

        def backtrack(start,path):
            if len(path) == len(nums):
                self.u.append(path.copy())
            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    backtrack(i+1,path)
                    path.pop()

        backtrack(0,[])
        return self.u