class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        r=0
        for i in s:
            if (i-1) not in s:
                l=1
                j=i
                while True:
                    if j+1 in s:
                        l=l+1
                        j=j+1
                    else :
                        break
                if r<l:
                    r=l
            else:
                continue 
        return r
        