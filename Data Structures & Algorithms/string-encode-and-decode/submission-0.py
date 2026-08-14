class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s=s+str(len(i))+"#"+i
        return s

    def decode(self, s: str) -> List[str]:
        l=[]
        i=0
        while i<len(s):
            j=s.find('#',i)
            le=int(s[i:j])
            l.append(str(s[j+1:j+1+le]))
            i=j+1+le
        return l