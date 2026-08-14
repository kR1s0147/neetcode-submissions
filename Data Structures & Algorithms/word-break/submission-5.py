class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        h =  set(wordDict)
        dp = {}
        def dfs(i,j):
            if j > n:
                return False
            if (i,j) in dp:
                return dp[(i,j)]
            if s[i:j] in h:
                if j == n:
                    dp[(i,j)] = True
                    return True
                if dfs(j,j+1):
                    dp[(i,j)] = True
                    return True
            dp[(i,j)] = dfs(i,j+1)
            return dp[(i,j)]
        return dfs(0,1)
       



        