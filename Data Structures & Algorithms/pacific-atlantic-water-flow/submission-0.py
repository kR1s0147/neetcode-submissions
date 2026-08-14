class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        cols = len(heights[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        self.pacific = self.atlantic = False
        def dfs(r,c,prev):
            if r < 0 or c<0 or c>=cols or r>=row or heights[r][c] > prev:
                if r < 0 or c<0:
                    self.pacific = True
                elif c >= cols or r >= row:
                    self.atlantic = True
                return 

            tmp = heights[r][c]
            heights[r][c] = float('inf')

            for dr,dc in directions:
                dfs(r+dr,c+dc,tmp)
                if self.pacific and self.atlantic:
                    break
            heights[r][c] = tmp
        res = []
        for r in range(row):
            for c in range(cols):
                self.pacific = False
                self.atlantic = False
                dfs(r,c,float('inf'))
                if self.pacific and self.atlantic:
                    res.append([r,c])
        return res
        