class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.u = []

        def backtrack(start,path):
            # path.sort()
            if path not in self.u:
                self.u.append(path.copy())
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()
        nums.sort()
        backtrack(0,[])
        return self.u