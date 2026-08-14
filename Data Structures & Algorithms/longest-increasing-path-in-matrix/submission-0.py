class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        dp = [[0] * cols for _ in range(rows)]  # dp[i][j] = longest path starting at (i,j)

        def dfs(i, j, prev_val):
            if i < 0 or i >= rows or j < 0 or j >= cols or matrix[i][j] <= prev_val:
                return 0
            if dp[i][j] != 0:   # already computed
                return dp[i][j]

            max_len = 1
            for r, c in directions:
                max_len = max(max_len, 1 + dfs(i+r, j+c, matrix[i][j]))

            dp[i][j] = max_len
            return dp[i][j]

        longest = 0
        for r in range(rows):
            for c in range(cols):
                longest = max(longest, dfs(r, c, -float("inf")))

        return longest