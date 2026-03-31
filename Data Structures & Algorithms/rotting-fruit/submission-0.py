class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:


        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        fresh_count = 0

        def addrotten(r,c):
            nonlocal fresh_count
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1 :
                return 
            
            grid[r][c] = 2
            fresh_count -= 1
            q.append((r,c))
            return 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2 :
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        if fresh_count == 0: return 0
        
        time = -1
        while q :
            time += 1
            for i in range(len(q)):
                r,c = q.popleft()

                directions = [(1,0),(0,1),(-1,0),(0,-1)]

                for dr,dc in directions:
                    new_r, new_c = r+dr,c+dc
                    addrotten(new_r,new_c)

        return time if fresh_count == 0 else -1
        