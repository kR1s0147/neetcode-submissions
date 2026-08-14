class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[1]*len(nums)
        r=[1]*len(nums)
        rv=1
        lv=1
        le=len(nums)
        for i in range(0,le):
            l[i]=lv
            lv=lv*nums[i]
        for i in range(le-1,-1,-1):
            r[i]=rv
            rv=rv*nums[i]
        for i in range(0,len(nums)):
            l[i]=l[i]*r[i]
        return l


