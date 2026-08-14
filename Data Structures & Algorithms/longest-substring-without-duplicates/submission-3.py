class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        res=0
        t=[]
        while r < len(s):
            if s[r] not in t:
                t.append(s[r])
                r+=1
            elif s[r] in t:
                t=[]
                l+=1
                r=l
            res = max(res,len(t))
        return res