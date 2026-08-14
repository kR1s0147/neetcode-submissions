from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        cols = len(grid[0])
        directions= [[1,0],[-1,0],[0,1],[0,-1]]
        queue = deque()
        maxTime = 0
        fresh = 0
        for r in range(row):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append([r,c,0])
                if grid[r][c] == 1:
                    fresh+=1
        if fresh == 0:
            return 0

        while queue:
            r,c,time = queue.popleft()
            maxTime = max(time,maxTime)

            for dr,dc in directions:
                r1,c1 = r+dr , c+dc
                if r1>=0 and c1 >=0 and r1 < row and c1<cols :
                    if  grid[r1][c1] == 1:
                        grid[r1][c1] = 2
                        fresh -=1
                        queue.append([r1,c1,time+1])
        if fresh > 0:
            return -1
        return maxTime
        
        
        