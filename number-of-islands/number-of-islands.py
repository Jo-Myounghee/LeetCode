class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def is_land(x, y):
            if 0 <= x < len(grid[0]) and 0 <= y < len(grid) and grid[y][x] == '1':
                return True
            return False
        
        
        def dfs(x, y):
            if not is_land(x, y):
                return
            
            grid[y][x] = '0'
            
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
        
        cnt = 0
        for _y in range(len(grid)):
            for _x in range(len(grid[0])):
                if grid[_y][_x] == '1':
                    dfs(_x, _y)
                    cnt += 1
        return cnt