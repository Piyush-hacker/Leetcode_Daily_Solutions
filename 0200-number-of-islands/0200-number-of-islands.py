from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        islands = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    islands += 1
                    # BFS to mark the whole island
                    q = deque([(r, c)])
                    grid[r][c] = "0"

                    while q:
                        x, y = q.popleft()
                        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                                grid[nx][ny] = "0"
                                q.append((nx, ny))

        return islands