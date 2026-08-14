class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        resLen , residx = 0, 0
        dp = [[False] * l for _ in range(l)]

        for i in range(l-1,-1,-1):
            for j in range(i,l):
                if s[j] == s[i]  and (j-i <=2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if resLen < (j-i+1):
                        residx = i
                        resLen = j-i+1


        return s[residx:residx+resLen]