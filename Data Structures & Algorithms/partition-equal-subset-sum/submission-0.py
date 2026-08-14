class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum %2 == 1:
            return False
        target = totalSum // 2
        def backtrack(i , path):
            if sum(path) == target:
                return True
            if sum(path) > target:
                return False
            for j in range(i,len(nums)):
                path.append(nums[j])
                if backtrack(j+1,path):
                    return True
                path.pop()
            return False
        return backtrack(0,[])