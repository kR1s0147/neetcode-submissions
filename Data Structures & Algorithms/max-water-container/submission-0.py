class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m=0
        l=0
        r=len(heights)-1
        while(l<r):
            a=min(heights[l],heights[r])*(r-l)
            if m<a:
                m=a
            if heights[l]<heights[r]:
                l=l+1
            else:
                r=r-1
        return m
        