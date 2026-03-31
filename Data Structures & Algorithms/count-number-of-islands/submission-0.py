class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        row = len(grid)
        col = len(grid[0])
        island = 0
        visit = set()

        def dfs(r,c,grid,visit):
            if r < 0 or c < 0 or (r>= row) or (c >= col) or ((r,c) in visit) or (grid[r][c] == "0"):
                return
            
            visit.add((r,c))
            dfs(r+1,c,grid,visit)
            dfs(r,c+1,grid,visit)
            dfs(r-1,c,grid,visit)
            dfs(r,c-1,grid,visit)

            return 

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in visit:
                    dfs(r,c,grid,visit)
                    island +=1 

        return island
                
        