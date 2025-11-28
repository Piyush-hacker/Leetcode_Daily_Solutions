class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        def dfs(node, parent):
            curr_sum = values[node]
            for i in adj_list[node]:
                if i == parent:
                    continue
                curr_sum += dfs(i, node)
            if curr_sum % k == 0:
                self.res += 1
                return 0
            return curr_sum

        adj_list = [[] for _ in range(n)]
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        self.res = 0
        dfs(0, -1)
        return self.res