class Solution:
    def trap(self, height: List[int]) -> int:
        pre=[0]*len(height)
        sub=[0]*len(height)
        m=height[0]
        for i in range(1,len(height)):
            pre[i]=m
            if height[i]>m:
                m=height[i]
        m=height[len(height)-1]
        for i in range(len(height)-2,-1,-1):
            sub[i]=m
            if height[i]>m:
                m=height[i]
        area=0
        for i in range(1,len(height)-1):
            a=min(pre[i],sub[i])-height[i]
            if a>0:
                area=area+a
        return area

