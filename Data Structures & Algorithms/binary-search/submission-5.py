class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarysearch(s,l):
            if s>l:
                return -1
            m = int((s+l)/2)
            if nums[m] == target:
                return m
            
            elif target > nums[m]:
               return binarysearch(m+1,l)
            elif target < nums[m]:
               return binarysearch(s,m-1)

        return binarysearch(0,len(nums)-1)
           
        