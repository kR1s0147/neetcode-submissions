class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.u = []

        def backtrack(start,path):

            if sum(path) == target:
                path.sort()
                if path not in self.u:
                    self.u.append(path.copy())
                return
            if sum(path) > target:
                return

            for i in range(start,len(candidates)):
                path.append(candidates[i])
                backtrack(i+1,path)
                path.pop()

        backtrack(0,[])
        return self.u