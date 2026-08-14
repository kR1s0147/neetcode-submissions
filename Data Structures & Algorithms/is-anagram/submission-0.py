class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            d1={}
            d2={}
            for i in range(0,len(s)):
                d1[s[i]]=0
                d2[t[i]]=0
            for i in range(0,len(s)):
                d1[s[i]]+=1
                d2[t[i]]+=1
            if d1==d2:
                return True
        return False