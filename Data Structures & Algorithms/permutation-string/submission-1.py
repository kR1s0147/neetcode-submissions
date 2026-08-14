class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        tar = {}
        for i in s1:
            tar[i] = tar.get(i,0) + 1
        l=0
        count = {}
        for r in range(len(s2)):
            count[s2[r]]=count.get(s2[r],0)+1
            if r-l+1 == len(s1):
                if tar == count:
                    return True
                else:
                    count[s2[l]] = count[s2[l]]-1
                    if count[s2[l]]==0:
                        del count[s2[l]]
                    l  = l+1
        return False

