class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        def dfs(i,j):
            if i>=len(text1) or  j>= len(text2):
                return 0

            if dp[i][j] != -1:
                return dp[i][j]
            if text1[i] == text2[j]:
                t =  1 + dfs(i+1,j+1)
                dp[i][j] = t
                return t
            t = max(dfs(i+1,j),dfs(i,j+1))
            dp[i][j] = t
            return t
        return dfs(0,0)