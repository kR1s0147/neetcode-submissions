class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.u = []
        def backtrack(start,path):
            if sum(path) == target:
                self.u.append(path.copy())
                return
            if sum(path)>target:
                return
            for i in range(start,len(nums)):
                if sum(path) + nums[i]  > target:
                    continue
                else:
                    path.append(nums[i])
                    backtrack(i,path)
                    path.pop()
        backtrack(0,[])
        return self.u