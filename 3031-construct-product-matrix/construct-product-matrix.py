MOD = 12345

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(grid), len(grid[0])

        prefix = [[1] * COLS for _ in range(ROWS)]
        suffix = [[1] * COLS for _ in range(ROWS)]

        pre, suf = 1, 1

        # forward pass: fill prefix sum
        for r in range(ROWS):
            for c in range(COLS):
                prefix[r][c] = pre
                pre = (pre * grid[r][c]) % MOD

        # backward pass: fill suffix sum and compute result
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                suffix[r][c] = suf
                suf = (suf * grid[r][c]) % MOD
                grid[r][c] = (prefix[r][c] * suffix[r][c]) % MOD

        return grid