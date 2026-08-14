class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row =  len(grid)
        cols = len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = []
        def dfs(r,c,dis):
            if r<0 or c <0 or r >= row or c >= cols or grid[r][c] == -1 or grid[r][c] == 0 or [r,c] in visited or grid[r][c] < dis:
                return 
            grid[r][c] = min(dis,grid[r][c])
            visited.append([r,c])
            for dr,dc in directions:
                dfs(r+dr,c+dc,dis+1)
            visited.pop()

        for r in range(row):
            for c in range(cols):
                if grid[r][c] == 0:
                    for dr, dc in directions:
                        dfs(r+dr,c+dc,1)