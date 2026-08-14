class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        self.m = len(word1) + len(word2)
        def dfs(i,j,c):
            if i >= len(word1):
                self.m = min(self.m,c + len(word2)-j)
                return 
            if j >= len(word2):
                self.m = min(self.m,c + len(word1)-i)
                return
            if word1[i] ==  word2[j]:
                dfs(i+1,j+1,c)
            else:
                dfs(i+1,j,c+1)
                dfs(i,j+1,c+1)
                dfs(i+1,j+1,c+1)
            return 
        dfs(0,0,0)
        return self.m
