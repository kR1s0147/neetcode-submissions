class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            b=[0]*26
            for j in i:
                b[ord(j)-97]=b[ord(j)-97]+1
            key=tuple(b)
            if key not in d:
                d[key]=[]
            d[key].append(i)
        return list(d.values())