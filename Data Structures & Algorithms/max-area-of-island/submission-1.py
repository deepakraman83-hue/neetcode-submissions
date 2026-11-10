class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        max_area,counter=0,0
        row,col=len(grid),len(grid[0])
        def dfs(r,c):
            if r<0 or c<0 or r>=row or c>=col or grid[r][c]==0:
                return 0
            grid[r][c]=0
            return (1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1))
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    current_area=dfs(r,c)
                    max_area=max(max_area,current_area)
        return max_area
#Time complexity: O(m×n)
#Space complexity: O(m×n)

        
