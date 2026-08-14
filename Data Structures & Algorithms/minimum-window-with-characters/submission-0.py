class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tar = {}
        for i in t:
            tar[i] = tar.get(i,0) + 1
        l=0
        count={}
        res = ""
        le = float("inf")
        have , need = 0 , len(tar)

        for r in range(len(s)):
            count[s[r]] =  count.get(s[r],0) + 1
            
            if s[r] in tar and tar[s[r]] == count[s[r]]:
                have+=1
            while have ==  need:
                if r-l+1 < le:
                    res = s[l:r+1]
                    le = r-l+1

                count[s[l]]-=1
                if s[l] in tar and count[s[l]] <  tar[s[l]]:
                    have-= 1
                l+=1

        return res 

        