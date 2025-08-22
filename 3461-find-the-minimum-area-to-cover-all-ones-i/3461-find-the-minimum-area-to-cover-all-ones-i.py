class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        iMin, iMax, jMin, jMax=1000, -1, 1000, -1
        for i, row in enumerate(grid):
            if 1 in row:
                iMin=min(iMin, i)
                iMax=max(iMax, i)
        for j, col in enumerate(zip(*grid)):
            if 1 in col:
                jMin=min(jMin, j)
                jMax=max(jMax, j)
        return (iMax-iMin+1)*(jMax-jMin+1)

             