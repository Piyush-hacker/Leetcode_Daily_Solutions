class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        xr = defaultdict(lambda: (inf, 0))
        yr = defaultdict(lambda: (inf, 0))
        res = 0
        for x, y in buildings:
            mi, mx = xr[x]
            xr[x] = (min(mi, y), max(mx, y))
            mi, mx = yr[y]
            yr[y] = (min(mi, x), max(mx, x))  
        for x, y in buildings:
            if xr[x][0] < y < xr[x][1] and yr[y][0] < x < yr[y][1]:
                res += 1
        return res