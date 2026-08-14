class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if not s or not t:
            return 0
    
        def dfs(i, path):
            # found a valid subsequence
            if len(path) == len(t):
                return 1 if "".join(path) == t else 0
            if i >= len(s):
                return 0
            # choice 1: take s[i]
            take = dfs(i + 1, path + [s[i]])
            # choice 2: skip s[i]
            skip = dfs(i + 1, path)
            return take + skip
        return dfs(0, [])
