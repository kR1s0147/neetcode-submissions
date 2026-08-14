class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        l=[]
        for i in range(0,len(nums)):
            if d.get(target-nums[i])!=None:
                l.append(d[target-nums[i]])
                l.append(i)
            else:
                d[nums[i]]=i
        return l