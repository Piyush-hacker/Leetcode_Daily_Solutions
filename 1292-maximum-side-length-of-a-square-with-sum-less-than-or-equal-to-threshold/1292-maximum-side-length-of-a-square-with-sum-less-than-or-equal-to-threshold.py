class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        prefix = [[0] * (len(mat[0])+1)]
        for row in mat:
            prefix.append([0] + row)
            for idx in range(len(row)):
                prefix[-1][idx + 1] -= prefix[-2][idx] 
                prefix[-1][idx + 1] += prefix[-1][idx] 
                prefix[-1][idx + 1] += prefix[-2][idx + 1] 

        res = 0
        for r in range(len(prefix) - 1):
            for c in range(len(prefix[0]) - 1):
                end_r = r + res + 1
                end_c = c + res + 1
                while end_r < len(prefix) and end_c < len(prefix[0]) and prefix[end_r][end_c] - prefix[r][end_c] - prefix[end_r][c] + prefix[r][c] <= threshold:
                    end_r += 1
                    end_c += 1
                    res += 1
        return res  